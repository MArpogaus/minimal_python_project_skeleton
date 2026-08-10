"""Tests for the example function."""

from minimal_python_project_skeleton import increment


def test_int() -> None:
    """Test that an int is incremented."""
    assert increment(3) == 4


def test_float() -> None:
    """Test that a float is incremented."""
    assert increment(3.0) == 4.0
