from Crypto.Util import number
from pulverizer import Pulverizer

class KeyGenerator:
    def __init__(self):
        self.pulverizer = Pulverizer()
        self.public_key = None
        self.private_key = None
        self.generate_keys()

    def getPrime(self, N):
        return number.getPrime(N)

    def calculate_n(self):
        p = self.getPrime(1024)
        q = self.getPrime(1024)
        return p, q, p * q

    def calculate_fi(self, p, q):
        return (p - 1) * (q - 1)

    def calculate_e(self, n, fi_of_n):
        return fi_of_n + self.getPrime(256)

    def generate_keys(self):
        if (self.public_key != None):
            raise Exception('KeyGenerator cannot be reinitialized')

        p, q, n = self.calculate_n()
        fi_of_n = self.calculate_fi(p, q)
        e = self.calculate_e(n, fi_of_n)
        
        self.public_key = (e, n)

        _, d, _ = self.pulverizer.calculate_gcd(e, fi_of_n)

        while d < 0:
            d += fi_of_n

        self.private_key = (d, e)

keyGenerator = KeyGenerator()

print(keyGenerator.public_key, '\n\n', keyGenerator.private_key)