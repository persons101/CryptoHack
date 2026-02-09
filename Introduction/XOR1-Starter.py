from Crypto.Util.number import *

example = "label"

example_xor = ""
for char in example:
    char_in_bytes = ord(char)
    example_xor += chr((char_in_bytes) ^ 13)

print(f"crypto{{{example_xor}}}")