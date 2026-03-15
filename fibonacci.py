def fibonacci(x):
    if x < 0:
        raise ValueError("Index must be a non-negative integer")
    if x == 0:
        return 0
    if x == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <index>")
        sys.exit(1)

    index = int(sys.argv[1])
    print(fibonacci(index))
