import random
import unittest
from rabin_signature import key_generation, sign, verify


class TestRabinSignature(unittest.TestCase):
    def setUp(self):
        self.message_list = [
            "lore ipsum",
            "hello world",
            "this is a test",
            "a" * 1000,
            "b" * 1000,
            "what's the answer to life, the universe, and everything?",
            "42",
            "1+1=2",
            "1+1=3",
            "I am become death, the destroyer of worlds.",
            "This message is top secret!",
        ]
        self.bits = 512
        self.k = 64

    def test_key_generation(self):
        for _ in range(10):
            n, private_key = key_generation(self.bits)

            # Check if private_key is a tuple
            self.assertIsInstance(private_key, tuple)
            # Check if private_key has 2 elements
            self.assertEqual(len(private_key), 2)

    def test_sign_and_verify(self):
        for _ in range(10):
            for message in self.message_list:
                n, private_key = key_generation(self.bits)
                public_key = n
                signature = sign(message, private_key, self.k)
                # Check if signature is a tuple
                self.assertIsInstance(signature, tuple)

                # Check if signature has 2 elements
                self.assertEqual(len(signature), 2)
                self.assertTrue(
                    verify(message, signature, public_key)
                )  # Check if signature is valid


if __name__ == "__main__":
    random.seed(17)
    unittest.main()
