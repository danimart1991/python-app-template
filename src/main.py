"""Main entry point for the application."""

import argparse
import logging
import sys
from importlib.metadata import PackageNotFoundError, version

from src import settings


def _get_version() -> str:
    """Get application version from package metadata."""
    try:
        return version("domoticarte-youtube-manager")
    except PackageNotFoundError:
        return "0.0.0"


def _setup_logging(verbose: int) -> None:
    """Config the logging system based on verbosity level.

    Args:
        verbose: Verbosity level (number of -v flags).
    """

    level = max(10, settings.LOGGING_DEFAULT_LEVEL - (verbose * 10))
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def _process_text(text: str | None) -> str:
    """
    Process the input text.

    Args:
        text: The text to process. If None or empty, a default message is used.

    Returns:
        The processed text.
    """
    logging.info("Processing text: %s", text)

    if not text:
        logging.warning("No text provided to process.")
        text = "No text provided."
    return text


def _create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="domoticarte-youtube-manager",
        description="YouTube metadata manager using YAML files and automation via GitHub Actions.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        allow_abbrev=True,
        add_help=False,  # Disable automatic -h/--help to add it manually
    )

    # Verbose flag (independent, can be combined with any action)
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="Increase verbosity level (can be used multiple times)",
    )

    action_group = parser.add_mutually_exclusive_group(required=False)

    action_group.add_argument(
        "--text",
        type=str,
        help="Text to process and display",
    )

    action_group.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {_get_version()}",
        help="Show program's version number and exit",
    )

    action_group.add_argument(
        "--help",
        "-h",
        action="help",
        help="Show this help message and exit",
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

    _setup_logging(args.verbose)

    result = _process_text(args.text)
    print(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())
