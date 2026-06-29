def gcd(a: int, b: int) -> int:
    """Calcola il Massimo Comune Divisore di a e b usando l'algoritmo di Euclide."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calcola il Minimo Comune Multiplo di a e b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    num1, num2 = 48, 18
    print(f"GCD di {num1} e {num2}: {gcd(num1, num2)}")
    print(f"LCM di {num1} e {num2}: {lcm(num1, num2)}")

    num1, num2 = 15, 20
    print(f"GCD di {num1} e {num2}: {gcd(num1, num2)}")
    print(f"LCM di {num1} e {num2}: {lcm(num1, num2)}")
