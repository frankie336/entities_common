# [0.2.0](https://github.com/frankie336/entities_common/compare/v0.1.16...v0.2.0) (2025-04-10)


### Features

* Add support for all google models. ([0eff4d3](https://github.com/frankie336/entities_common/commit/0eff4d356acb834e36e3459b02ed6c165beae0ae))
* add support for websockets ([3a52965](https://github.com/frankie336/entities_common/commit/3a529653173ad6e5512e5b0d8c73b51dbfb19486))

## [0.1.16](https://github.com/frankie336/entities_common/compare/v0.1.15...v0.1.16) (2025-04-08)


### Bug Fixes

* fastapi dependency ([dfb77c1](https://github.com/frankie336/entities_common/commit/dfb77c172b593ed9d931b7ab4de6b4ac57ecb066))
* formatting ([9947ab2](https://github.com/frankie336/entities_common/commit/9947ab2c544a6c8e8e1753df028e45aed2b57426))
* formatting ([1e45d1f](https://github.com/frankie336/entities_common/commit/1e45d1fa0df2ac846a4cbbb57b140a92c4be940e))
* imports ([ed69c32](https://github.com/frankie336/entities_common/commit/ed69c32167f1864bc9c8e5d53e995eaeea3c6be2))
* install black ([998f911](https://github.com/frankie336/entities_common/commit/998f91149c4e820a3a242b77023637944a6bd8ec))
* name migration ([71e3a28](https://github.com/frankie336/entities_common/commit/71e3a288089b3ad25406f9d21957b7c0adedfd2c))
* TEST_PYPI_URL ([c705014](https://github.com/frankie336/entities_common/commit/c705014fe94d64ea9522a301cc9f54bd96308783))
* TEST_PYPI_URL2 ([1dd07dc](https://github.com/frankie336/entities_common/commit/1dd07dcd0da8c839adcec50431e548d1a6412270))
* workflow ([2267aee](https://github.com/frankie336/entities_common/commit/2267aeed89a7646943966c134be21a7913b08199))

## [0.1.15](https://github.com/frankie336/entities_common/compare/v0.1.14...v0.1.15) (2025-04-08)


### Bug Fixes

* Imports order ([075742d](https://github.com/frankie336/entities_common/commit/075742d51e75ddb8d86ae79e0f9b11eb6cf4c1f8))

## [0.1.14](https://github.com/frankie336/entities_common/compare/v0.1.13...v0.1.14) (2025-04-07)


### Bug Fixes

* schemas.vectors ([53bfb45](https://github.com/frankie336/entities_common/commit/53bfb4569876add37f56d83de6c4604bde1dfbd9))

## [0.1.13](https://github.com/frankie336/entities_common/compare/v0.1.12...v0.1.13) (2025-04-07)


### Bug Fixes

* vector_file meta_data issue ([dc958bd](https://github.com/frankie336/entities_common/commit/dc958bd940a034bc53517e24f2399086671819e3))

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
