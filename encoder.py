from alphabet_encoder import AlphabetEncoder
from key_generator import KeyGenerator

class Encoder(AlphabetEncoder):
    def __init__(self, public_key):
        self.public_key = public_key

    def encode(self, string):
        message = super().encode(string)
        pow(message, self.public_key[0])
        # encoded_message = pow(message, self.public_key[0]) % self.public_key[1]
        # return encoded_message

keyGenerator = KeyGenerator()
encoder = Encoder(keyGenerator.public_key)
print(encoder.encode('Hello world!'))