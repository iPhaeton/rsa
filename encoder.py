from alphabet_encoder import AlphabetEncoder
from key_generator import KeyGenerator

class Encoder(AlphabetEncoder):
    def __init__(self, public_key):
        self.public_key = public_key

    def encode(self, string):
        message = super().encode(string)
        print(message)
        encoded_message = pow(message, self.public_key[0]) % self.public_key[1]
        return encoded_message

keyGenerator = KeyGenerator(size=1024, test=False)
print(keyGenerator.public_key, '\n', keyGenerator.private_key)
encoder = Encoder(keyGenerator.public_key)
encoded_message = encoder.encode('Hello, world!')
# print(encoded_message)
print(keyGenerator.decode(encoded_message))