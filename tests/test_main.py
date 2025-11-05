"""Unit tests for the main module."""

import pytest

from src.main import _create_parser, _process_text, main


class TestProcessText:
    """Test cases for the process_text function."""

    @pytest.mark.unit
    def test_process_text_returns_input(self, sample_text: str) -> None:
        """Test that process_text returns the input text unchanged."""
        result = _process_text(sample_text)
        assert result == sample_text

    @pytest.mark.unit
    def test_process_text_with_empty_string(self) -> None:
        """Test process_text with an empty string."""
        result = _process_text("")
        assert result == ""

    @pytest.mark.unit
    def test_process_text_with_special_characters(self) -> None:
        """Test process_text with special characters."""
        text = "Hello! @#$ %^& *() World"
        result = _process_text(text)
        assert result == text


class TestCreateParser:
    """Test cases for the _create_parser function."""

    @pytest.mark.unit
    def test_create_parser_returns_parser(self) -> None:
        """Test that _create_parser returns an ArgumentParser."""
        parser = _create_parser()
        assert parser is not None
        assert parser.prog == "my-app"

    @pytest.mark.unit
    def test_parser_accepts_text_argument(self) -> None:
        """Test that the parser accepts --text argument."""
        parser = _create_parser()
        args = parser.parse_args(["--text", "test"])
        assert args.text == "test"

    @pytest.mark.unit
    def test_parser_text_argument_optional(self) -> None:
        """Test that --text argument is optional."""
        parser = _create_parser()
        args = parser.parse_args([])
        assert args.text is None


class TestMain:
    """Test cases for the main function."""

    @pytest.mark.unit
    def test_main_with_text_returns_success(
        self, sample_text: str, capsys: pytest.CaptureFixture
    ) -> None:
        """Test main function with --text argument returns 0."""
        exit_code = main(["--text", sample_text])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert sample_text in captured.out

    @pytest.mark.unit
    def test_main_without_arguments_returns_success(self, capsys: pytest.CaptureFixture) -> None:
        """Test main function without arguments shows help and returns 0."""
        exit_code = main([])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert "usage:" in captured.out.lower()

    @pytest.mark.unit
    def test_main_with_empty_text(self, capsys: pytest.CaptureFixture) -> None:
        """Test main function with empty text."""
        exit_code = main(["--text", ""])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert captured.out == "\n"

    @pytest.mark.unit
    def test_main_with_version_flag(self, capsys: pytest.CaptureFixture) -> None:
        """Test main function with --version flag."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])

        assert exc_info.value.code == 0
