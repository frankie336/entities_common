## [0.1.12](https://github.com/frankie336/entities_common/compare/v0.1.11...v0.1.12) (2025-04-06)


### Bug Fixes

* workflow2 ([0285db9](https://github.com/frankie336/entities_common/commit/0285db9f315235578d911f35a4cd5019a86ec560))

## [0.1.11](https://github.com/frankie336/entities_common/compare/v0.1.10...v0.1.11) (2025-04-06)


### Bug Fixes

* dependency ([b48dac5](https://github.com/frankie336/entities_common/commit/b48dac5a3f432d6d869cb6a160ca616ddb8e4ca2))
* dependency 2 ([8407f0b](https://github.com/frankie336/entities_common/commit/8407f0b58dd0e4607652bee59c70a7f6032a6549))
* requirements-dev.txt ([2f1299b](https://github.com/frankie336/entities_common/commit/2f1299bf4bc9699782ba012a93b342292c3058d9))
* test ([abe4e39](https://github.com/frankie336/entities_common/commit/abe4e396fb42439a528bc82f6c337dfe31234cb1))
* test_tag_release.yml ([0620759](https://github.com/frankie336/entities_common/commit/06207599e89d6edc902d2bcae9bf225345066e2e))
* vectors.py ([73054e3](https://github.com/frankie336/entities_common/commit/73054e3d6d4328c6c7a958c99a64ab4eee8ade9c))
* workflow ([4b5a6e4](https://github.com/frankie336/entities_common/commit/4b5a6e41f7bb5311a33ba7ac6b51feb4e0435ed6))

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
