# src/entities_common/validation.py
# Use relative imports for modules within your package.

from entities_common.schemas.actions import (
    ActionBase, ActionStatus, ActionCreate, ActionRead, ActionList, ActionUpdate
)
from entities_common.schemas.assistants import (
    AssistantCreate, AssistantRead, AssistantUpdate
)
from entities_common.schemas.enums import ProviderEnum, StatusEnum
from entities_common.schemas.files import FileUploadRequest, FileResponse
from entities_common.schemas.inference import ProcessOutput, StreamRequest
from entities_common.schemas.messages import (
    MessageRole, MessageCreate, MessageRead, MessageUpdate, ToolMessageCreate
)
from entities_common.schemas.runs import (
    Run, RunCreate, RunReadDetailed, RunStatus, RunStatusUpdate
)
from entities_common.schemas.threads import (
    ThreadCreate, ThreadRead, ThreadUpdate, ThreadParticipant, ThreadReadDetailed, ThreadIds
)
from entities_common.schemas.tools import (
    ToolFunction, Tool, ToolCreate, ToolRead, ToolUpdate, ToolList
)
from entities_common.schemas.users import (
    UserBase, UserCreate, UserRead, UserUpdate, UserDeleteResponse
)
from entities_common.schemas.vectors import (
    VectorStoreCreate, VectorStoreRead, VectorStoreUpdate, VectorStoreList,
    EnhancedVectorSearchResult, SearchExplanation, VectorStoreSearchResult, VectorStoreAddRequest, VectorStoreFileRead
)

from entities_common.schemas.keys import APIKeyRead, APIKeyCreate

class ValidationInterface:
    """
    Exposes Pydantic validation classes, retaining their original naming.

    This interface allows consumers to access the various schemas like:
        - ValidationInterface.FileUploadRequest
        - ValidationInterface.ActionCreate
        - etc.
    """

    # Actions schemas
    ActionBase = ActionBase
    ActionStatus = ActionStatus
    ActionCreate = ActionCreate
    ActionRead = ActionRead
    ActionList = ActionList
    ActionUpdate = ActionUpdate

    # Assistants schemas
    AssistantCreate = AssistantCreate
    AssistantRead = AssistantRead
    AssistantUpdate = AssistantUpdate
    VectorStoreRead = VectorStoreRead

    # Enum schemas
    ProviderEnum = ProviderEnum
    StatusEnum = StatusEnum

    # Files schemas
    FileUploadRequest = FileUploadRequest
    FileResponse = FileResponse

    # Inference schemas
    ProcessOutput = ProcessOutput
    StreamRequest = StreamRequest

    # Messages schemas
    MessageRole = MessageRole
    MessageCreate = MessageCreate
    MessageRead = MessageRead
    MessageUpdate = MessageUpdate
    ToolMessageCreate = ToolMessageCreate

    # Runs schemas
    Run = Run
    RunCreate = RunCreate
    RunReadDetailed = RunReadDetailed
    RunStatus = RunStatus
    RunStatusUpdate = RunStatusUpdate

    # Threads schemas
    ThreadCreate = ThreadCreate
    ThreadRead = ThreadRead
    ThreadUpdate = ThreadUpdate
    ThreadParticipant = ThreadParticipant
    ThreadReadDetailed = ThreadReadDetailed
    ThreadIds = ThreadIds

    # Tools schemas
    ToolFunction = ToolFunction
    Tool = Tool
    ToolCreate = ToolCreate
    ToolRead = ToolRead
    ToolUpdate = ToolUpdate
    ToolList = ToolList

    # Users schemas
    UserBase = UserBase
    UserCreate = UserCreate
    UserRead = UserRead
    UserUpdate = UserUpdate
    UserDeleteResponse = UserDeleteResponse

    # Vector Store schemas
    VectorStoreCreate  = VectorStoreCreate
    VectorStoreRead  = VectorStoreRead
    VectorStoreFileRead = VectorStoreFileRead
    VectorStoreUpdate = VectorStoreUpdate
    VectorStoreList = VectorStoreList
    EnhancedVectorSearchResult = EnhancedVectorSearchResult
    SearchExplanation = SearchExplanation
    VectorStoreSearchResult = VectorStoreSearchResult
    VectorStoreAddRequest = VectorStoreAddRequest

    # Key
    APIKeyRead = APIKeyRead
    APIKeyCreate = APIKeyCreate
