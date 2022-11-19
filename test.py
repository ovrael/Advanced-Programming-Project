def isPrime(number: int) -> bool:
    """Checks if number is a prime using AKS method.
    https://en.wikipedia.org/wiki/AKS_primality_test

    Args:
        number (int): Number > 1

    Returns:
        bool: _description_
    """
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return False

        i += w
        w = 6 - w

    return True


primeText = "prime" if isPrime(14) is True else "not prime"
print(primeText)
