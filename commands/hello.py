"""Example command module demonstrating the command structure."""

import argparse
from cli import Command


class HelloCommand(Command):
    """Say hello to someone."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            'name',
            nargs='?',
            default='World',
            help='Name to greet'
        )
        parser.add_argument(
            '-c', '--count',
            type=int,
            default=1,
            help='Number of times to greet'
        )
        parser.add_argument(
            '--uppercase',
            action='store_true',
            help='Output in uppercase'
        )

    def execute(self, args: argparse.Namespace) -> int:
        greeting = f"Hello, {args.name}!"

        if args.uppercase:
            greeting = greeting.upper()

        for _ in range(args.count):
            print(greeting)

        return 0

    def validate(self, args: argparse.Namespace) -> bool:
        if args.count < 1:
            print("Count must be at least 1")
            return False
        if args.count > 100:
            print("Count cannot exceed 100")
            return False
        return True