class AlphabetEncoder:
    def encode(self, string):
        encoded_string = ''
        for ch in string:
            encoded_string += str(ord(ch))
        return int(encoded_string)

# alphabetEncoder = AlphabetEncoder()
# print(alphabetEncoder.encode('Hello world!'))