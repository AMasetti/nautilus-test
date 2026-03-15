import pytest

from fibonacci import fibonacci


class TestFibonacciFirst1000:
    """Test the first 1000 Fibonacci numbers by verifying the recurrence relation."""

    def test_base_case_0(self):
        assert fibonacci(0) == 0

    def test_base_case_1(self):
        assert fibonacci(1) == 1

    def test_recurrence_relation_for_first_1000(self):
        """Verify fib(n) == fib(n-1) + fib(n-2) for n = 2..999."""
        prev2 = fibonacci(0)
        prev1 = fibonacci(1)
        for n in range(2, 1000):
            current = fibonacci(n)
            assert current == prev1 + prev2, (
                f"fibonacci({n}) = {current}, but fibonacci({n-1}) + fibonacci({n-2}) = {prev1 + prev2}"
            )
            prev2 = prev1
            prev1 = current

    def test_known_values(self):
        """Spot-check well-known Fibonacci values within the first 1000."""
        known = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            6: 8,
            7: 13,
            10: 55,
            20: 6765,
            30: 832040,
            50: 12586269025,
        }
        for n, expected in known.items():
            assert fibonacci(n) == expected


class TestFibonacciNegativeInput:
    """Custom test: verify that negative inputs raise ValueError."""

    def test_negative_raises_value_error(self):
        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            fibonacci(-1)

    def test_large_negative_raises_value_error(self):
        with pytest.raises(ValueError, match="n must be a non-negative integer"):
            fibonacci(-100)
