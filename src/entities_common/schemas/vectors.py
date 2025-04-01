import time
from enum import Enum
from typing import List, Dict, Any, Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator
from entities_common.schemas.enums import StatusEnum  # assuming this defines status strings like "active", "deleted", etc.

# ---------------------------------------------------------------------
# Enums for response status
# ---------------------------------------------------------------------
class VectorStoreStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    processing = "processing"
    error = "error"


# ---------------------------------------------------------------------
# Request Schemas (for DB sync) - these are the payloads our API accepts
# ---------------------------------------------------------------------
class VectorStoreCreate(BaseModel):
    shared_id: str = Field(..., description="Pre-generated shared UUID for sync between DB and vector engine")
    name: str = Field(..., min_length=3, max_length=128, description="Human-friendly store name")
    user_id: str = Field(..., min_length=3, description="Owner user ID (must exist in the database)")
    vector_size: int = Field(..., gt=0, description="Dimensionality of the vectors (positive integer)")
    distance_metric: str = Field(..., description="Distance metric (COSINE, EUCLID, DOT)")
    config: Optional[Dict[str, Any]] = Field(None, description="Additional configuration options")

    @field_validator("distance_metric")
    @classmethod
    def validate_distance_metric(cls, v: str) -> str:
        allowed = {"COSINE", "EUCLID", "DOT"}
        upper = v.upper()
        if upper not in allowed:
            raise ValueError(f"Invalid distance metric: '{v}'. Must be one of {allowed}")
        return upper

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------------------------------------
# Response Schemas - what we send back from our API after creation etc.
# ---------------------------------------------------------------------
class VectorStoreRead(BaseModel):
    id: str = Field(..., description="Unique identifier for the vector store", example="vectorstore_123")
    name: str = Field(..., description="Name of the vector store", example="My Vector Store")
    user_id: str = Field(..., description="ID of the owner user", example="user_123")
    collection_name: str = Field(..., description="Name of the vector collection", example="my_movie_db")
    vector_size: int = Field(..., description="Dimensionality of stored vectors", example=384)
    distance_metric: str = Field(..., description="Distance metric used (COSINE, EUCLID, DOT)", example="COSINE")
    created_at: int = Field(..., description="Unix timestamp when the vector store was created", example=1640995200)
    updated_at: Optional[int] = Field(None, description="Unix timestamp when last updated", example=1641081600)
    status: VectorStoreStatus = Field(..., description="Current status of the vector store")
    config: Optional[Dict[str, Any]] = Field(None, description="Additional configuration details")
    file_count: int = Field(0, description="Number of files in the vector store", example=10)

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------------------------------------
# Update schema for vector store (partial update)
# ---------------------------------------------------------------------
class VectorStoreUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=128)
    status: Optional[VectorStoreStatus] = None
    config: Optional[Dict[str, Any]] = None


# ---------------------------------------------------------------------
# File schemas
# ---------------------------------------------------------------------
class VectorStoreFileCreate(BaseModel):
    file_name: str = Field(..., max_length=256)
    file_path: str = Field(..., max_length=1024)
    metadata: Optional[Dict[str, Any]] = None


class VectorStoreFileRead(BaseModel):
    id: str
    file_name: str
    file_path: str
    processed_at: Optional[int] = None
    status: StatusEnum
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    model_config = ConfigDict(from_attributes=True)


class VectorStoreFileUpdate(BaseModel):
    status: Optional[StatusEnum] = None
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class VectorStoreList(BaseModel):
    vector_stores: List[VectorStoreRead]


class VectorStoreFileList(BaseModel):
    files: List[VectorStoreFileRead]


# ---------------------------------------------------------------------
# Assistant Linking Schemas
# ---------------------------------------------------------------------
class VectorStoreLinkAssistant(BaseModel):
    assistant_ids: List[str] = Field(..., min_items=1, description="List of assistant IDs to link")


class VectorStoreUnlinkAssistant(BaseModel):
    assistant_id: str = Field(..., description="Assistant ID to unlink")


# ---------------------------------------------------------------------
# Search Schemas
# ---------------------------------------------------------------------
class VectorStoreSearchResult(BaseModel):
    text: str
    metadata: Optional[dict] = None
    score: float
    vector_id: Optional[str] = Field("", description="ID of the vector point", example="point_123")
    store_id: Optional[str] = Field("", description="ID of the vector store", example="vectorstore_123")
    retrieved_at: int = Field(default_factory=lambda: int(time.time()), description="Unix timestamp of retrieval")


class SearchExplanation(BaseModel):
    base_score: float
    filters_passed: List[str]
    boosts_applied: Dict[str, float]
    final_score: float


class EnhancedVectorSearchResult(VectorStoreSearchResult):
    explanation: Optional[SearchExplanation] = None


# ---------------------------------------------------------------------
# Request Schema for Adding Documents to the Store
# ---------------------------------------------------------------------
class VectorStoreAddRequest(BaseModel):
    texts: List[str] = Field(..., description="List of texts to add to the vector store")
    vectors: List[List[float]] = Field(..., description="Vector embeddings corresponding to each text")
    metadata: List[Dict[str, Any]] = Field(..., description="Metadata dictionaries corresponding to each text")

    @field_validator('vectors')
    @classmethod
    def validate_vectors_length(cls, v, values):
        texts = values.get('texts')
        if texts is not None and len(v) != len(texts):
            raise ValueError("The number of vectors must match the number of texts")
        return v

    @field_validator('metadata')
    @classmethod
    def validate_metadata_length(cls, v, values):
        texts = values.get('texts')
        if texts is not None and len(v) != len(texts):
            raise ValueError("The number of metadata entries must match the number of texts")
        return v
