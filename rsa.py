def is_prime(n: int) -> bool:
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            continue
    return True
    pass
