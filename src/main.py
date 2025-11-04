"""Main entry point for the application."""

import argparse
import sys

__version__ = "0.1.0"


def process_text(text: str) -> str:
    """
    Process the input text.

    Args:
        text: The text to process.

    Returns:
        The processed text.
    """
    return text


def create_parser() -> argparse.ArgumentParser:
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
        version=f"%(prog)s {__version__}",
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
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.text is not None:
        result = process_text(args.text)
        print(result)
        return 0
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
