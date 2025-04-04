#!/usr/bin/env python3
"""
Digital Thread Orchestrator para GAIA AIR
Coordina el flujo de información entre las capas de diseño, producción y operaciones,
asegurando la trazabilidad completa del ciclo de vida del producto.
"""

import logging
import uuid
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gaia_air.digital_thread")

class ThreadEventType(Enum):
    """Tipos de eventos en el hilo digital"""
    DESIGN_CHANGE = "design_change"
    REQUIREMENT_UPDATE = "requirement_update"
    PRODUCTION_EVENT = "production_event"
    QUALITY_CHECK = "quality_check"
    MAINTENANCE_RECORD = "maintenance_record"
    SUPPLY_CHAIN_EVENT = "supply_chain_event"
    SUSTAINABILITY_METRIC = "sustainability_metric"

class DigitalThreadEvent:
    """Evento en el hilo digital que conecta todas las fases del ciclo de vida"""
    
    def __init__(self, 
                 event_type: ThreadEventType,
                 component_id: str,
                 data: Dict[str, Any],
                 source_system: str,
                 user_id: Optional[str] = None):
        self.event_id = str(uuid.uuid4())
        self.event_type = event_type
        self.component_id = component_id
        self.data = data
        self.source_system = source_system
        self.user_id = user_id
        self.timestamp = datetime.now()
        self.previous_events = []
        
    def add_reference(self, previous_event_id: str):
        """Añade referencia a un evento anterior para mantener la trazabilidad"""
        self.previous_events.append(previous_event_id)
        
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el evento a diccionario para almacenamiento/transmisión"""
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "component_id": self.component_id,
            "data": self.data,
            "source_system": self.source_system,
            "user_id": self.user_id,
            "timestamp": self.timestamp.isoformat(),
            "previous_events": self.previous_events
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DigitalThreadEvent':
        """Crea un evento a partir de un diccionario"""
        event = cls(
            event_type=ThreadEventType(data["event_type"]),
            component_id=data["component_id"],
            data=data["data"],
            source_system=data["source_system"],
            user_id=data.get("user_id")
        )
        event.event_id = data["event_id"]
        event.timestamp = datetime.fromisoformat(data["timestamp"])
        event.previous_events = data.get("previous_events", [])
        return event

class DigitalThreadOrchestrator:
    """
    Orquestador del hilo digital que coordina eventos entre sistemas
    y mantiene la trazabilidad completa del ciclo de vida del producto
    """
    
    def __init__(self, storage_adapter=None, event_bus=None):
        """
        Inicializa el orquestador con adaptadores para almacenamiento y bus de eventos
        
        Args:
            storage_adapter: Adaptador para almacenamiento persistente de eventos
            event_bus: Bus de eventos para publicación/suscripción
        """
        self.storage = storage_adapter or MockStorageAdapter()
        self.event_bus = event_bus or MockEventBus()
        self.handlers = {
            ThreadEventType.DESIGN_CHANGE: self._handle_design_change,
            ThreadEventType.REQUIREMENT_UPDATE: self._handle_requirement_update,
            ThreadEventType.PRODUCTION_EVENT: self._handle_production_event,
            ThreadEventType.QUALITY_CHECK: self._handle_quality_check,
            ThreadEventType.MAINTENANCE_RECORD: self._handle_maintenance_record,
            ThreadEventType.SUPPLY_CHAIN_EVENT: self._handle_supply_chain_event,
            ThreadEventType.SUSTAINABILITY_METRIC: self._handle_sustainability_metric
        }
        
    async def register_event(self, event: DigitalThreadEvent) -> str:
        """
        Registra un nuevo evento en el hilo digital
        
        Args:
            event: Evento a registrar
            
        Returns:
            ID del evento registrado
        """
        # Almacenar el evento
        await self.storage.store_event(event)
        
        # Publicar el evento en el bus
        await self.event_bus.publish(event.event_type.value, event.to_dict())
        
        # Procesar el evento según su tipo
        if event.event_type in self.handlers:
            await self.handlers[event.event_type](event)
        
        logger.info(f"Registered event {event.event_id} of type {event.event_type.value}")
        return event.event_id
    
    async def query_component_history(self, component_id: str) -> List[Dict[str, Any]]:
        """
        Consulta el historial completo de un componente
        
        Args:
            component_id: ID del componente
            
        Returns:
            Lista de eventos relacionados con el componente
        """
        events = await self.storage.get_events_by_component(component_id)
        return [event.to_dict() for event in events]
    
    async def trace_lineage(self, event_id: str) -> Dict[str, Any]:
        """
        Traza el linaje completo de un evento, siguiendo todas las referencias
        
        Args:
            event_id: ID del evento
            
        Returns:
            Grafo de eventos relacionados
        """
        # Implementación de algoritmo de trazado de grafo
        visited = set()
        event_graph = {"nodes": [], "edges": []}
        
        await self._trace_recursive(event_id, visited, event_graph)
        
        return event_graph
    
    async def _trace_recursive(self, event_id: str, visited: set, graph: Dict[str, Any]):
        """Función recursiva auxiliar para trazar el linaje"""
        if event_id in visited:
            return
        
        visited.add(event_id)
        event = await self.storage.get_event(event_id)
        
        if not event:
            return
            
        # Añadir nodo al grafo
        graph["nodes"].append({
            "id": event.event_id,
            "type": event.event_type.value,
            "component": event.component_id,
            "timestamp": event.timestamp.isoformat()
        })
        
        # Procesar eventos anteriores
        for prev_id in event.previous_events:
            # Añadir arista al grafo
            graph["edges"].append({
                "source": prev_id,
                "target": event.event_id
            })
            
            # Procesar recursivamente
            await self._trace_recursive(prev_id, visited, graph)
    
    async def _handle_design_change(self, event: DigitalThreadEvent):
        """Maneja eventos de cambio de diseño"""
        # Notificar a sistemas PLM
        # Actualizar documentación técnica
        # Evaluar impacto en producción
        logger.info(f"Processing design change for component {event.component_id}")
        
    async def _handle_requirement_update(self, event: DigitalThreadEvent):
        """Maneja eventos de actualización de requisitos"""
        # Actualizar matriz de trazabilidad
        # Verificar conformidad con estándares
        logger.info(f"Processing requirement update for component {event.component_id}")
        
    async def _handle_production_event(self, event: DigitalThreadEvent):
        """Maneja eventos de producción"""
        # Actualizar estado de fabricación
        # Registrar métricas de producción
        logger.info(f"Processing production event for component {event.component_id}")
        
    async def _handle_quality_check(self, event: DigitalThreadEvent):
        """Maneja eventos de control de calidad"""
        # Registrar resultados de inspección
        # Actualizar certificaciones
        logger.info(f"Processing quality check for component {event.component_id}")
        
    async def _handle_maintenance_record(self, event: DigitalThreadEvent):
        """Maneja registros de mantenimiento"""
        # Actualizar historial de servicio
        # Programar próximo mantenimiento
        logger.info(f"Processing maintenance record for component {event.component_id}")
        
    async def _handle_supply_chain_event(self, event: DigitalThreadEvent):
        """Maneja eventos de cadena de suministro"""
        # Actualizar inventario
        # Verificar conformidad de proveedores
        logger.info(f"Processing supply chain event for component {event.component_id}")
        
    async def _handle_sustainability_metric(self, event: DigitalThreadEvent):
        """Maneja métricas de sostenibilidad"""
        # Actualizar indicadores ESG
        # Verificar cumplimiento de objetivos
        logger.info(f"Processing sustainability metric for component {event.component_id}")

# Adaptadores mock para demostración
class MockStorageAdapter:
    """Adaptador mock para almacenamiento de eventos"""
    
    def __init__(self):
        self.events = {}
        
    async def store_event(self, event: DigitalThreadEvent):
        """Almacena un evento"""
        self.events[event.event_id] = event
        
    async def get_event(self, event_id: str) -> Optional[DigitalThreadEvent]:
        """Recupera un evento por ID"""
        return self.events.get(event_id)
        
    async def get_events_by_component(self, component_id: str) -> List[DigitalThreadEvent]:
        """Recupera eventos por componente"""
        return [e for e in self.events.values() if e.component_id == component_id]

class MockEventBus:
    """Bus de eventos mock para demostración"""
    
    async def publish(self, topic: str, message: Dict[str, Any]):
        """Publica un mensaje en un tema"""
        logger.info(f"Published message to topic {topic}")
        
    async def subscribe(self, topic: str, callback):
        """Suscribe a un tema"""
        logger.info(f"Subscribed to topic {topic}")

# Ejemplo de uso
async def example_usage():
    """Ejemplo de uso del orquestador de hilo digital"""
    orchestrator = DigitalThreadOrchestrator()
    
    # Registrar un evento de diseño
    design_event = DigitalThreadEvent(
        event_type=ThreadEventType.DESIGN_CHANGE,
        component_id="wing_assembly_001",
        data={
            "change_type": "material_update",
            "previous_material": "aluminum_7075",
            "new_material": "carbon_composite_tc500",
            "weight_reduction": "12.5%",
            "strength_increase": "8.3%"
        },
        source_system="PLM_SYSTEM",
        user_id="engineer_jane_doe"
    )
    
    design_event_id = await orchestrator.register_event(design_event)
    
    # Registrar un evento de producción relacionado
    production_event = DigitalThreadEvent(
        event_type=ThreadEventType.PRODUCTION_EVENT,
        component_id="wing_assembly_001",
        data={
            "operation": "composite_layup",
            "machine_id": "autoclave_03",
            "duration": "4.5h",
            "quality_score": 0.98
        },
        source_system="MES_SYSTEM",
        user_id="operator_john_smith"
    )
    
    # Añadir referencia al evento de diseño
    production_event.add_reference(design_event_id)
    
    await orchestrator.register_event(production_event)
    
    # Consultar historial del componente
    history = await orchestrator.query_component_history("wing_assembly_001")
    print(f"Component history: {json.dumps(history, indent=2)}")
    
    # Trazar linaje del evento de producción
    lineage = await orchestrator.trace_lineage(production_event.event_id)
    print(f"Event lineage: {json.dumps(lineage, indent=2)}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(example_usage())
