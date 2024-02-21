def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyword = keyword.upper()

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    keyword = keyword.upper()

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            plaintext += char

    return plaintext
