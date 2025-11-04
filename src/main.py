"""Main entry point for the application."""

import argparse
import sys
from importlib.metadata import PackageNotFoundError, version


def _get_version() -> str:
    """Get application version from package metadata."""
    try:
        return version("python-app-template")
    except PackageNotFoundError:
        return "0.0.0"


def process_text(text: str) -> str:
    """
    Process the input text.

    Args:
        text: The text to process.

    Returns:
        The processed text.
    """
    return text


def _create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="my-app",
        description="Python Application Template - A modern Python starter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {_get_version()}",
    )

    parser.add_argument(
        "--text",
        type=str,
        help="Text to process and display",
        required=False,
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for the application.

    Args:
        argv: Command-line arguments. If None, sys.argv[1:] is used.

    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    parser = _create_parser()
    args = parser.parse_args(argv)

    if args.text is not None:
        result = process_text(args.text)
        print(result)
        return 0
    else:
        parser.print_help()
        return 0  # Return 0 instead of 1 when showing help


if __name__ == "__main__":
    sys.exit(main())
