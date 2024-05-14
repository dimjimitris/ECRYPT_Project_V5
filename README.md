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

- The `hash function` and parameter `k` (controls size of random string appended to message) are public (known to everyone).



## References
For more information about the Rabin digital signature algorithm, refer to the following resources:
- [Wikipedia](https://en.wikipedia.org/wiki/Rabin_signature_algorithm)
- [Rabin Publication](http://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-212.pdf)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.