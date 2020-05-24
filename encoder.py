from alphabet import AlphabetEncoder
from key_generator import KeyGenerator
from pulverizer import Pulverizer
from modulo import modulo

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

        # encoded_message = pow(message, self.public_key[0]) % self.public_key[1]
        encoded_message = modulo(message, self.public_key[0], self.public_key[1])
        return encoded_message

keyGenerator = KeyGenerator(size=1024, test=False)
print('Public key:', keyGenerator.public_key, '\n')
print('Private key:', keyGenerator.private_key, '\n')
encoder = Encoder(keyGenerator.public_key)
message = 'Some arbitrary string with spaces, commas (and exclamation marks)!'
print('Original message:', message, '\n')
encoded_message = encoder.encode(message)
print('Encoded message:', encoded_message, '\n')
print('Decoded message:', keyGenerator.decode(encoded_message))