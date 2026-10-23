"""
Launch an Xmascript file as a terminal UCI engine.

Requires Python 3.14 and the original Xmascript interpreter.
"""

from __future__ import annotations

from argparse import ArgumentParser, Namespace
from contextlib import suppress
from json import loads as json_loads
from pathlib import Path
from sys import setrecursionlimit, stdout
from typing import Any


def launch(notebook_path: Path, program_path: Path, recursion_limit: int) -> None:
    setrecursionlimit(recursion_limit)
    stdout.reconfigure(line_buffering=True, write_through=True)
    notebook: dict[str, Any] = json_loads(notebook_path.read_text(encoding='utf-8'))
    namespace: dict[str, Any] = {'__name__': '__main__'}
    for cell in notebook['cells']:
        if cell.get('cell_type') != 'code':
            continue
        source: str = ''.join(cell.get('source', []))
        if 'interpreter.run(' not in source:
            exec(  # noqa: S102
                compile(source, str(notebook_path), 'exec'),
                namespace,
                namespace,
            )
    interpreter: Any = namespace['interpreter']
    interpreter.run(str(program_path))


def main() -> None:
    parser: ArgumentParser = ArgumentParser(
        description='Run XmascriptChess via the Xmascript interpreter',
    )
    parser.add_argument(
        'notebook',
        type=Path,
        help='Path to the original xmascript.ipynb',
    )
    parser.add_argument(
        '--program',
        type=Path,
        default=(Path(__file__).parent / 'src' / 'main.xmascript'),
        help='Entry point (default: src/main.xmascript)',
    )
    parser.add_argument(
        '--recursion-limit',
        type=int,
        default=50_000,
        help='Python recursion limit (default: 50000)',
    )
    args: Namespace = parser.parse_args()
    launch(args.notebook.resolve(), args.program.resolve(), args.recursion_limit)


if __name__ == '__main__':
    with suppress(EOFError):
        main()
