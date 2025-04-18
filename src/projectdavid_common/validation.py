# src/projectdavid_common/validation.py

from projectdavid_common.schemas.actions import (
    ActionBase,
    ActionCreate,
    ActionList,
    ActionRead,
    ActionStatus,
    ActionUpdate,
)
from projectdavid_common.schemas.api_key_schemas import (
    ApiKeyCreateRequest,
    ApiKeyCreateResponse,
    ApiKeyDetails,
    ApiKeyListResponse,
)
from projectdavid_common.schemas.assistants import (
    AssistantCreate,
    AssistantRead,
    AssistantUpdate,
)
from projectdavid_common.schemas.enums import ProviderEnum, StatusEnum
from projectdavid_common.schemas.files import FileResponse, FileUploadRequest
from projectdavid_common.schemas.inference import ProcessOutput
from projectdavid_common.schemas.messages import (
    MessageCreate,
    MessageRead,
    MessageRole,
    MessageUpdate,
    ToolMessageCreate,
)
from projectdavid_common.schemas.runs import (
    Run,
    RunCreate,
    RunReadDetailed,
    RunStatus,
    RunStatusUpdate,
)
from projectdavid_common.schemas.stream import StreamRequest
from projectdavid_common.schemas.threads import (
    ThreadCreate,
    ThreadIds,
    ThreadParticipant,
    ThreadRead,
    ThreadReadDetailed,
    ThreadUpdate,
)
from projectdavid_common.schemas.tools import (
    Tool,
    ToolCreate,
    ToolFunction,
    ToolList,
    ToolRead,
    ToolUpdate,
)
from projectdavid_common.schemas.users import (
    UserBase,
    UserCreate,
    UserDeleteResponse,
    UserRead,
    UserUpdate,
)
from projectdavid_common.schemas.vectors import (
    EnhancedVectorSearchResult,
    SearchExplanation,
    VectorStoreAddRequest,
    VectorStoreCreate,
    VectorStoreCreateWithSharedId,
    VectorStoreFileCreate,
    VectorStoreFileList,
    VectorStoreFileRead,
    VectorStoreFileUpdate,
    VectorStoreFileUpdateStatus,
    VectorStoreLinkAssistant,
    VectorStoreList,
    VectorStoreRead,
    VectorStoreSearchResult,
    VectorStoreUnlinkAssistant,
    VectorStoreUpdate,
)


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

    # Core Vector Store CRUD
    VectorStoreCreate = VectorStoreCreate
    VectorStoreCreateWithSharedId = VectorStoreCreateWithSharedId
    VectorStoreRead = VectorStoreRead
    VectorStoreUpdate = VectorStoreUpdate
    VectorStoreList = VectorStoreList

    # File-level operations
    VectorStoreFileCreate = VectorStoreFileCreate
    VectorStoreFileRead = VectorStoreFileRead
    VectorStoreFileUpdate = VectorStoreFileUpdate
    VectorStoreFileUpdateStatus = VectorStoreFileUpdateStatus
    VectorStoreFileList = VectorStoreFileList

    # Search & Results
    VectorStoreSearchResult = VectorStoreSearchResult
    EnhancedVectorSearchResult = EnhancedVectorSearchResult
    SearchExplanation = SearchExplanation

    # Assistant linking
    VectorStoreLinkAssistant = VectorStoreLinkAssistant
    VectorStoreUnlinkAssistant = VectorStoreUnlinkAssistant

    # Optional: Request wrapper
    VectorStoreAddRequest = VectorStoreAddRequest

    # Key
    ApiKeyCreateRequest = ApiKeyCreateRequest
    ApiKeyCreateResponse = ApiKeyCreateResponse
    ApiKeyDetails = ApiKeyDetails
    ApiKeyListResponse = ApiKeyListResponse

    # Stream
    StreamRequest = StreamRequest
