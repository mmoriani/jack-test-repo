def power(base: int, exponent: int) -> int:
    if exponent < 0:
        raise ValueError("exponent must be >= 0")
    result = 1
    for _ in range(exponent):
        result *= base
    return result


if __name__ == "__main__":
    print(f"power(2, 10): {power(2, 10)}")
    print(f"power(3, 5): {power(3, 5)}")
