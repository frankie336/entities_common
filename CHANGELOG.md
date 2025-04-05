# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.10] - 2025-04-05

### Added

- `entities_common.utilities.load_environment` module:
  - `is_inside_container()` – Detects Docker container execution.
  - `get_env_file()` – Picks `.env.dev` or `.env.docker` based on context.
  - `load_environment()` – Loads environment variables from the right file, with host/container overrides.

- GitHub Actions: `publish.yml` now builds and publishes to Test PyPI on version tag push (`v*.*.*`).
- Added support for Pydantic v2 across all schema modules:
  - Migrated all `@validator` usages to `@field_validator` or `@model_validator`.
  - Replaced deprecated `min_items`, `example`, and legacy keyword usage.

### Changed

- Enforced formatting with `black` (line length = 100).
- CI now includes `flake8` for PEP8 linting (`max-line-length = 79`).
- All schema classes now use `ConfigDict` instead of legacy `Config`.

### Fixed

- `twine` not being found in GitHub Actions `Check built files` step — resolved by installing `twine` explicitly.
- 403 Forbidden error on Test PyPI uploads — resolved by properly storing `TEST_PYPI_TOKEN` in GitHub secrets.
