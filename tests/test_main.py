"""Unit tests for the main module."""

import logging

import pytest

from src import main


class TestProcessText:
    """Test cases for the process_text function."""

    @pytest.mark.unit
    def test_process_text_returns_input(self, sample_text: str) -> None:
        """Test that process_text returns the input text unchanged."""
        result = main._process_text(sample_text)
        assert result == sample_text

    @pytest.mark.unit
    def test_process_text_with_empty_string(self) -> None:
        """Test process_text with an empty string returns default text."""
        result = main._process_text("")
        assert result == "No text provided."

    @pytest.mark.unit
    def test_process_text_with_none(self, caplog: pytest.LogCaptureFixture) -> None:
        """Test process_text with None returns default text and logs warning."""
        result = main._process_text(None)
        assert result == "No text provided."
        assert "No text provided to process" in caplog.text

    @pytest.mark.unit
    def test_process_text_with_special_characters(self) -> None:
        """Test process_text with special characters."""
        text = "Hello! @#$ %^& *() World"
        result = main._process_text(text)
        assert result == text


class TestCreateParser:
    """Test cases for the _create_parser function."""

    @pytest.mark.unit
    def test_create_parser_returns_parser(self) -> None:
        """Test that _create_parser returns an ArgumentParser."""
        parser = main._create_parser()
        assert parser is not None
        assert parser.prog == "domoticarte-youtube-manager"

    @pytest.mark.unit
    def test_parser_accepts_text_argument(self) -> None:
        """Test that the parser accepts --text argument."""
        parser = main._create_parser()
        args = parser.parse_args(["--text", "test"])
        assert args.text == "test"

    @pytest.mark.unit
    def test_parser_allows_no_arguments(self) -> None:
        """Test that the parser allows no arguments (action group is optional)."""
        parser = main._create_parser()
        args = parser.parse_args([])
        assert args.text is None

    @pytest.mark.unit
    def test_parser_text_and_version_mutually_exclusive(self) -> None:
        """Test that --text and --version are mutually exclusive."""
        parser = main._create_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--text", "test", "--version"])
        assert exc_info.value.code == 2

    @pytest.mark.unit
    def test_parser_text_and_help_mutually_exclusive(self) -> None:
        """Test that --text and --help are mutually exclusive."""
        parser = main._create_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--text", "test", "--help"])
        assert exc_info.value.code == 2  # Mutual exclusion error exits with 2

    @pytest.mark.unit
    def test_parser_accepts_help_argument(self) -> None:
        """Test that the parser accepts --help argument."""
        parser = main._create_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--help"])
        assert exc_info.value.code == 0


class TestMain:
    """Test cases for the main function."""

    @pytest.mark.unit
    def test_main_with_text_returns_success(
        self, sample_text: str, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test main function with --text argument returns 0."""
        exit_code = main.main(["--text", sample_text])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert sample_text in captured.out

    @pytest.mark.unit
    def test_main_without_text_uses_default(
        self, capsys: pytest.CaptureFixture[str], caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test main function without text (None or empty) uses default and logs warning."""
        # Test with no arguments (text=None)
        exit_code = main.main([])
        assert exit_code == 0
        captured = capsys.readouterr()
        assert "No text provided." in captured.out
        assert "No text provided to process" in caplog.text

        # Clear captured output and logs
        capsys.readouterr()
        caplog.clear()

        # Test with empty string
        exit_code = main.main(["--text", ""])
        assert exit_code == 0
        captured = capsys.readouterr()
        assert "No text provided." in captured.out
        assert "No text provided to process" in caplog.text

    @pytest.mark.unit
    def test_main_with_version_flag(self) -> None:
        """Test main function with --version flag."""
        with pytest.raises(SystemExit) as exc_info:
            main.main(["--version"])

        assert exc_info.value.code == 0


class TestSetupLogging:
    """Test cases for the _setup_logging function."""

    @pytest.mark.unit
    def test_setup_logging_default_level(self) -> None:
        """Test that default logging level is WARNING (30)."""
        # Reset root logger
        logging.root.handlers = []
        main._setup_logging(verbose=0)
        logger = logging.getLogger()
        assert logger.level == logging.WARNING

    @pytest.mark.unit
    def test_setup_logging_verbose_once(self) -> None:
        """Test that -v sets logging level to INFO (20)."""
        # Reset root logger
        logging.root.handlers = []
        main._setup_logging(verbose=1)
        logger = logging.getLogger()
        assert logger.level == logging.INFO

    @pytest.mark.unit
    def test_setup_logging_verbose_twice(self) -> None:
        """Test that -vv sets logging level to DEBUG (10)."""
        # Reset root logger
        logging.root.handlers = []
        main._setup_logging(verbose=2)
        logger = logging.getLogger()
        assert logger.level == logging.DEBUG

    @pytest.mark.unit
    def test_setup_logging_verbose_max(self) -> None:
        """Test that excessive verbosity doesn't go below DEBUG (10)."""
        # Reset root logger
        logging.root.handlers = []
        main._setup_logging(verbose=5)
        logger = logging.getLogger()
        assert logger.level == logging.DEBUG


class TestMainWithVerbosity:
    """Test cases for main function with verbosity flags."""

    @pytest.mark.unit
    def test_main_with_verbose_flag_info_level(self, caplog: pytest.LogCaptureFixture) -> None:
        """Test main function with -v flag enables INFO logging."""
        with caplog.at_level(logging.INFO):
            exit_code = main.main(["-v", "--text", "test"])
            assert exit_code == 0
            # Verify INFO level log appears
            assert "Processing text:" in caplog.text
            assert "test" in caplog.text

    @pytest.mark.unit
    def test_main_with_verbose_flag_debug_level(self, caplog: pytest.LogCaptureFixture) -> None:
        """Test main function with -vv (or --verbose --verbose) enables DEBUG logging."""
        with caplog.at_level(logging.DEBUG):
            # Test short form -vv
            exit_code = main.main(["-vv", "--text", "debug test"])
            assert exit_code == 0
            assert "Processing text:" in caplog.text
            assert "debug test" in caplog.text
