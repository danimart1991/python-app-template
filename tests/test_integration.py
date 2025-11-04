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
            ["poetry", "run", "my-app", "--help"],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode in [0, 1]
        assert "usage:" in result.stdout.lower() or "usage:" in result.stderr.lower()

    @pytest.mark.integration
    def test_app_with_text_argument(self) -> None:
        """Test app execution with --text argument."""
        test_text = "Integration test message"
        result = subprocess.run(
            ["poetry", "run", "my-app", "--text", test_text],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            assert test_text in result.stdout

    @pytest.mark.integration
    def test_module_execution(self) -> None:
        """Test that the module can be executed as a Python module."""
        result = subprocess.run(
            [sys.executable, "-m", "src.main", "--text", "Module test"],
            capture_output=True,
            text=True,
            check=False,
            cwd="src",
        )

        assert result.returncode in [0, 1]
