import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

# Example
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
