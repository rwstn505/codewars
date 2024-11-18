class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        return ''.join(
            chr((ord(char) - 65 + self.shift) % 26 + 65) if char.isalpha() else char
            for char in st.upper()
        )

    def decode(self, st):
        return ''.join(
            chr((ord(char) - 65 - self.shift) % 26 + 65) if char.isalpha() else char
            for char in st.upper()
        )


c = CaesarCipher(5)
print(c.encode('Codewars'))  # HTIJBFWX
print(c.decode('HTIJBFWX'))  # CODEWARS