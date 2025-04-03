# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0-alpha] - 2025-04-03

### New

- Environment detection and loading utilities added under `entities_common.utilities.load_environment`.
  Includes:
  - `is_inside_container()` – detects whether running inside a Docker container.
  - `get_env_file()` – chooses `.env.docker` or `.env.dev` based on context.
  - `load_environment()` – loads and patches environment variables with support for Docker vs host overrides.
