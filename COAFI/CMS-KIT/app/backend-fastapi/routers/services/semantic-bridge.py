#!/usr/bin/env python3
"""
Semantic Bridge Router for COAFI API
Provides endpoints for semantic queries, memory operations, and system statistics.
"""

import time
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, Body
from pydantic import BaseModel, Field

# Import memory service
try:
    from services.memory import (
        memory_service, 
        MemoryItem, 
        MemoryQuery, 
        MemoryResult, 
        MemoryStats
    )
    MEMORY_SERVICE_AVAILABLE = True
except ImportError:
    MEMORY_SERVICE_AVAILABLE = False
    logging.warning("Memory service not available. Using mock implementations.")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("coafi.semantic_bridge")

# Create router
router = APIRouter()

# Models for API requests and responses
class SemanticQueryRequest(BaseModel):
    """Request model for semantic queries"""
    query: str
    mood_id: Optional[str] = None
    folder_id: Optional[str] = None
    conversation_id: Optional[str] = None
    min_similarity: float = 0.7
    token_limit: int = 1000
    max_results: int = 20
    include_metadata: bool = True

class SemanticQueryResponse(BaseModel):
    """Response model for semantic queries"""
    results: List[Dict[str, Any]]
    total_results: int
    processing_time: float
    token_count: int = 0
    query_embedding: Optional[List[float]] = None

class MemoryItemRequest(BaseModel):
    """Request model for adding memory items"""
    content: str
    source_type: str = "memory_layer"
    metadata: Dict[str, Any] = Field(default_factory=dict)

class MemoryItemResponse(BaseModel):
    """Response model for memory operations"""
    success: bool
    id: Optional[str] = None
    error: Optional[str] = None

class MemoryCleanupRequest(BaseModel):
    """Request model for memory cleanup operations"""
    cleanup_type: str  # duplicates, low_quality, compress
    similarity_threshold: float = 0.92
    folder_id: Optional[str] = None

class MemoryCleanupResponse(BaseModel):
    """Response model for memory cleanup operations"""
    success: bool
    stats: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class SystemStatsResponse(BaseModel):
    """Response model for system statistics"""
    vector_db: Dict[str, Any] = Field(default_factory=dict)
    cache: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, Any] = Field(default_factory=dict)

class QueryLogEntry(BaseModel):
    """Model for query log entries"""
    query_text: str
    timestamp: datetime
    mood_id: Optional[str] = None
    token_count: int = 0
    processing_time: float = 0
    result_count: int = 0
    cache_hit: bool = False

class QueryLogsResponse(BaseModel):
    """Response model for query logs"""
    logs: List[Dict[str, Any]]
    total: int

class TrendDataResponse(BaseModel):
    """Response model for trend data"""
    dates: List[str]
    values: List[float]

# Mock implementations for when memory service is not available
class MockMemoryService:
    """Mock implementation of memory service for testing"""
    
    async def query_memory(self, query: Any):
        """Mock query implementation"""
        time.sleep(0.2)  # Simulate processing time
        
        results = []
        for i in range(5):
            results.append({
                "id": f"mock_{i}",
                "content": f"This is mock content {i} for query: {query.query}",
                "similarity_score": max(0.7, 1.0 - (i * 0.05)),
                "source_type": ["memory_layer", "message", "conversation", "summary"][i % 4],
                "metadata": {
                    "timestamp": datetime.now().isoformat(),
                    "mood_id": query.mood_id,
                    "folder_id": query.folder_id or "default"
                }
            })
        
        stats = {
            "total_items": len(results),
            "total_tokens": sum(len(r["content"]) // 4 for r in results),
            "avg_similarity": sum(r["similarity_score"] for r in results) / len(results),
            "query_time_ms": 200.0,
            "cache_hit_rate": 0.0,
            "embedding_time_ms": 150.0
        }
        
        return results, stats
    
    async def get_embedding(self, text: str):
        """Mock embedding implementation"""
        time.sleep(0.1)
        return [0.1] * 10  # Return a small mock embedding
    
    async def store_memory(self, item: Any):
        """Mock store implementation"""
        return f"mock_{int(time.time())}"

# Initialize mock service if needed
if not MEMORY_SERVICE_AVAILABLE:
    mock_memory_service = MockMemoryService()

# Query logs storage (in-memory for demo)
query_logs = []

# Endpoints
@router.post("/", response_model=SemanticQueryResponse)
async def semantic_query(query: SemanticQueryRequest):
    """
    Execute a semantic query against the memory system
    
    Returns semantically similar content based on the query text
    """
    start_time = time.time()
    
    try:
        # Create memory query from request
        memory_query = MemoryQuery(
            query=query.query,
            mood_id=query.mood_id,
            folder_id=query.folder_id,
            conversation_id=query.conversation_id,
            min_similarity=query.min_similarity,
            token_limit=query.token_limit,
            max_results=query.max_results,
            include_metadata=query.include_metadata
        )
        
        # Get embedding for the query
        if MEMORY_SERVICE_AVAILABLE:
            query_embedding = await memory_service.get_embedding(query.query)
            memory_query.embedding = query_embedding
            
            # Execute query
            results, stats = await memory_service.query_memory(memory_query)
            
            # Convert results to dict for response
            results_dict = [result.dict() for result in results]
            
            # Calculate token count
            token_count = stats.total_tokens
        else:
            # Use mock implementation
            query_embedding = await mock_memory_service.get_embedding(query.query)
            memory_query.embedding = query_embedding
            
            # Execute query
            results_dict, stats = await mock_memory_service.query_memory(memory_query)
            
            # Calculate token count
            token_count = sum(len(r["content"]) // 4 for r in results_dict)
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        # Log the query
        query_logs.append({
            "query_text": query.query,
            "timestamp": datetime.now(),
            "mood_id": query.mood_id,
            "token_count": token_count,
            "processing_time": processing_time,
            "result_count": len(results_dict),
            "cache_hit": stats.get("cache_hit_rate", 0) > 0 if isinstance(stats, dict) else stats.cache_hit_rate > 0
        })
        
        # Limit query logs to last 1000 entries
        if len(query_logs) > 1000:
            query_logs.pop(0)
        
        # Return response
        return {
            "results": results_dict,
            "total_results": len(results_dict),
            "processing_time": processing_time,
            "token_count": token_count,
            "query_embedding": query_embedding[:5] if query.include_metadata else None  # Only include first 5 dimensions
        }
    
    except Exception as e:
        logger.error(f"Error executing semantic query: {e}")
        raise HTTPException(status_code=500, detail=f"Error executing query: {str(e)}")

@router.post("/rag", response_model=Dict[str, Any])
async def generate_rag_response(
    query: str = Body(..., embed=True),
    context_results: List[Dict[str, Any]] = Body(..., embed=True),
    model: str = Body("gpt-4o", embed=True),
    temperature: float = Body(0.7, embed=True),
    include_citations: bool = Body(True, embed=True)
):
    """
    Generate a response using Retrieval-Augmented Generation (RAG)
    
    Uses the provided context results to generate a response to the query
    """
    try:
        if not MEMORY_SERVICE_AVAILABLE:
            # Mock implementation
            time.sleep(0.5)
            return {
                "response": f"This is a mock RAG response to: {query}\n\nBased on the provided context, I can tell you that aerospace documentation requires precision and technical accuracy. [1][2]",
                "model": model,
                "processing_time": 0.5
            }
        
        # Convert context results to MemoryResult objects
        memory_results = []
        for result in context_results:
            memory_results.append(MemoryResult(
                id=result.get("id", ""),
                content=result.get("content", ""),
                similarity_score=result.get("similarity_score", 0.0),
                source_type=result.get("source_type", "unknown"),
                metadata=result.get("metadata", {}),
                token_count=len(result.get("content", "")) // 4
            ))
        
        # Generate RAG response
        start_time = time.time()
        response = await memory_service.generate_rag_response(
            query=query,
            memory_results=memory_results,
            model=model,
            temperature=temperature,
            include_citations=include_citations
        )
        
        processing_time = time.time() - start_time
        
        return {
            "response": response,
            "model": model,
            "processing_time": processing_time
        }
    
    except Exception as e:
        logger.error(f"Error generating RAG response: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating RAG response: {str(e)}")

@router.post("/memory", response_model=MemoryItemResponse)
async def add_memory_item(item: MemoryItemRequest):
    """
    Add a new item to the memory system
    
    Stores content with associated metadata for future retrieval
    """
    try:
        # Generate a unique ID based on timestamp and content hash
        import hashlib
        content_hash = hashlib.md5(item.content.encode()).hexdigest()[:8]
        item_id = f"mem_{int(time.time())}_{content_hash}"
        
        if MEMORY_SERVICE_AVAILABLE:
            # Get embedding for the content
            embedding = await memory_service.get_embedding(item.content)
            
            # Create memory item
            memory_item = MemoryItem(
                id=item_id,
                content=item.content,
                embedding=embedding,
                metadata=item.metadata
            )
            
            # Store in memory service
            stored_id = await memory_service.store_memory(memory_item)
            
            return {
                "success": True,
                "id": stored_id
            }
        else:
            # Use mock implementation
            stored_id = await mock_memory_service.store_memory(item)
            
            return {
                "success": True,
                "id": stored_id
            }
    
    except Exception as e:
        logger.error(f"Error adding memory item: {e}")
        return {
            "success": False,
            "error": str(e)
        }

@router.post("/memory/cleanup", response_model=MemoryCleanupResponse)
async def cleanup_memory(request: MemoryCleanupRequest):
    """
    Run cleanup operations on the memory system
    
    Supports deduplication, quality filtering, and compression
    """
    try:
        if not MEMORY_SERVICE_AVAILABLE:
            # Mock implementation
            time.sleep(1.0)
            return {
                "success": True,
                "stats": {
                    "processed": 100,
                    "affected": 15,
                    "bytes_saved": 1024 * 1024 * 2  # 2 MB
                }
            }
        
        # In a real implementation, this would call the memory service cleanup method
        # For now, return a mock response
        return {
            "success": True,
            "stats": {
                "processed": 100,
                "affected": 15,
                "bytes_saved": 1024 * 1024 * 2  # 2 MB
            }
        }
    
    except Exception as e:
        logger.error(f"Error cleaning up memory: {e}")
        return {
            "success": False,
            "error": str(e)
        }

@router.get("/stats", response_model=SystemStatsResponse)
async def get_system_stats():
    """
    Get system statistics and metrics
    
    Returns information about vector database, cache, and performance metrics
    """
    try:
        if not MEMORY_SERVICE_AVAILABLE:
            # Mock implementation
            return {
                "vector_db": {
                    "type": "mock",
                    "dimension": 1536,
                    "total_vectors": 1250,
                    "memory_usage": 1024 * 1024 * 50,  # 50 MB
                    "distribution": {
                        "message": 35,
                        "conversation": 25,
                        "summary": 20,
                        "memory_layer": 20
                    }
                },
                "cache": {
                    "using_redis": False,
                    "size": 100,
                    "hits": 75,
                    "misses": 25,
                    "hit_rate": 0.75
                },
                "metrics": {
                    "queries_total": len(query_logs),
                    "token_usage_total": sum(log.get("token_count", 0) for log in query_logs),
                    "avg_query_time_ms": 150.0,
                    "avg_embedding_time_ms": 100.0,
                    "query_performance": {
                        "last_24h": [
                            {"hour": "00:00", "avg_time": 120, "count": 5},
                            {"hour": "04:00", "avg_time": 110, "count": 8},
                            {"hour": "08:00", "avg_time": 150, "count": 15},
                            {"hour": "12:00", "avg_time": 180, "count": 25},
                            {"hour": "16:00", "avg_time": 160, "count": 20},
                            {"hour": "20:00", "avg_time": 130, "count": 10}
                        ]
                    }
                }
            }
        
        # In a real implementation, this would get stats from the memory service
        # For now, return a mock response similar to the one above
        stats = {
            "vector_db": {
                "type": memory_service.vector_db_type,
                "dimension": memory_service.vector_dimension,
                "total_vectors": 1250,  # This would come from the actual service
                "memory_usage": 1024 * 1024 * 50,  # 50 MB
                "distribution": {
                    "message": 35,
                    "conversation": 25,
                    "summary": 20,
                    "memory_layer": 20
                }
            },
            "cache": {
                "using_redis": memory_service.cache_type == "redis",
                "size": len(memory_service.local_cache) if memory_service.cache_type == "local" else 100,
                "hits": memory_service.stats.get("cache_hits", 0),
                "misses": memory_service.stats.get("cache_misses", 0),
                "hit_rate": memory_service.stats.get("cache_hits", 0) / 
                           (memory_service.stats.get("cache_hits", 0) + memory_service.stats.get("cache_misses", 1))
            },
            "metrics": {
                "queries_total": memory_service.stats.get("queries_total", 0),
                "token_usage_total": sum(log.get("token_count", 0) for log in query_logs),
                "avg_query_time_ms": memory_service.stats.get("avg_query_time_ms", 0),
                "avg_embedding_time_ms": memory_service.stats.get("avg_embedding_time_ms", 0),
                "query_performance": {
                    "last_24h": [
                        {"hour": "00:00", "avg_time": 120, "count": 5},
                        {"hour": "04:00", "avg_time": 110, "count": 8},
                        {"hour": "08:00", "avg_time": 150, "count": 15},
                        {"hour": "12:00", "avg_time": 180, "count": 25},
                        {"hour": "16:00", "avg_time": 160, "count": 20},
                        {"hour": "20:00", "avg_time": 130, "count": 10}
                    ]
                }
            }
        }
        
        return stats
    
    except Exception as e:
        logger.error(f"Error getting system stats: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting system stats: {str(e)}")

@router.get("/logs", response_model=QueryLogsResponse)
async def get_query_logs(
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    mood_id: Optional[str] = None,
    limit: int = Query(100, ge=1, le=1000)
):
    """
    Get query logs for the specified time period
    
    Filters logs by time range and mood, with pagination
    """
    try:
        # Parse time range
        start_dt = datetime.fromisoformat(start_time) if start_time else datetime.now() - timedelta(days=1)
        end_dt = datetime.fromisoformat(end_time) if end_time else datetime.now()
        
        # Filter logs
        filtered_logs = []
        for log in query_logs:
            log_time = log["timestamp"]
            if start_dt <= log_time <= end_dt:
                if mood_id is None or log.get("mood_id") == mood_id:
                    filtered_logs.append(log)
        
        # Sort by timestamp (newest first)
        filtered_logs.sort(key=lambda x: x["timestamp"], reverse=True)
        
        # Apply limit
        limited_logs = filtered_logs[:limit]
        
        # Convert datetime to string for JSON serialization
        for log in limited_logs:
            log["timestamp"] = log["timestamp"].isoformat()
        
        return {
            "logs": limited_logs,
            "total": len(filtered_logs)
        }
    
    except Exception as e:
        logger.error(f"Error getting query logs: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting query logs: {str(e)}")

@router.get("/trend", response_model=TrendDataResponse)
async def get_memory_trend(days: int = Query(7, ge=1, le=30)):
    """
    Get memory usage trend data
    
    Returns daily memory usage for the specified number of days
    """
    try:
        # Generate mock trend data
        now = datetime.now()
        dates = [(now - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days, -1, -1)]
        
        # Generate some realistic looking growth pattern
        base_value = 50  # Start at 50 MB
        values = []
        for i in range(len(dates)):
            # Add some randomness but with an overall growth trend
            growth = i * 1.5  # Linear growth component
            random_factor = (i % 3 - 1) * 2  # Some fluctuation
            value = base_value + growth + random_factor
            values.append(round(value, 1))
        
        return {
            "dates": dates,
            "values": values
        }
    
    except Exception as e:
        logger.error(f"Error getting memory trend: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting memory trend: {str(e)}")
