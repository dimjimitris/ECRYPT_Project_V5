import sympy
import random
import hashlib
import string

# def _extended_gcd_recursive(a, b):
#    def aux(a, b):
#        if b == 0: (base step of induction)
#            return a, 1, 0 # a * 1 + b * 0 = a
#        else:
#            gcd, x, y = aux(b, a % b) # b * x + (a % b) * y = gcd
#                                      # (hypothesis of induction)
#            # Prove (induction step):
#            # a * y + b * (x - (a // b) * y) = gcd
#            # a * y + b * x - b * (a // b) * y = gcd
#            # a * y + b * x - (a - a % b) * y = gcd
#            # a * y + b * x - a * y + (a % b) * y = gcd
#            # b * x + (a % b) * y = gcd, which is true
#            return gcd, y, x - (a // b) * y
#
#    return aux(a, b)


# Wikipedia algorithm for extended Euclidean algorithm
def _extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def _jacobi_symbol(a, n):
    if n < 0 or not n % 2:
        raise ValueError("n should be an odd positive integer")
    if a < 0 or a > n:
        a %= n
    # a is formatted as 0 <= a < n and n is an odd positive integer

    if not a:
        return int(n == 1)
    if n == 1 or a == 1:
        return 1

    # if a and n are not coprime then Jacobi(a, n) = 0
    if sympy.igcd(a, n) != 1:
        return 0

    # Initialize the Jacobi symbol
    j = 1
    # Follow the algorithm steps (wikipedia page for Jacobi symbol)
    while a != 0:
        while a % 2 == 0 and a > 0:
            a >>= 1
            if n % 8 in [3, 5]:
                j = -j
        a, n = n, a
        if a % 4 == n % 4 == 3:
            j = -j
        a %= n
    return j


def _generate_rabin_prime(bits):
    while True:
        p = sympy.randprime(2 ** (bits - 1), 2**bits)
        if p % 4 == 3:
            return p


def _hash_function(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)


def _random_string(k):
    """
    Generate a random string of printable characters.
    Input: k - the number of bits in the generated string
    Output: a random string of printable characters
    """
    characters = k // 8
    return "".join(random.choices(string.printable, k=characters))


def key_generation(bits):
    """
    Generate a Rabin signature key pair.
    Input: bits - the number of bits in the primes p and q
    Output: n - the public key, (p, q) - the private key
    """
    p = _generate_rabin_prime(bits)
    q = _generate_rabin_prime(bits)
    while p == q:
        q = _generate_rabin_prime(bits)
    n = p * q

    return n, (p, q)


def sign(message, private_key, k=256):
    """
    Sign a message using the Rabin signature scheme.
    Input: message - the message to sign,
           private_key - the private key,
           k - the number of random bits to use
    Output: (x, u) - the signature
    """
    p, q = private_key
    n = p * q

    while True:
        u = _random_string(k)
        c = _hash_function(message + u) % n

        # check x^2 = c mod n, this will be true iff
        # c is a quadratic residue mod p and mod q.
        if _jacobi_symbol(c, p) != 1 or _jacobi_symbol(c, q) != 1:
            continue

        # find x_p^2 = c mod p and x_q^2 = c mod q
        # solve for x using the Chinese Remainder Theorem
        # x = x_p mod p, x = x_q mod q
        # y_p * p + y_q * q = 1
        # y_p = p^-1 mod q, y_q = q^-1 mod p
        # a = q * y_q, b = p * y_p
        # a = 0 mod q, a = 1 mod p
        # b = 0 mod p, b = 1 mod q
        # x = x_p * a + x_q * b mod n, so
        # x = x_p * q * y_q + x_q * p * y_p mod n
        x_p = pow(c, (p + 1) // 4, p)  # known formula
        x_q = pow(c, (q + 1) // 4, q)  # known formula

        _, y_p, y_q = _extended_gcd(p, q)
        x = (x_p * q * y_q + x_q * p * y_p) % n
        return x, u


def verify(message, signature, public_key):
    """
    Verify a message using the Rabin signature scheme.
    Input: message - the message to verify,
           signature - the signature,
           public_key - the public key
    Output: True if the signature is valid, False otherwise
    """
    n = public_key
    x, u = signature
    c = _hash_function(message + u) % n
    return pow(x, 2, n) == c


def _main():

    bits = 512
    k = 64
    message = str(input("Enter a message: "))

    n, private_key = key_generation(bits)
    print("Public key:", n)
    print("Private key:", private_key)

    signature = sign(message, private_key, k)
    print("Signature:", signature)

    print("Verification:", verify(message, signature, n))


if __name__ == "__main__":
    _main()
