# Example Project Using awesome-cli

This example demonstrates how to use the `awesome-cli` library to build your own CLI application.

## Installation

First, install the awesome-cli library from the parent directory:

```bash
# From the example_project directory
pip install -e ../
```

Or if awesome-cli is published to PyPI:

```bash
pip install awesome-cli
```

## Running the Example

```bash
# Make executable
chmod +x my_cli.py

# Show help
./my_cli.py --help

# Show version
./my_cli.py --version

# Run commands
./my_cli.py greet John
./my_cli.py greet "Jane Doe" --formal
./my_cli.py calculate add 10 20
./my_cli.py calculate divide 100 3 --precision 4
```

## Project Structure

```
example_project/
├── my_cli.py           # Main CLI entry point
├── my_commands/        # Your custom commands
│   ├── __init__.py
│   ├── greet.py       # Greeting command
│   └── calculate.py   # Calculator command
└── README.md
```

## Adding New Commands

1. Create a new Python file in `my_commands/`
2. Import the `Command` class from `awesome_cli`
3. Create a class that inherits from `Command`
4. Implement `add_arguments()` and `execute()` methods
5. The command is automatically discovered when you run the CLI

Example template:

```python
from awesome_cli import Command
import argparse

class MyNewCommand(Command):
    """Description of your command."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('--option', help='An option')

    def execute(self, args: argparse.Namespace) -> int:
        # Your logic here
        print(f"Running with: {args.option}")
        return 0
```