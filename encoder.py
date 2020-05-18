from alphabet_encoder import AlphabetEncoder
from key_generator import KeyGenerator
from pulverizer import Pulverizer

class Encoder(AlphabetEncoder):
    def __init__(self, public_key):
        super().__init__()
        self.public_key = public_key
        self.pulverizer = Pulverizer()

    def encode(self, string):
        message = super().encode(string)

        gcd, _, _ = self.pulverizer.calculate_gcd(message, self.public_key[1])
        if gcd != 1:
            raise Exception('Incorrect key. Generate another one.')

        print(message)
        encoded_message = pow(message, self.public_key[0]) % self.public_key[1]
        return encoded_message

keyGenerator = KeyGenerator(size=1024, test=False)
print(keyGenerator.public_key, '\n', keyGenerator.private_key)
encoder = Encoder(keyGenerator.public_key)
encoded_message = encoder.encode('Hello, world!')
# print(encoded_message)
print(keyGenerator.decode(encoded_message))