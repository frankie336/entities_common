import os
from pathlib import Path

from dotenv import load_dotenv

from entities_common.utilities.logging_service import LoggingUtility

log = LoggingUtility()


def is_inside_container() -> bool:
    return os.path.exists("/.dockerenv") or os.getenv("RUNNING_IN_DOCKER") == "1"


def load_environment() -> dict:
    base_dir = Path(__file__).resolve().parent
    env_file = base_dir / (".env.docker" if is_inside_container() else ".env.dev")

    log.info("[ENV DETECTION] Detected %s environment. Loading: %s",
             "container" if is_inside_container() else "host",
             env_file)

    if not env_file.is_file():
        log.critical("Missing environment file: %s", env_file)
        raise RuntimeError(f"Missing environment file: {env_file}")

    load_dotenv(dotenv_path=env_file, override=True)

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        log.critical("DATABASE_URL missing in env! Check your .env file: %s", env_file)
        raise RuntimeError("DATABASE_URL must be defined in the environment file.")

    if not is_inside_container() and "localhost:3306" in db_url:
        patched = db_url.replace("localhost:3306", "localhost:3307")
        os.environ["DATABASE_URL"] = patched
        log.info("[PATCH] Adjusted host DATABASE_URL: %s", patched)

    return dict(os.environ)
