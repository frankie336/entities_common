import time
from enum import Enum
from typing import List, Dict, Any, Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator


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


# ---------------------------------------------------------------------
# Request Schemas (for DB sync) - Payloads API accepts
# ---------------------------------------------------------------------


class VectorStoreCreate(BaseModel):
    shared_id: str = Field(
        ...,
        description="Client-generated unique ID (e.g., vs_...). Used for DB primary key "
        "and "
        "Qdrant collection name.",
    )
    name: str = Field(
        ...,
        min_length=3,
        max_length=128,
        description="Human-friendly store name",
    )
    user_id: str = Field(
        ...,
        min_length=3,
        description="Owner user ID (must exist in the database)",
    )
    vector_size: int = Field(
        ...,
        gt=0,
        description="Dimensionality of the vectors (positive integer)",
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
            raise ValueError(
                f"Invalid distance metric: '{v}'. Must be one of {allowed}"
            )
        return upper


# ---------------------------------------------------------------------
# Response Schemas - What API sends back
# ---------------------------------------------------------------------
class VectorStoreRead(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier for the vector store (same as shared_id/collection_name)",
        example="vs_abc123",
    )
    name: str = Field(
        ...,
        description="Name of the vector store",
        example="My Project Documents",
    )
    user_id: str = Field(
        ..., description="ID of the owner user", example="user_xyz789"
    )
    collection_name: str = Field(
        ...,
        description="Name of the corresponding Qdrant collection (same as id)",
        example="vs_abc123",
    )
    vector_size: int = Field(
        ..., description="Dimensionality of stored vectors", example=384
    )
    distance_metric: str = Field(
        ...,
        description="Distance metric used (COSINE, EUCLID, DOT)",
        example="COSINE",
    )
    created_at: int = Field(
        ...,
        description="Unix timestamp when the vector store record was created",
        example=1640995200,
    )
    updated_at: Optional[int] = Field(
        None,
        description="Unix timestamp when the record was last updated",
        example=1641081600,
    )
    # Use the consistent, richer StatusEnum
    status: StatusEnum = Field(
        ...,
        description="Current status of the vector store record",
        example=StatusEnum.active,
    )
    config: Optional[Dict[str, Any]] = Field(
        None, description="Additional configuration details"
    )
    file_count: int = Field(
        ...,
        ge=0,
        description="Number of files associated with this vector store in the DB",
        example=10,
    )

    model_config = ConfigDict(from_attributes=True)

    # Enable ORM mode


# ---------------------------------------------------------------------
# Update schema for vector store (partial update)
# ---------------------------------------------------------------------
class VectorStoreUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=3,
        max_length=128,
        description="New name for the vector store",
    )
    # Use StatusEnum for consistency
    status: Optional[StatusEnum] = Field(
        None, description="New status for the vector store"
    )
    config: Optional[Dict[str, Any]] = Field(
        None,
        description="Updated configuration (will replace existing config)",
    )
    # Note: file_count is managed internally by adding/deleting files, not directly updatable here


# ---------------------------------------------------------------------
# File schemas
# ---------------------------------------------------------------------
class VectorStoreFileCreate(BaseModel):
    # Added file_id - Client must provide this unique ID (e.g., vsf_...)
    file_id: str = Field(
        ...,
        description="Client-generated unique ID for this file record (e.g., vsf_...).",
    )
    file_name: str = Field(
        ..., max_length=256, description="Original name of the file."
    )
    file_path: str = Field(
        ...,
        max_length=1024,
        description="Path identifier used in Qdrant metadata "
        ""
        "(e.g., 'source' field).",
    )
    # Added optional status
    status: Optional[StatusEnum] = Field(
        None,
        description="Initial status of the file (e.g., completed, queued). "
        ""
        "Defaults to 'completed' if not provided by API.",
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Optional user-defined metadata associated with the "
        ""
        "file.",
    )


class VectorStoreFileRead(BaseModel):
    id: str = Field(
        ..., description="Unique ID of the file record", example="vsf_def456"
    )
    # Added vector_store_id - Crucial context
    vector_store_id: str = Field(
        ...,
        description="ID of the vector store this file belongs to",
        example="vs_abc123",
    )
    file_name: str = Field(
        ..., description="Original name of the file", example="document.pdf"
    )
    file_path: str = Field(
        ...,
        description="Path identifier used in Qdrant metadata",
        example="s3://bucket/document.pdf",
    )
    processed_at: Optional[int] = Field(
        None,
        description="Unix timestamp when the file "
        "processing state last changed "
        "(completed/failed)",
        example=1641081600,
    )
    status: StatusEnum = Field(
        ...,
        description="Current status of the file processing",
        example=StatusEnum.completed,
    )
    error_message: Optional[str] = Field(
        None, description="Error details if the status is 'failed'"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="User-defined metadata associated with the file"
    )

    model_config = ConfigDict(from_attributes=True)


class VectorStoreFileUpdate(BaseModel):
    # Allows updating status, error message, or metadata for an existing file record
    status: Optional[StatusEnum] = Field(
        None, description="New status for the file"
    )
    error_message: Optional[str] = Field(
        None, description="Error message if status is 'failed'"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Updated metadata (will replace existing metadata)"
    )


class VectorStoreList(BaseModel):
    # Consider adding pagination fields here if listing can be large
    # e.g., limit: int, offset: int, total: int
    vector_stores: List[VectorStoreRead]


class VectorStoreFileList(BaseModel):
    # Consider adding pagination fields here
    files: List[VectorStoreFileRead]


# ---------------------------------------------------------------------
# Assistant Linking Schemas ( Kept for potential future use / alternative API design )
# ---------------------------------------------------------------------
class VectorStoreLinkAssistant(BaseModel):
    assistant_ids: List[str] = Field(
        ..., min_items=1, description="List of assistant IDs to link"
    )


class VectorStoreUnlinkAssistant(BaseModel):
    assistant_id: str = Field(..., description="Assistant ID to unlink")


# ---------------------------------------------------------------------
# Search Schemas ( Appear aligned with VectorSearchHandler output )
# ---------------------------------------------------------------------
class VectorStoreSearchResult(BaseModel):
    text: str = Field(..., description="Retrieved text chunk")
    metadata: Optional[dict] = Field(
        None,
        description="Metadata associated with the chunk "
        ""
        "(includes original file info, custom meta, "
        ""
        ""
        "and potentially score/explanation)",
    )
    score: float = Field(
        ..., description="Similarity score from the vector search"
    )
    vector_id: Optional[str] = Field(
        None,
        description="ID of the specific vector " "" "point in Qdrant",
        example="uuid-...",
    )
    store_id: Optional[str] = Field(
        None,
        description="ID of the vector store where the result "
        ""
        ""
        "was found",
        example="vs_abc123",
    )
    retrieved_at: int = Field(
        default_factory=lambda: int(time.time()),
        description="Unix timestamp when this result was retrieved",
    )


class SearchExplanation(BaseModel):
    # Structure depends on what Qdrant/search logic provides
    base_score: float
    filters_passed: Optional[List[str]] = None
    boosts_applied: Optional[Dict[str, float]] = None
    final_score: float


class EnhancedVectorSearchResult(VectorStoreSearchResult):
    explanation: Optional[SearchExplanation] = Field(
        None,
        description="Details about how the score was calculated "
        "(if requested)",
    )


# ---------------------------------------------------------------------
# Request Schema for Adding Documents to the Store ( Kept for potential future use / alternative API design )
# ---------------------------------------------------------------------


class VectorStoreAddRequest(BaseModel):
    texts: List[str] = Field(
        ..., description="List of texts to add to the vector store"
    )
    vectors: List[List[float]] = Field(
        ..., description="Vector embeddings corresponding to each text"
    )
    metadata: List[Dict[str, Any]] = Field(
        ..., description="Metadata dictionaries corresponding to each text"
    )

    # Using model_validator instead of multiple field_validators for cross-field validation
    from pydantic import model_validator

    @model_validator(mode="after")
    def check_lengths_match(self) -> "VectorStoreAddRequest":
        texts_len = len(self.texts)
        vectors_len = len(self.vectors)
        metadata_len = len(self.metadata)
        if not (texts_len == vectors_len == metadata_len):
            raise ValueError(
                f"Lengths of texts ({texts_len}), vectors ({vectors_len}), "
                f"and metadata "
                f"({metadata_len}) must all match."
            )
        return self
