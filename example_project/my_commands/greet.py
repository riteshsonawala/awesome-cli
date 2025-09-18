"""Custom greeting command for the example project."""

import argparse
from datetime import datetime
from awesome_cli import Command


class GreetCommand(Command):
    """Greet someone with the current time."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            'name',
            help='Name of person to greet'
        )
        parser.add_argument(
            '--formal',
            action='store_true',
            help='Use formal greeting'
        )

    def execute(self, args: argparse.Namespace) -> int:
        current_time = datetime.now().strftime("%H:%M")

        if args.formal:
            greeting = f"Good day, {args.name}. The time is {current_time}."
        else:
            greeting = f"Hey {args.name}! It's {current_time}."

        print(greeting)
        return 0