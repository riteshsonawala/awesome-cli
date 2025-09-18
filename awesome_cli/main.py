"""Main entry point for the awesome-cli package when used as a library template."""

import sys
from .core import CLI


def create_cli(name: str = "my-cli", description: str = "My CLI Application", version: str = "0.1.0") -> CLI:
    """Factory function to create a CLI instance.

    Args:
        name: Name of your CLI application
        description: Description of your CLI
        version: Version of your CLI

    Returns:
        Configured CLI instance
    """
    cli = CLI(name=name, description=description, version=version)
    return cli


def main():
    """Example main function showing how to use the library."""
    cli = create_cli(
        name="awesome-cli-example",
        description="Example CLI built with awesome-cli framework",
        version="1.0.0"
    )

    # Discover commands from local directory
    cli.discover_commands("commands")

    # Run the CLI
    sys.exit(cli.run())


if __name__ == "__main__":
    main()