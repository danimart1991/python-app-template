"""Tests configuration and fixtures."""

import pytest


@pytest.fixture
def sample_text() -> str:
    """Provide sample text for testing."""
    return "Hello, World!"
