# Awesome CLI - Extensible Command Framework

A Python-based extensible CLI framework that allows easy addition of self-contained commands following a standard structure.

## Features

- Plugin-based architecture
- Automatic command discovery
- Standard command structure using ABC (Abstract Base Classes)
- Built-in argument parsing with argparse
- Command validation support
- No external dependencies (pure Python)

## Quick Start

```bash
# Make the CLI executable
chmod +x cli.py

# Run the CLI
./cli.py --help

# Run a specific command
./cli.py hello John
./cli.py list-files -r --extension .py
```

## Adding New Commands

Create a new Python file in the `commands/` directory:

```python
# commands/mycommand.py
import argparse
from cli import Command

class MyCommand(Command):
    """Description of your command."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        # Add your command-specific arguments
        parser.add_argument('--option', help='An option')

    def execute(self, args: argparse.Namespace) -> int:
        # Your command logic here
        print(f"Executing with option: {args.option}")
        return 0  # Return 0 for success, non-zero for failure

    def validate(self, args: argparse.Namespace) -> bool:
        # Optional: Validate arguments before execution
        return True
```

The command will be automatically discovered and registered when you run the CLI.

## Command Structure

Every command must:

1. Inherit from the `Command` base class
2. Implement `add_arguments()` to define command arguments
3. Implement `execute()` to define command logic
4. Optionally override `validate()` for argument validation

## Using Third-Party Libraries

While the core framework uses no external dependencies, you can use any third-party libraries in your commands:

### Option 1: Pure Python (Current Implementation)
- No dependencies needed
- Works out of the box
- Simple and lightweight

### Option 2: With Click (Alternative)
If you prefer Click's decorators:
```bash
pip install click
```

### Option 3: With Typer (Alternative)
For type hints-based CLI:
```bash
pip install typer
```

## Project Structure

```
awesome-cli/
├── cli.py              # Main CLI framework
├── commands/           # Command modules directory
│   ├── __init__.py
│   ├── hello.py       # Example: Hello command
│   └── list_files.py  # Example: List files command
└── README.md
```

## Benefits of This Architecture

1. **Modularity**: Each command is self-contained
2. **Extensibility**: Add new commands without modifying core code
3. **Discoverability**: Commands are automatically discovered
4. **Testability**: Each command can be tested independently
5. **No Lock-in**: Start simple, add dependencies as needed