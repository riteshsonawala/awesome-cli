"""Core CLI framework components."""

import argparse
import importlib
import importlib.util
import inspect
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Type


class Command(ABC):
    """Base class for all CLI commands."""

    def __init__(self):
        self.name: str = self.__class__.__name__.lower().replace('command', '')
        self.description: str = self.__doc__ or "No description provided"

    @abstractmethod
    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add command-specific arguments to the parser."""
        pass

    @abstractmethod
    def execute(self, args: argparse.Namespace) -> int:
        """Execute the command with given arguments.

        Returns:
            Exit code (0 for success, non-zero for failure)
        """
        pass

    def validate(self, args: argparse.Namespace) -> bool:
        """Validate arguments before execution.

        Returns:
            True if arguments are valid, False otherwise
        """
        return True


class CLI:
    """Main CLI application that manages and executes commands."""

    def __init__(self, name: str = "cli", description: str = "CLI Application", version: str = "0.1.0"):
        self.name = name
        self.description = description
        self.version = version
        self.commands: Dict[str, Command] = {}
        self.parser = argparse.ArgumentParser(
            prog=name,
            description=description,
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        self.parser.add_argument(
            '--version', '-v',
            action='version',
            version=f'{name} {version}'
        )
        self.subparsers = self.parser.add_subparsers(
            dest='command',
            help='Available commands',
            metavar='COMMAND'
        )

    def register_command(self, command: Command) -> None:
        """Register a command with the CLI."""
        if command.name in self.commands:
            raise ValueError(f"Command '{command.name}' is already registered")

        self.commands[command.name] = command

        # Create subparser for this command
        subparser = self.subparsers.add_parser(
            command.name,
            help=command.description,
            description=command.description
        )

        # Let command add its own arguments
        command.add_arguments(subparser)

    def register_command_class(self, command_class: Type[Command]) -> None:
        """Register a command class with the CLI."""
        if not issubclass(command_class, Command):
            raise TypeError(f"{command_class} must be a subclass of Command")

        command_instance = command_class()
        self.register_command(command_instance)

    def discover_commands(self, directory: str = "commands") -> None:
        """Automatically discover and load commands from a directory.

        Args:
            directory: Directory path containing command modules
        """
        commands_dir = Path(directory)
        if not commands_dir.exists():
            return

        # Add commands directory to Python path if needed
        parent_dir = str(commands_dir.parent)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)

        for file_path in commands_dir.glob("*.py"):
            if file_path.name.startswith("_"):
                continue

            module_name = f"{directory.replace('/', '.')}.{file_path.stem}"

            try:
                # Try to import module
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)

                    # Find all Command subclasses in the module
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and
                            issubclass(obj, Command) and
                            obj != Command and
                            not inspect.isabstract(obj)):

                            self.register_command_class(obj)

            except Exception as e:
                print(f"Failed to load module {module_name}: {e}", file=sys.stderr)

    def discover_commands_from_module(self, module_name: str) -> None:
        """Discover commands from an installed Python module.

        Args:
            module_name: Name of the module containing commands
        """
        try:
            module = importlib.import_module(module_name)

            # Find all Command subclasses in the module
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and
                    issubclass(obj, Command) and
                    obj != Command and
                    not inspect.isabstract(obj)):

                    self.register_command_class(obj)

        except ImportError as e:
            print(f"Failed to import module {module_name}: {e}", file=sys.stderr)

    def run(self, argv: Optional[List[str]] = None) -> int:
        """Run the CLI with given arguments.

        Args:
            argv: Command line arguments (defaults to sys.argv[1:])

        Returns:
            Exit code
        """
        args = self.parser.parse_args(argv)

        if not args.command:
            self.parser.print_help()
            return 0

        if args.command not in self.commands:
            print(f"Unknown command: {args.command}", file=sys.stderr)
            return 1

        command = self.commands[args.command]

        # Validate arguments
        if not command.validate(args):
            return 1

        # Execute command
        try:
            return command.execute(args)
        except KeyboardInterrupt:
            print("\nOperation cancelled by user", file=sys.stderr)
            return 130
        except Exception as e:
            print(f"Error executing command '{args.command}': {e}", file=sys.stderr)
            return 1