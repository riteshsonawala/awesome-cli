"""Calculator command for the example project."""

import argparse
from awesome_cli import Command


class CalculateCommand(Command):
    """Perform basic arithmetic operations."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            'operation',
            choices=['add', 'subtract', 'multiply', 'divide'],
            help='Operation to perform'
        )
        parser.add_argument(
            'x',
            type=float,
            help='First number'
        )
        parser.add_argument(
            'y',
            type=float,
            help='Second number'
        )
        parser.add_argument(
            '--precision',
            type=int,
            default=2,
            help='Decimal precision for result (default: 2)'
        )

    def execute(self, args: argparse.Namespace) -> int:
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else None,
        }

        result = operations[args.operation](args.x, args.y)

        if result is None:
            print("Error: Division by zero")
            return 1

        if isinstance(result, float):
            result = round(result, args.precision)

        print(f"Result: {result}")
        return 0

    def validate(self, args: argparse.Namespace) -> bool:
        if args.operation == 'divide' and args.y == 0:
            print("Error: Cannot divide by zero")
            return False
        if args.precision < 0:
            print("Error: Precision must be non-negative")
            return False
        return True