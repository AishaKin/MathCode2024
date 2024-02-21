import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    def score(decrypted_text: str) -> int:
        words = decrypted_text.split()
        return sum(1 for word in words if word.lower() in dictionary)

    best_shift = 0
    max_score = 0

    for shift in range(26):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
                decrypted_char = decrypted_char.upper() if char.isupper() else decrypted_char
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        current_score = score(decrypted_text)
        if current_score > max_score:
            max_score = current_score
            best_shift = shift

    return best_shift