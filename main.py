def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]


def sum_primes(limit):
    print("Test")
    return sum(primes_up_to(limit))


def nth_prime(n):
    if n < 1:
        raise ValueError("n must be >= 1")
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate


def prime_factors(n):
    if n < 2:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    primes = primes_up_to(30)
    for p in primes:
        print(p)
    print(f"sum: {sum_primes(30)}")
    print(f"10th: {nth_prime(10)}")
    print(f"factors(360): {prime_factors(360)}")
