def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    import string
    keywordToText = ''.join(keyword[i % len(keyword)]
                            for i in range(len(plaintext)))
    letters = string.ascii_letters
    abc = letters[:len(letters)//2]+letters[:len(letters)//2]
    ABC = letters[len(letters)//2:]+letters[len(letters)//2:]
    ciphertext = ''.join((ABC[ABC.find(plaintext[i])+ABC.find(keywordToText[i])])
                         if plaintext[i].isupper()
                         else abc[abc.find(plaintext[i])+abc.find(keywordToText[i])]
                         for i in range(len(plaintext)))

    return ciphertext


print(encrypt_vigenere("PYTHON", "A"))
print(encrypt_vigenere("python", "a"))
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    import string
    keywordToText = ''.join(keyword[i % len(keyword)]
                            for i in range(len(ciphertext)))
    letters = string.ascii_letters
    abc = letters[:len(letters)//2]+letters[:len(letters)//2]
    ABC = letters[len(letters)//2:]+letters[len(letters)//2:]
    plaintext = ''.join((ABC[ABC.find(ciphertext[i])-ABC.find(keywordToText[i])])
                        if ciphertext[i].isupper()
                        else abc[abc.find(ciphertext[i])-abc.find(keywordToText[i])]
                        for i in range(len(ciphertext)))
    return plaintext


print(decrypt_vigenere("PYTHON", "A"))
print(decrypt_vigenere("python", "a"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
