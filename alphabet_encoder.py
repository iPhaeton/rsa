import string

class AlphabetEncoder:
    def __init__(self):
        self.dictionary = dict( (key, i + 10) for i, key in enumerate([' ', ',', '!', '.', '(', ')', '{', '}', '[', ']'] + list(string.ascii_lowercase) + list(string.ascii_uppercase)))
    
    def encode(self, string):
        encoded_string = ''
        for ch in string:
            encoded_string += str(self.dictionary[ch])
        return int(encoded_string)

# alphabetEncoder = AlphabetEncoder()
# print(alphabetEncoder.dictionary)
# print(alphabetEncoder.encode('Hello world!'))