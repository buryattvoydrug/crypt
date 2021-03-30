def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    import string
    keywordToText = ''.join(keyword[i % len(keyword)]
                            for i in range(len(plaintext)))
    letters = string.ascii_letters
    abc = letters[:len(letters)//2]+letters[:len(letters)//2]
    ABC = letters[len(letters)//2:]+letters[len(letters)//2:]
    shift = ord("L")+ord("A")
    ciphertext = ''.join((ABC[ABC.find(plaintext[i])+ABC.find(keywordToText[i])])
                         if plaintext[i].isupper()
                         else abc[abc.find(plaintext[i])+abc.find(keywordToText[i])]
                         for i in range(len(plaintext)))

    return ciphertext


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    import string
    keywordToText = ''.join(keyword[i % len(keyword)]
                            for i in range(len(plaintext)))
    letters = string.ascii_letters
    abc = letters[:len(letters)//2]+letters[:len(letters)//2]
    ABC = letters[len(letters)//2:]+letters[len(letters)//2:]
    shift = ord("L")+ord("A")
    ciphertext = ''.join((ABC[ABC.find(plaintext[i])+ABC.find(keywordToText[i])])
                         if plaintext[i].isupper()
                         else abc[abc.find(plaintext[i])+abc.find(keywordToText[i])]
                         for i in range(len(plaintext)))

    return ciphertext


print(encrypt_vigenere("PYTHON", "A"))
print(encrypt_vigenere("python", "a"))
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
