#!/usr/bin/env python3
"""
Dashboard de Métricas para el Sistema de Memoria Semántica
Proporciona visualización y análisis de las consultas, uso de tokens y rendimiento del sistema.
"""

import os
import json
import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import requests

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de la aplicación
FASTAPI_URL = os.environ.get("FASTAPI_URL", "http://localhost:8000")
REFRESH_INTERVAL = 30  # segundos

# Inicializar la aplicación Dash
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="COAFI Memory Metrics Dashboard",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

# Definir el layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("COAFI Memory Metrics Dashboard", className="text-center my-4"),
            html.P("Monitoreo en tiempo real del sistema de memoria semántica", className="text-center text-muted"),
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Filtros", className="bg-primary text-white"),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Label("Rango de tiempo:"),
                            dcc.Dropdown(
                                id="time-range",
                                options=[
                                    {"label": "Última hora", "value": "1h"},
                                    {"label": "Últimas 24 horas", "value": "24h"},
                                    {"label": "Últimos 7 días", "value": "7d"},
                                    {"label": "Últimos 30 días", "value": "30d"},
                                ],
                                value="24h",
                                clearable=False,
                            ),
                        ], width=4),
                        dbc.Col([
                            html.Label("Mood:"),
                            dcc.Dropdown(
                                id="mood-filter",
                                options=[
                                    {"label": "Todos", "value": "all"},
                                    {"label": "Strategist", "value": "strategist"},
                                    {"label": "Engineer", "value": "engineer"},
                                    {"label": "Creative", "value": "creative"},
                                    {"label": "Aerospace", "value": "aerospace"},
                                ],
                                value="all",
                                clearable=False,
                            ),
                        ], width=4),
                        dbc.Col([
                            html.Label("Actualización:"),
                            dbc.Button(
                                "Actualizar ahora", 
                                id="refresh-button", 
                                color="primary", 
                                className="w-100"
                            ),
                            dcc.Interval(
                                id="refresh-interval",
                                interval=REFRESH_INTERVAL * 1000,
                                n_intervals=0,
                            ),
                        ], width=4),
                    ]),
                ]),
            ], className="mb-4"),
        ], width=12),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Resumen de Métricas", className="bg-primary text-white"),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3(id="total-queries", children="0"),
                                html.P("Consultas Totales"),
                            ], className="text-center border rounded p-3"),
                        ], width=3),
                        dbc.Col([
                            html.Div([
                                html.H3(id="total-tokens", children="0"),
                                html.P("Tokens Utilizados"),
                            ], className="text-center border rounded p-3"),
                        ], width=3),
                        dbc.Col([
                            html.Div([
                                html.H3(id="avg-latency", children="0 ms"),
                                html.P("Latencia Promedio"),
                            ], className="text-center border rounded p-3"),
                        ], width=3),
                        dbc.Col([
                            html.Div([
                                html.H3(id="cache-hit-rate", children="0%"),
                                html.P("Tasa de Aciertos de Caché"),
                            ], className="text-center border rounded p-3"),
                        ], width=3),
                    ]),
                ]),
            ], className="mb-4"),
        ], width=12),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Consultas por Hora", className="bg-primary text-white"),
                dbc.CardBody([
                    dcc.Graph(id="queries-by-hour"),
                ]),
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Uso de Tokens por Mood", className="bg-primary text-white"),
                dbc.CardBody([
                    dcc.Graph(id="tokens-by-mood"),
                ]),
            ]),
        ], width=6),
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Distribución de Latencia", className="bg-primary text-white"),
                dbc.CardBody([
                    dcc.Graph(id="latency-distribution"),
                ]),
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Tasa de Aciertos de Caché", className="bg-primary text-white"),
                dbc.CardBody([
                    dcc.Graph(id="cache-hit-rate-trend"),
                ]),
            ]),
        ], width=6),
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Consultas Recientes", className="bg-primary text-white"),
                dbc.CardBody([
                    html.Div(id="recent-queries-table"),
                ]),
            ]),
        ], width=12),
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Estado del Sistema", className="bg-primary text-white"),
                dbc.CardBody([
                    html.Div(id="system-status"),
                ]),
            ]),
        ], width=12),
    ]),
    
    # Almacenamiento de datos
    dcc.Store(id="query-data"),
    dcc.Store(id="system-data"),
    
    # Footer
    dbc.Row([
        dbc.Col([
            html.Hr(),
            html.P(
                "COAFI Memory Metrics Dashboard © 2024",
                className="text-center text-muted",
            ),
        ], width=12),
    ]),
], fluid=True)

# Funciones de utilidad
def fetch_query_data(time_range: str, mood: str = "all") -> pd.DataFrame:
    """Obtiene datos de consultas desde la API"""
    try:
        # Calcular rango de tiempo
        now = datetime.now()
        if time_range == "1h":
            start_time = now - timedelta(hours=1)
        elif time_range == "24h":
            start_time = now - timedelta(days=1)
        elif time_range == "7d":
            start_time = now - timedelta(days=7)
        else:  # 30d
            start_time = now - timedelta(days=30)
            
        # Construir parámetros de consulta
        params = {
            "start_time": start_time.isoformat(),
            "end_time": now.isoformat(),
        }
        
        if mood != "all":
            params["mood_id"] = mood
            
        # Realizar solicitud a la API
        response = requests.get(
            f"{FASTAPI_URL}/semantic-query/logs",
            params=params
        )
        
        if response.status_code != 200:
            logger.error(f"Error fetching query data: {response.status_code} - {response.text}")
            return pd.DataFrame()
            
        data = response.json()
        
        # Convertir a DataFrame
        df = pd.DataFrame(data["logs"])
        
        # Convertir timestamp a datetime
        if not df.empty and "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            
        return df
        
    except Exception as e:
        logger.error(f"Error fetching query data: {e}")
        return pd.DataFrame()

def fetch_system_status() -> Dict[str, Any]:
    """Obtiene el estado del sistema desde la API"""
    try:
        response = requests.get(f"{FASTAPI_URL}/semantic-query/stats")
        
        if response.status_code != 200:
            logger.error(f"Error fetching system status: {response.status_code} - {response.text}")
            return {}
            
        return response.json()
        
    except Exception as e:
        logger.error(f"Error fetching system status: {e}")
        return {}

# Callbacks
@app.callback(
    [
        Output("query-data", "data"),
        Output("system-data", "data"),
    ],
    [
        Input("refresh-button", "n_clicks"),
        Input("refresh-interval", "n_intervals"),
        Input("time-range", "value"),
        Input("mood-filter", "value"),
    ],
)
def update_data(n_clicks, n_intervals, time_range, mood):
    """Actualiza los datos cuando se solicita"""
    query_df = fetch_query_data(time_range, mood)
    system_status = fetch_system_status()
    
    return query_df.to_json(date_format="iso", orient="split"), json.dumps(system_status)

@app.callback(
    [
        Output("total-queries", "children"),
        Output("total-tokens", "children"),
        Output("avg-latency", "children"),
        Output("cache-hit-rate", "children"),
    ],
    [Input("query-data", "data")],
)
def update_summary_metrics(query_data):
    """Actualiza las métricas de resumen"""
    if not query_data:
        return "0", "0", "0 ms", "0%"
        
    df = pd.read_json(query_data, orient="split")
    
    if df.empty:
        return "0", "0", "0 ms", "0%"
        
    total_queries = len(df)
    total_tokens = df["token_count"].sum() if "token_count" in df.columns else 0
    
    # Formatear tokens para legibilidad
    if total_tokens >= 1_000_000:
        total_tokens_str = f"{total_tokens / 1_000_000:.2f}M"
    elif total_tokens >= 1_000:
        total_tokens_str = f"{total_tokens / 1_000:.1f}K"
    else:
        total_tokens_str = str(total_tokens)
    
    # Calcular latencia promedio
    if "processing_time" in df.columns:
        avg_latency = df["processing_time"].mean() * 1000  # convertir a ms
        avg_latency_str = f"{avg_latency:.0f} ms"
    else:
        avg_latency_str = "N/A"
    
    # Calcular tasa de aciertos de caché
    if "cache_hit" in df.columns:
        cache_hits = df["cache_hit"].sum()
        cache_hit_rate = (cache_hits / total_queries) * 100 if total_queries > 0 else 0
        cache_hit_rate_str = f"{cache_hit_rate:.1f}%"
    else:
        cache_hit_rate_str = "N/A"
    
    return str(total_queries), total_tokens_str, avg_latency_str, cache_hit_rate_str

@app.callback(
    Output("queries-by-hour", "figure"),
    [Input("query-data", "data")],
)
def update_queries_by_hour(query_data):
    """Actualiza el gráfico de consultas por hora"""
    if not query_data:
        return go.Figure()
        
    df = pd.read_json(query_data, orient="split")
    
    if df.empty or "timestamp" not in df.columns:
        return go.Figure()
    
    # Agrupar por hora
    df["hour"] = df["timestamp"].dt.floor("H")
    hourly_counts = df.groupby("hour").size().reset_index(name="count")
    
    fig = px.bar(
        hourly_counts, 
        x="hour", 
        y="count",
        labels={"hour": "Hora", "count": "Número de Consultas"},
        title="Consultas por Hora"
    )
    
    fig.update_layout(
        xaxis_title="Hora",
        yaxis_title="Número de Consultas",
        template="plotly_white"
    )
    
    return fig

@app.callback(
    Output("tokens-by-mood", "figure"),
    [Input("query-data", "data")],
)
def update_tokens_by_mood(query_data):
    """Actualiza el gráfico de uso de tokens por mood"""
    if not query_data:
        return go.Figure()
        
    df = pd.read_json(query_data, orient="split")
    
    if df.empty or "mood_id" not in df.columns or "token_count" not in df.columns:
        return go.Figure()
    
    # Rellenar valores nulos de mood_id
    df["mood_id"] = df["mood_id"].fillna("sin_mood")
    
    # Agrupar por mood
    mood_tokens = df.groupby("mood_id")["token_count"].sum().reset_index()
    
    fig = px.pie(
        mood_tokens,
        values="token_count",
        names="mood_id",
        title="Uso de Tokens por Mood",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    fig.update_traces(textposition="inside", textinfo="percent+label")
    
    return fig

@app.callback(
    Output("latency-distribution", "figure"),
    [Input("query-data", "data")],
)
def update_latency_distribution(query_data):
    """Actualiza el gráfico de distribución de latencia"""
    if not query_data:
        return go.Figure()
        
    df = pd.read_json(query_data, orient="split")
    
    if df.empty or "processing_time" not in df.columns:
        return go.Figure()
    
    # Convertir a milisegundos
    latencies_ms = df["processing_time"] * 1000
    
    fig = px.histogram(
        latencies_ms,
        nbins=20,
        labels={"value": "Latencia (ms)"},
        title="Distribución de Latencia",
        color_discrete_sequence=["#3366CC"]
    )
    
    fig.update_layout(
        xaxis_title="Latencia (ms)",
        yaxis_title="Frecuencia",
        template="plotly_white"
    )
    
    # Añadir línea vertical para la media
    mean_latency = latencies_ms.mean()
    fig.add_vline(
        x=mean_latency,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Media: {mean_latency:.1f} ms",
        annotation_position="top right"
    )
    
    return fig

@app.callback(
    Output("cache-hit-rate-trend", "figure"),
    [Input("query-data", "data")],
)
def update_cache_hit_rate_trend(query_data):
    """Actualiza el gráfico de tendencia de tasa de aciertos de caché"""
    if not query_data:
        return go.Figure()
        
    df = pd.read_json(query_data, orient="split")
    
    if df.empty or "timestamp" not in df.columns or "cache_hit" not in df.columns:
        return go.Figure()
    
    # Agrupar por hora y calcular tasa de aciertos
    df["hour"] = df["timestamp"].dt.floor("H")
    hourly_stats = df.groupby("hour").agg(
        cache_hits=("cache_hit", "sum"),
        total_queries=("cache_hit", "count")
    ).reset_index()
    
    hourly_stats["hit_rate"] = (hourly_stats["cache_hits"] / hourly_stats["total_queries"]) * 100
    
    fig = px.line(
        hourly_stats,
        x="hour",
        y="hit_rate",
        labels={"hour": "Hora", "hit_rate": "Tasa de Aciertos (%)"},
        title="Tendencia de Tasa de Aciertos de Caché"
    )
    
    fig.update_layout(
        xaxis_title="Hora",
        yaxis_title="Tasa de Aciertos (%)",
        template="plotly_white",
        yaxis=dict(range=[0, 100])
    )
    
    return fig

@app.callback(
    Output("recent-queries-table", "children"),
    [Input("query-data", "data")],
)
def update_recent_queries_table(query_data):
    """Actualiza la tabla de consultas recientes"""
    if not query_data:
        return html.P("No hay datos disponibles")
        
    df = pd.read_json(query_data, orient="split")
    
    if df.empty:
        return html.P("No hay datos disponibles")
    
    # Ordenar por timestamp (más reciente primero) y tomar las 10 más recientes
    df = df.sort_values("timestamp", ascending=False).head(10)
    
    # Formatear para la tabla
    table_data = []
    for _, row in df.iterrows():
        query_text = row.get("query_text", "")
        if len(query_text) > 50:
            query_text = query_text[:50] + "..."
            
        timestamp = row.get("timestamp")
        if timestamp:
            if isinstance(timestamp, str):
                timestamp = pd.to_datetime(timestamp)
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            timestamp_str = "N/A"
            
        mood_id = row.get("mood_id", "N/A")
        token_count = row.get("token_count", 0)
        processing_time = row.get("processing_time", 0) * 1000  # ms
        result_count = row.get("result_count", 0)
        cache_hit = "Sí" if row.get("cache_hit", False) else "No"
        
        table_data.append(
            html.Tr([
                html.Td(query_text),
                html.Td(timestamp_str),
                html.Td(mood_id),
                html.Td(f"{token_count}"),
                html.Td(f"{processing_time:.1f} ms"),
                html.Td(f"{result_count}"),
                html.Td(cache_hit),
            ])
        )
    
    # Crear tabla
    table = dbc.Table(
        [
            html.Thead(
                html.Tr([
                    html.Th("Consulta"),
                    html.Th("Timestamp"),
                    html.Th("Mood"),
                    html.Th("Tokens"),
                    html.Th("Tiempo"),
                    html.Th("Resultados"),
                    html.Th("Caché"),
                ])
            ),
            html.Tbody(table_data),
        ],
        bordered=True,
        hover=True,
        responsive=True,
        striped=True,
    )
    
    return table

@app.callback(
    Output("system-status", "children"),
    [Input("system-data", "data")],
)
def update_system_status(system_data):
    """Actualiza el estado del sistema"""
    if not system_data:
        return html.P("No hay datos disponibles")
        
    try:
        data = json.loads(system_data)
        
        # Crear tarjetas de estado
        cache_info = data.get("cache", {})
        vector_db_info = data.get("vector_db", {})
        metrics_info = data.get("metrics", {})
        
        cache_card = dbc.Card([
            dbc.CardHeader("Estado de Caché"),
            dbc.CardBody([
                html.P(f"Tipo: {cache_info.get('using_redis', False) and 'Redis' or 'Local'}"),
                html.P(f"Tamaño: {cache_info.get('size', 'N/A')}"),
                html.P(f"Aciertos: {cache_info.get('hits', 0)}"),
                html.P(f"Fallos: {cache_info.get('misses', 0)}"),
                html.P(f"Tasa de aciertos: {cache_info.get('hit_rate', 0) * 100:.1f}%"),
            ]),
        ], className="h-100")
        
        vector_db_card = dbc.Card([
            dbc.CardHeader("Base de Datos Vectorial"),
            dbc.CardBody([
                html.P(f"Tipo: {vector_db_info.get('type', 'N/A')}"),
                html.P(f"Dimensión: {vector_db_info.get('dimension', 'N/A')}"),
            ]),
        ], className="h-100")
        
        metrics_card = dbc.Card([
            dbc.CardHeader("Métricas Globales"),
            dbc.CardBody([
                html.P(f"Consultas totales: {metrics_info.get('queries_total', 0)}"),
                html.P(f"Tokens totales: {metrics_info.get('token_usage_total', 0)}"),
                html.P(f"Latencia promedio: {metrics_info.get('avg_latency', 0) * 1000:.1f} ms"),
            ]),
        ], className="h-100")
        
        return dbc.Row([
            dbc.Col(cache_card, width=4),
            dbc.Col(vector_db_card, width=4),
            dbc.Col(metrics_card, width=4),
        ])
        
    except Exception as e:
        logger.error(f"Error updating system status: {e}")
        return html.P(f"Error al procesar datos del sistema: {str(e)}")

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
