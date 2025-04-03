import os

from dotenv import load_dotenv, dotenv_values

from entities_common.utilities.logging_service import LoggingUtility

logging_utility = LoggingUtility()

def is_inside_container() -> bool:
    """Detect if the process is running inside a Docker container."""
    return os.path.exists("/.dockerenv") or os.getenv("RUNNING_IN_DOCKER") == "1"


def get_env_file() -> str:
    """Select the appropriate .env file based on environment."""
    return ".env.docker" if is_inside_container() else ".env.dev"


def load_environment() -> dict:
    """
    Load environment variables from the appropriate file and apply local patches.
    Returns the final env dict after patching.
    """
    env_file = get_env_file()
    logging_utility.info(
        "[ENV DETECTION] Detected %s environment. Loading: %s",
        "container" if is_inside_container() else "host",
        env_file
    )

    raw_env = dotenv_values(env_file)
    load_dotenv(dotenv_path=env_file, override=True)

    # Debug only: print loaded dotenv values
    logging_utility.debug(">>> dotenv values: %s", raw_env)

    # Patch DATABASE_URL for host port override
    patched = False
    db_url = os.getenv("DATABASE_URL")
    if not is_inside_container() and db_url and "localhost:3306" in db_url:
        db_url = db_url.replace("localhost:3306", "localhost:3307")
        os.environ["DATABASE_URL"] = db_url
        logging_utility.info("[PATCH] Adjusted host DATABASE_URL for local port mapping: %s", db_url)
        patched = True

    if not db_url:
        logging_utility.critical("DATABASE_URL missing in env! Check your .env file: %s", env_file)
        raise RuntimeError("DATABASE_URL must be defined in the environment file.")

    if patched:
        raw_env["DATABASE_URL"] = db_url

    return raw_env
