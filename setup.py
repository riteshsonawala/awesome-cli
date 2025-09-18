"""Setup configuration for awesome-cli package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="awesome-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An extensible CLI framework for building modular command-line applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/awesome-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "build>=0.7",
            "twine>=4.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "awesome-cli-example=awesome_cli.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/awesome-cli/issues",
        "Source": "https://github.com/yourusername/awesome-cli",
    },
)