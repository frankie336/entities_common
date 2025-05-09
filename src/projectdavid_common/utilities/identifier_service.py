import random
import string


class IdentifierService:
    @staticmethod
    def generate_id(prefix: str, length: int = 22) -> str:
        """Generate a prefixed ID with a specified length of random
        alphanumeric characters."""
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choice(characters) for _ in range(length))
        return f"{prefix}_{random_string}"

    @staticmethod
    def generate_thread_id() -> str:
        """Generate a thread ID."""
        return IdentifierService.generate_id("thread")

    @staticmethod
    def generate_user_id() -> str:
        """Generate a user ID."""
        return IdentifierService.generate_id("user")

    @staticmethod
    def generate_message_id() -> str:
        """Generate a message ID."""
        return IdentifierService.generate_id("message")

    @staticmethod
    def generate_project_id() -> str:
        """Generate a project ID."""
        return IdentifierService.generate_id("project")

    @staticmethod
    def generate_task_id() -> str:
        """Generate a task ID."""
        return IdentifierService.generate_id("task")

    @staticmethod
    def generate_custom_id(prefix: str) -> str:
        """Generate a custom ID with a given prefix."""
        return IdentifierService.generate_id(prefix)

    @staticmethod
    def generate_assistant_id() -> str:
        """Generate an assistant ID in the specified format."""
        return IdentifierService.generate_id("asst")

    @staticmethod
    def generate_tool_id() -> str:
        """Generate an assistant ID in the specified format."""
        return IdentifierService.generate_id("tool")

    @staticmethod
    def generate_action_id() -> str:
        """Generate an assistant ID in the specified format."""
        return IdentifierService.generate_id("act")

    @staticmethod
    def generate_run_id() -> str:
        """Generate an assistant ID in the specified format."""
        return IdentifierService.generate_id("run")

    @staticmethod
    def generate_sandbox_id() -> str:
        return IdentifierService.generate_id("cli")

    @staticmethod
    def generate_vector_id() -> str:
        """Generate valid UUID4 string for Qdrant compatibility"""
        return IdentifierService.generate_id("vect")

    @staticmethod
    def generate_file_id() -> str:
        """Generate valid UUID4 string for Qdrant compatibility"""
        return IdentifierService.generate_id("file")

    @staticmethod
    def generate_key_id() -> str:
        """Generate valid UUID4 string for Qdrant compatibility"""
        return IdentifierService.generate_id("key")

    @staticmethod
    def generate_prefixed_id(prefix) -> str:
        """Generate valid UUID4 string for Qdrant compatibility"""
        return IdentifierService.generate_id(prefix)


if __name__ == "__main__":
    identity = IdentifierService()
    print(identity.generate_prefixed_id(prefix='plt_ast'))
