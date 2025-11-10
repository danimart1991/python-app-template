"""Integration tests for the application."""

import subprocess
import sys

import pytest


class TestAppIntegration:
    """Integration tests for the application."""

    @pytest.mark.integration
    def test_app_executable_exists(self) -> None:
        """Test that the app can be executed via poetry."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--help"],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower() or "usage:" in result.stderr.lower()

    @pytest.mark.integration
    def test_app_with_text_argument(self) -> None:
        """Test app execution with --text argument."""
        test_text = "Integration test message"
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--text", test_text],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert test_text in result.stdout

    @pytest.mark.integration
    def test_module_execution(self) -> None:
        """Test that the module can be executed as a Python module."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--text", "Module test"],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert "Module test" in result.stdout

    @pytest.mark.integration
    def test_verbose_flag_single(self) -> None:
        """Test app with single -v flag (INFO level)."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "-v", "--text", "verbose test"],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert "verbose test" in result.stdout

    @pytest.mark.integration
    def test_verbose_flag_double(self) -> None:
        """Test app with -vv flag (DEBUG level) shows debug messages."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "-vv", "--text", "debug test"],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert "debug test" in result.stdout
        # Debug log should appear in stderr
        assert "Processing text:" in result.stderr or "DEBUG" in result.stderr

    @pytest.mark.integration
    def test_verbose_long_form(self) -> None:
        """Test app with --verbose flag (long form)."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--verbose", "--text", "long form test"],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert "long form test" in result.stdout

    @pytest.mark.integration
    def test_multiple_verbose_flags(self) -> None:
        """Test app with multiple --verbose flags."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "src.main",
                "--verbose",
                "--verbose",
                "--text",
                "multiple verbose",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert "multiple verbose" in result.stdout
        assert "Processing text:" in result.stderr or "DEBUG" in result.stderr

    @pytest.mark.integration
    def test_no_verbose_no_debug_output(self) -> None:
        """Test that without verbose flag, no debug messages appear."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--text", "no verbose"],
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0
        assert "no verbose" in result.stdout
        # Debug messages should NOT appear
        assert "Processing text:" not in result.stderr
        assert "DEBUG" not in result.stderr
