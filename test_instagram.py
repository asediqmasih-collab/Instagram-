"""Comprehensive test suite for Instagram brute-force tool."""

import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock
from instagram import Engine, valid_int, valid_float, display_database_stats, prune_database
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


class TestEngine:
    """Test Engine class functionality."""

    def test_engine_initialization(self):
        """Test Engine initialization."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("password1\npassword2\n")
            passlist_path = f.name

        try:
            engine = Engine("testuser", 8, passlist_path, True)
            assert engine.username == "testuser"
            assert engine.threads == 8
            assert engine.passlist_path == passlist_path
            assert engine.is_alive is True
            assert engine.resume is False
        finally:
            os.unlink(passlist_path)

    def test_engine_stop(self):
        """Test Engine stop method."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("password1\n")
            passlist_path = f.name

        try:
            engine = Engine("testuser", 8, passlist_path, True)
            engine.stop()
            assert engine.is_alive is False
        finally:
            os.unlink(passlist_path)

    def test_write_to_file(self):
        """Test credentials file writing."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("password1\n")
            passlist_path = f.name

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            credentials_file = f.name

        try:
            engine = Engine("testuser", 8, passlist_path, True)
            # Mock the credentials file location
            with patch('instagram.credentials', credentials_file):
                engine.write_to_file("foundpassword123")
                
                with open(credentials_file, 'r') as f:
                    content = f.read()
                    assert "Testuser" in content
                    assert "foundpassword123" in content
        finally:
            os.unlink(passlist_path)
            if os.path.exists(credentials_file):
                os.unlink(credentials_file)


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


class TestIntegration:
    """Integration tests."""

    def test_engine_initialization_with_real_files(self):
        """Test Engine with real files in repo."""
        try:
            engine = Engine("testuser", 8, "passwords.txt", True)
            assert engine.username == "testuser"
            assert engine.threads == 8
            assert os.path.exists(engine.passlist_path)
            engine.stop()
        except Exception as e:
            # Skip if lib dependencies are not available
            if "ModuleNotFoundError" not in str(type(e).__name__):
                raise


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
