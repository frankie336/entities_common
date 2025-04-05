import time
from enum import Enum
from typing import List, Dict, Any, Optional

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    field_validator,
    model_validator,
)


class StatusEnum(str, Enum):
    deleted = "deleted"
    active = "active"
    queued = "queued"
    in_progress = "in_progress"
    pending_action = "action_required"
    completed = "completed"
    failed = "failed"
    cancelling = "cancelling"
    cancelled = "cancelled"
    pending = "pending"
    processing = "processing"
    expired = "expired"
    retrying = "retrying"
    inactive = "inactive"
    error = "error"


class VectorStoreCreate(BaseModel):
    shared_id: str = Field(
        ..., description="Client-generated unique ID used as DB primary key and Qdrant collection "
                         "name"
    )
    name: str = Field(
        ..., min_length=3, max_length=128, description="Human-friendly store name"
    )
    user_id: str = Field(
        ..., min_length=3, description="Owner user ID (must exist in the database)"
    )
    vector_size: int = Field(
        ..., gt=0, description="Dimensionality of the vectors (positive integer)"
    )
    distance_metric: str = Field(
        ..., description="Distance metric (COSINE, EUCLID, DOT)"
    )
    config: Optional[Dict[str, Any]] = Field(
        None, description="Additional configuration options"
    )

    @field_validator("distance_metric")
    @classmethod
    def validate_distance_metric(cls, v: str) -> str:
        allowed = {"COSINE", "EUCLID", "DOT"}
        upper = v.upper()
        if upper not in allowed:
            raise ValueError(f"Invalid distance metric: '{v}'. Must be one of {allowed}")
        return upper


class VectorStoreRead(BaseModel):
    id: str = Field(..., description="Unique identifier for the vector store")
    name: str = Field(..., description="Vector store name")
    user_id: str = Field(..., description="User who owns this store")
    collection_name: str = Field(..., description="Qdrant collection name")
    vector_size: int = Field(..., description="Vector dimensionality")
    distance_metric: str = Field(..., description="Metric used for comparison")
    created_at: int = Field(..., description="Unix timestamp when created")
    updated_at: Optional[int] = Field(None, description="Last modified timestamp")
    status: StatusEnum = Field(..., description="Vector store status")
    config: Optional[Dict[str, Any]] = Field(None, description="Optional config dict")
    file_count: int = Field(..., ge=0, description="Total file count")

    model_config = ConfigDict(from_attributes=True)


class VectorStoreUpdate(BaseModel):
    name: Optional[str] = Field(
        None, min_length=3, max_length=128, description="New vector store name"
    )
    status: Optional[StatusEnum] = Field(None, description="Status override")
    config: Optional[Dict[str, Any]] = Field(None, description="New config")


class VectorStoreFileCreate(BaseModel):
    file_id: str = Field(..., description="Client-assigned unique ID "
                                          "for the file record")
    file_name: str = Field(..., max_length=256, description="Original "
                                                            "filename")
    file_path: str = Field(..., max_length=1024, description="Identifier "
                                                             "in metadata")
    status: Optional[StatusEnum] = Field(None, description="Initial processing "
                                                           "state")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata dict")


class VectorStoreFileRead(BaseModel):
    id: str = Field(..., description="Record ID")
    vector_store_id: str = Field(..., description="Owning vector store")
    file_name: str = Field(..., description="Original file name")
    file_path: str = Field(..., description="Qdrant metadata path")
    processed_at: Optional[int] = Field(None, description="Last processing "
                                                          "change timestamp")
    status: StatusEnum = Field(..., description="Current processing state")
    error_message: Optional[str] = Field(None, description="Failure "
                                                           "reason if failed")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata dict")

    model_config = ConfigDict(from_attributes=True)


class VectorStoreFileUpdate(BaseModel):
    status: Optional[StatusEnum] = Field(None, description="Status override")
    error_message: Optional[str] = Field(None, description="New error message")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata "
                                                                 "replacement")


class VectorStoreList(BaseModel):
    vector_stores: List[VectorStoreRead]


class VectorStoreFileList(BaseModel):
    files: List[VectorStoreFileRead]


class VectorStoreLinkAssistant(BaseModel):
    assistant_ids: List[str] = Field(..., min_length=1, description="IDs to "
                                                                    "link")


class VectorStoreUnlinkAssistant(BaseModel):
    assistant_id: str = Field(..., description="ID to unlink")


class VectorStoreSearchResult(BaseModel):
    text: str = Field(..., description="Returned chunk")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Chunk "
                                                                 "metadata")
    score: float = Field(..., description="Vector similarity score")
    vector_id: Optional[str] = Field(None, description="Qdrant vector ID")
    store_id: Optional[str] = Field(None, description="Store ID")
    retrieved_at: int = Field(
        default_factory=lambda: int(time.time()), description="Unix timestamp"
    )


class SearchExplanation(BaseModel):
    base_score: float
    filters_passed: Optional[List[str]] = None
    boosts_applied: Optional[Dict[str, float]] = None
    final_score: float


class EnhancedVectorSearchResult(VectorStoreSearchResult):
    explanation: Optional[SearchExplanation] = Field(
        None, description="Scoring explanation if available"
    )


class VectorStoreAddRequest(BaseModel):
    texts: List[str] = Field(..., description="Chunks to index")
    vectors: List[List[float]] = Field(..., description="Embeddings per "
                                                        "chunk")
    metadata: List[Dict[str, Any]] = Field(..., description="Metadata per "
                                                            "chunk")

    @model_validator(mode="after")
    def check_lengths_match(self) -> "VectorStoreAddRequest":
        if not (len(self.texts) == len(self.vectors) == len(self.metadata)):
            raise ValueError(
                f"Lengths must match: texts({len(self.texts)}), "
                f"vectors({len(self.vectors)}), metadata({len(self.metadata)})"
            )
        return self
