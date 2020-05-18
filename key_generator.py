from Crypto.Util import number
from pulverizer import Pulverizer

class KeyGenerator:
    def __init__(self, size):
        self.size = size
        self.pulverizer = Pulverizer()
        self.public_key = None
        self.private_key = None
        self.generate_keys()

    def getPrime(self, N):
        return number.getPrime(N)

    def calculate_n(self):
        p = self.getPrime(self.size)
        q = self.getPrime(self.size)
        return p, q, p * q

    def calculate_fi(self, p, q):
        return (p - 1) * (q - 1)

    def calculate_e(self, n, fi_of_n):
        e = self.getPrime(8)
        gcd, _, _ = self.pulverizer.calculate_gcd(e, fi_of_n)
        while gcd != 1:
            e = self.getPrime(8)
            gcd, _, _ = self.pulverizer.calculate_gcd(e, fi_of_n)
        return e

    def generate_keys(self):
        if (self.public_key != None):
            raise Exception('KeyGenerator cannot be reinitialized')

        p, q, n = self.calculate_n()
        fi_of_n = self.calculate_fi(p, q)

        e = self.calculate_e(n, fi_of_n)
        _, d, _ = self.pulverizer.calculate_gcd(e, fi_of_n)

        while d < 0:
            d += fi_of_n

        self.public_key = (e, n)
        self.private_key = (d, n)

    def decode(self, encoded_message):
        return pow(encoded_message, self.private_key[0], self.private_key[1])


# keyGenerator = KeyGenerator(16)

# print(keyGenerator.public_key, '\n\n', keyGenerator.private_key)