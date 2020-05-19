import string

known_symbols = [' ', ',', '!', '.', '(', ')', '{', '}', '[', ']'] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

class AlphabetEncoder():
    def __init__(self):
        self.dictionary = dict( (key, i + 10) for i, key in enumerate(known_symbols))

    def encode(self, string):
        encoded_string = ''
        for ch in string:
            encoded_string += str(self.dictionary[ch])
        return int(encoded_string)

class AlphabetDecoder():
    def __init__(self):
        self.dictionary = dict( (i + 10, key) for i, key in enumerate(known_symbols))

    def decode(self, encoded_message):
        encoded_string = str(encoded_message)
        decoded_string = ''
        for i in range(0, len(encoded_string), 2):
            decoded_string += self.dictionary[int(encoded_string[i: i+2])]
        return decoded_string

# alphabetEncoder = AlphabetEncoder()
# print(alphabetEncoder.encode('Hello world!'))

# alphabetDecoder = AlphabetDecoder()
# print(alphabetDecoder.decode(53243131341110423437312312))