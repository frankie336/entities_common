from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="entities_common",
    version="0.1.0",
    author="Francis N.",
    author_email="francis.neequaye@projectdavid.co.uk",
    description="Common shared custom packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frankie336/entities_common",
    package_dir={"": "src"},  # Tells setuptools that packages live under src/
    packages=find_packages(where="src", include=["entities_common", "entities_common.*"]),

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "anyio",
        "certifi",
        "h11",
        "httpcore",
        "httpx",
        "idna",
        "sniffio",
        "fastapi",
        "databases",
        "uvicorn",
        "sqlalchemy",
        "pydantic~=1.10.13",  # Enforcing Pydantic v1
        "starlette",
        "asgiref",
        "click",
        "pymysql",
        "cryptography",
        "typing_extensions",
        "python-dotenv",
    ],
    extras_require={
        "dev": ["pytest"],
    },
    entry_points={
        "console_scripts": [
            "entities_common-api=src.entities_common.main:main",
        ],
    },
)
