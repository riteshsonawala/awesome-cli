"""Example command for listing files."""

import argparse
import os
from pathlib import Path
from cli import Command


class ListFilesCommand(Command):
    """List files in a directory with various filters."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            'path',
            nargs='?',
            default='.',
            help='Directory path to list'
        )
        parser.add_argument(
            '-e', '--extension',
            help='Filter by file extension (e.g., .py, .txt)'
        )
        parser.add_argument(
            '-r', '--recursive',
            action='store_true',
            help='List files recursively'
        )
        parser.add_argument(
            '--size',
            action='store_true',
            help='Show file sizes'
        )

    def execute(self, args: argparse.Namespace) -> int:
        path = Path(args.path)

        if not path.exists():
            print(f"Error: Path '{path}' does not exist")
            return 1

        if not path.is_dir():
            print(f"Error: '{path}' is not a directory")
            return 1

        files = self._get_files(path, args.recursive, args.extension)

        for file in files:
            if args.size:
                size = file.stat().st_size
                size_str = self._format_size(size)
                print(f"{file.relative_to(path)} ({size_str})")
            else:
                print(file.relative_to(path))

        return 0

    def _get_files(self, path: Path, recursive: bool, extension: str = None):
        """Get files from directory based on filters."""
        if recursive:
            pattern = '**/*' if not extension else f'**/*{extension}'
            files = path.glob(pattern)
        else:
            pattern = '*' if not extension else f'*{extension}'
            files = path.glob(pattern)

        return [f for f in files if f.is_file()]

    def _format_size(self, size: int) -> str:
        """Format file size in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"