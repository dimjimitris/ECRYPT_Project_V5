import random

from rabin_signature import key_generation, sign, verify

def _main():
    message_list = [
        "hello world",
        "this is a test",
        "another test",
        "1",
        "what about this message",
        "lorem ipsum",
        "answer to universe and everything",
    ]

    for message in message_list:
        print(f"Message: {message}")
        random.seed(17)
        bits = 512
        k = 64

        n, private_key = key_generation(bits)
        print(f"Public key: {n}")
        print(f"Private key: {private_key}")

        signature = sign(message, private_key, k)
        x, u = signature
        print(f"Square root: {x}")
        print(f"Random string: {u}")

        print(f"Verification: {verify(message, signature, n)}")
        print("-" * 20)

if __name__ == "__main__":
    _main()