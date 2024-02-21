import typing as tp

# str.maketrans('ar', 'by') #сам сменяет символы на код и создает словарь
# 'htllo'.translate({})
#
# 'arroz'.translate({97:98, 114:121})
# ord('a') #получить код символа
#
# abc = 'abcdefghij...'
# ces = 'defghij...' #создаем словарь и словарь шифра и передаем в макетранс далее в транслейт
# АВС = 'ABCDEF...'
#
# d1 = {1:2, 2:3}
# d2 = {2:3}
# d1.update(d2)
# d_all ={**d1, ***d2}
#
# d_end = [shift:] + [:shift]
#
# print(*a) #чтобы каждый элемент словарепй, списков отдельно выводился

abc = 'abcdefghijklmnopqrstuvwxyz'#string.ascii_letters


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""

    for i in range(len(plaintext)):
        symbol = ord(plaintext[i])
        if (symbol > 64) and (symbol < 91):
            if (symbol + shift) > 90:
                ciphertext += chr(symbol - 26 + shift)

                continue

            ciphertext += chr(symbol + shift)
        elif (symbol > 96) and (symbol < 122):
            if (symbol + shift) > 121:
                ciphertext += chr(symbol - 26 + shift)

                continue

            ciphertext += chr(symbol + shift)
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""

    for i in range(len(ciphertext)):
        symbol = ord(ciphertext[i])
        if (symbol > 64) and (symbol < 91):
            if (symbol - shift) < 65:
                plaintext += chr(symbol + 26 - shift)
                continue

            plaintext += chr(symbol - shift)
        elif (symbol > 96) and (symbol < 122):
            if (symbol - shift) < 97:
                plaintext += chr(symbol + 26 - shift)
                continue

            plaintext += chr(symbol - shift)
        else:
            plaintext += ciphertext[i]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
