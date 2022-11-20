from primePy import primes


def tryToInt(number: str) -> int:
    """Checks if given number is integer.

    Args:
        number (string): Number as string

    Returns:
        bool: Whether number can be cast to integer
    """
    try:
        intNumber = int(number)
        return intNumber
    except ValueError:
        return -1


def validateForPrime(number: int) -> bool:
    """Checks if given number can be checked for being prime.

    Args:
        number (int): Number for check

    Returns:
        bool: False if number < 2, otherwise True
    """

    if number < 2:
        return False

    return True


def isPrime(number: int) -> bool:
    """Checks if number is a prime using AKS method.
    https://en.wikipedia.org/wiki/AKS_primality_test

    Args:
        number (int): Number > 1

    Returns:
        bool: If number is prime
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
