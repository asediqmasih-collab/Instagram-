"""Comprehensive test suite for Instagram brute-force tool."""

import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock
from instagram import valid_int, valid_float
from argparse import ArgumentTypeError


class TestValidation:
    """Test input validation functions."""

    def test_valid_int_valid_input(self):
        """Test valid_int with valid inputs."""
        assert valid_int("0") == 0
        assert valid_int("1") == 1
        assert valid_int("2") == 2
        assert valid_int("3") == 3

    def test_valid_int_invalid_non_numeric(self):
        """Test valid_int with non-numeric input."""
        with pytest.raises(ArgumentTypeError):
            valid_int("abc")

    def test_valid_int_invalid_too_large(self):
        """Test valid_int with value > 3."""
        with pytest.raises(ArgumentTypeError):
            valid_int("4")

    def test_valid_int_invalid_negative(self):
        """Test valid_int with negative value."""
        with pytest.raises(ArgumentTypeError):
            valid_int("-1")

    def test_valid_float_valid_input(self):
        """Test valid_float with valid inputs."""
        assert valid_float("0.0") == 0.0
        assert valid_float("0.5") == 0.5
        assert valid_float("1.0") == 1.0

    def test_valid_float_invalid_too_large(self):
        """Test valid_float with value > 1."""
        with pytest.raises(ArgumentTypeError):
            valid_float("1.5")

    def test_valid_float_invalid_negative(self):
        """Test valid_float with negative value."""
        with pytest.raises(ArgumentTypeError):
            valid_float("-0.5")

    def test_valid_float_invalid_non_numeric(self):
        """Test valid_float with non-numeric input."""
        with pytest.raises(ArgumentTypeError):
            valid_float("abc")


class TestFileOperations:
    """Test file operations."""

    def test_password_file_exists(self):
        """Test that passwords.txt file exists."""
        assert os.path.exists('passwords.txt')

    def test_proxies_file_exists(self):
        """Test that proxies.txt file exists."""
        assert os.path.exists('proxies.txt')

    def test_password_file_not_empty(self):
        """Test that passwords.txt is not empty."""
        with open('passwords.txt', 'r') as f:
            content = f.read().strip()
            assert len(content) > 0

    def test_proxies_file_not_empty(self):
        """Test that proxies.txt is not empty."""
        with open('proxies.txt', 'r') as f:
            content = f.read().strip()
            assert len(content) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
