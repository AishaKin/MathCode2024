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

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
