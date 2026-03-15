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


class TestFibonacciEdgeCases:
    """Edge cases and type handling."""

    def test_non_integer_float_raises(self):
        with pytest.raises(TypeError):
            fibonacci(3.5)

    def test_string_raises(self):
        with pytest.raises(TypeError):
            fibonacci("5")

    def test_none_raises(self):
        with pytest.raises(TypeError):
            fibonacci(None)

    def test_returns_int_type(self):
        for n in [0, 1, 2, 10, 50]:
            assert isinstance(fibonacci(n), int)


class TestFibonacciMathProperties:
    """Verify mathematical properties of the Fibonacci sequence."""

    def test_cassini_identity(self):
        """Cassini's identity: fib(n-1)*fib(n+1) - fib(n)^2 == (-1)^n."""
        for n in range(1, 100):
            lhs = fibonacci(n - 1) * fibonacci(n + 1) - fibonacci(n) ** 2
            assert lhs == (-1) ** n, f"Cassini's identity failed at n={n}"

    def test_gcd_property(self):
        """gcd(fib(m), fib(n)) == fib(gcd(m, n))."""
        from math import gcd

        pairs = [(6, 9), (10, 15), (12, 8), (20, 30), (7, 11)]
        for m, n in pairs:
            assert gcd(fibonacci(m), fibonacci(n)) == fibonacci(gcd(m, n)), (
                f"GCD property failed for m={m}, n={n}"
            )

    def test_golden_ratio_convergence(self):
        """fib(n)/fib(n-1) converges to the golden ratio phi."""
        phi = (1 + 5**0.5) / 2
        ratio = fibonacci(50) / fibonacci(49)
        assert abs(ratio - phi) < 1e-10


class TestFibonacciLargeValues:
    """Verify the function handles large indices correctly."""

    def test_fib_1000(self):
        """Known value for fib(1000)."""
        expected = (
            "4346655768693745643568852767504062580256466051737178"
            "0402481729089536555417949051890403879840079255169295"
            "9225930803226347752096896232398733224711616429964409"
            "06533187938298969649928516003704476137795166849228875"
        )
        assert str(fibonacci(1000)) == expected

    def test_monotonically_increasing_after_2(self):
        """fib(n) > fib(n-1) for all n >= 3 (since fib(2) == fib(1) == 1)."""
        prev = fibonacci(2)
        for n in range(3, 200):
            curr = fibonacci(n)
            assert curr > prev, f"fibonacci({n}) <= fibonacci({n-1})"
            prev = curr
