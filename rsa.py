def is_prime(n: int) -> bool:
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            continue
    return True
    pass


def gcd(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b
    pass


def multiplicative_inverse(e: int, phi: int) -> int:
    for d in range(phi):
        if (d*e) % phi == 1:
            return d
    pass


def generate_keypair(p: int, q: int):
    import random
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p*q
    # PUT YOUR CODE HERE

    phi = (p-1)*(q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


generate_keypair(7, 13)
