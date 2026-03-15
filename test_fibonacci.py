import subprocess
import sys

import pytest

from fibonacci import fibonacci


# --- Happy path ---


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_two():
    """Ticket example: func(x=2) = 1."""
    assert fibonacci(2) == 1


def test_fibonacci_small_values():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, val in enumerate(expected):
        assert fibonacci(i) == val, f"fibonacci({i}) should be {val}"


def test_fibonacci_ten():
    assert fibonacci(10) == 55


def test_fibonacci_twenty():
    assert fibonacci(20) == 6765


# --- Edge cases ---


def test_fibonacci_large_index():
    assert fibonacci(50) == 12586269025


# --- Error / failure scenarios ---


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)


def test_fibonacci_negative_large_raises():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-100)


# --- CLI entrypoint ---


def test_cli_valid_input(tmp_path):
    result = subprocess.run(
        [sys.executable, "fibonacci.py", "5"],
        capture_output=True,
        text=True,
        cwd="/private/tmp/nautilus-worktrees/INP-6",
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "5"


def test_cli_no_args():
    result = subprocess.run(
        [sys.executable, "fibonacci.py"],
        capture_output=True,
        text=True,
        cwd="/private/tmp/nautilus-worktrees/INP-6",
    )
    assert result.returncode == 1
    assert "Usage" in result.stdout


def test_cli_too_many_args():
    result = subprocess.run(
        [sys.executable, "fibonacci.py", "1", "2"],
        capture_output=True,
        text=True,
        cwd="/private/tmp/nautilus-worktrees/INP-6",
    )
    assert result.returncode == 1
    assert "Usage" in result.stdout
