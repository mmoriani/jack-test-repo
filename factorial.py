def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def factorial_sequence(count: int) -> list[int]:
    return [factorial(i) for i in range(count)]


if __name__ == "__main__":
    print(factorial_sequence(8))
    print(f"factorial(5): {factorial(5)}")
