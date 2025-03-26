# src/entities_common/validation.py
# Use relative imports for modules within your package.

from dotenv import load_dotenv

# Relative imports from your package's schemas and services.
from .schemas.actions import (
    ActionBase, ActionStatus, ActionCreate, ActionRead, ActionList, ActionUpdate
)
from .schemas.assistants import (
    AssistantCreate, AssistantRead, AssistantUpdate, VectorStoreRead
)
from .schemas.enums import ProviderEnum, StatusEnum
from .schemas.files import FileUploadRequest, FileResponse
from .schemas.inference import ProcessOutput, StreamRequest
from .schemas.messages import (
    MessageRole, MessageCreate, MessageRead, MessageUpdate, ToolMessageCreate
)
from .schemas.runs import (
    Run, RunCreate, RunReadDetailed, RunStatus, RunStatusUpdate
)
from .schemas.threads import (
    ThreadCreate, ThreadRead, ThreadUpdate, ThreadParticipant, ThreadReadDetailed, ThreadIds
)
from .schemas.tools import (
    ToolFunction, Tool, ToolCreate, ToolRead, ToolUpdate, ToolList
)
from .schemas.users import (
    UserBase, UserCreate, UserRead, UserUpdate, UserDeleteResponse
)
from .services.logging_service import LoggingUtility

# Load environment variables from .env file.
load_dotenv()

# Initialize logging utility.
logging_utility = LoggingUtility()


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
