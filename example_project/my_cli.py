#!/usr/bin/env python3
"""Example CLI application using awesome-cli framework."""

import sys
from awesome_cli import CLI


def main():
    # Create your CLI application
    cli = CLI(
        name="my-app",
        description="My awesome CLI application",
        version="1.0.0"
    )

    # Discover commands from local directory
    cli.discover_commands("my_commands")

    # Run the CLI
    sys.exit(cli.run())


if __name__ == "__main__":
    main()