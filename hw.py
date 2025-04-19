import random
from math import gcd


def generate_keys():
    primes = [i for i in range(2, 10**6) if all(i % d != 0 for d in range(2, int(i**0.5) + 1))]
    p, q = random.sample(primes, 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = next(x for x in range(2, phi_n) if gcd(x, phi_n) == 1)
    d = pow(e, -1, phi_n)
    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)