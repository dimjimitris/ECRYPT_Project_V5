# Python Implementation of Rabin Digital Signature

## Project Description
This project is a Python implementation of the Rabin digital signature algorithm. It is developed as part of the ECRYPT course at WUT.

## Author
Dimitrios Georgousis

## Project Topic
V.5 Rabin Digital Signature

## Environment
- Development: Windows 11 Pro 64-bit
```shell
PS > python --version
Python 3.12.1
PS > pip show sympy
Name: sympy
Version: 1.12
Summary: Computer algebra system (CAS) in Python
Home-page: https://sympy.org
Author: SymPy development team
Author-email: sympy@googlegroups.com
License: BSD
Location: %%%
Requires: mpmath
Required-by: torch
```
- Testing:
```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy
$ python3 --version
Python 3.10.12
$ pip show sympy
Name: sympy
Version: 1.12
Summary: Computer algebra system (CAS) in Python
Home-page: https://sympy.org
Author: SymPy development team
Author-email: sympy@googlegroups.com
License: BSD
Location: %%%
Requires: mpmath
Required-by:
```
As required by the project description our program was tested and works in `Python 3.10` environments.

## Usage
To use this implementation, follow these steps:
1. Clone the repository.
2. Install the required dependencies.
3. Run `test.py` to observe the results of some testing we did on our algorithms
4. `rabin_signature.py` contains the functions used for key generation, signing and verifying.

## Rabin Signature API

The `rabin_signature.py` module provides the following functions for key generation, signing, and verifying:

- `key_generation(bits)`: Generates a public-private key pair for Rabin digital signature, the primes used are of length `bits`.
- `sign(message, private_key, k)`: Signs a message using the private key and returns the signature. `k` is a parameter used for specifying the length of a random string appended at the end of the message.
- `verify(message, signature, public_key)`: Verifies the signature of a message using the public key.

To use these functions, import the `rabin_signature` module and call the respective functions.

## Algorithm Explanation

The `hash function` and parameter `k` (controls size of random string appended to message) are public (known to everyone).

Prime numbers we use as private key: if `p` is such a prime then we select `p mod 4 = 3` or `4 | (p + 1)`.

These primes come in handy, because the Rabin algorithm looks for quadratic residues modulo a prime. And we know that:
if there exists `x` such that `x^2 mod p = c` then one such `x` is `x = c^((p + 1) / 4) mod p` (A).

- Key generation: key generation function is nothing special. We produce 2 primes that leave remainder 3 when divided by 4. These primes are the private key and their product is the public key.
- Signing:
    1. produce random string `u` of length `k` bits
    2. append `u` at the end of message `message`
    3. calculate the hash value of this string, let's call it `c`
    4. Check if `c` is a q.r. modulo `n`, where `n` is the public key. To do this we can, equivalently, check if `c` is a q.r. `mod p` and `mod q` where `p`, `q` are the private key. We do we evaluate the Jacobi Symbol. If c is not a q.r. modulo `n` then we go back to step (1.), otherwise, we continue. (It will take about 4 tries to satisfy this criterion)
    5. Find `x` such that `x^2 mod n = c`.
        1. First we find `x_p`, `x_q` such that `x_p^2 mod p = c` and `x_q^2 mod q = c`
        2. We are looking for `a`, `b` such that `a = 1 mod p`, `a = 0 mod q`, `b = 0 mod p`, `b = 1 mod q`. Then `x = a * x_p + b * x_q` will be a solution to our original problem.
        3. How do we find them?
            1. Solve CRT for: `x = x_p mod p` and `x = x_q mod q`.
            2. The solution gives us: `y_p` and `y_q` such that `p * y_p + q * y_q = 1` (Extended GCD algorithm), so `y_p = p^(-1) mod q` and `y_q = q^(-1) mod p`.
            3. `x = (q * y_q) * x_p + (p * y_p) * x_q`
            4. Test if `a = q * y_q` and `b = p * y_p` satisfy the previous conditions. We can easily observe that they do.
        4. Thus, the solution is `x = (q * y_q) * x_p + (p * y_p) * x_q mod n`
    6. We return the signature `(x, u)`
- Verification: Verification isn't anything special. We compute `x^2` and `c = hash of message + u` and compare the two modulo `n`, where `n` is the public key.

The safety of this signature system lies with the fact that solving `x^2 = c mod n` when the factorization of `n` is not known is equivalent to integer factorization of `n` which is a hard problem.

## References
For more information about the Rabin digital signature algorithm, refer to the following resources:
- [Wikipedia](https://en.wikipedia.org/wiki/Rabin_signature_algorithm)
- [Rabin Publication](http://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-212.pdf)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.