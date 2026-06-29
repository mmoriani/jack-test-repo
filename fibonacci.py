def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_sequence(count: int) -> list[int]:
    return [fib(i) for i in range(count)]


if __name__ == "__main__":
    print(fib_sequence(10))
    print(f"fib(20): {fib(20)}")
