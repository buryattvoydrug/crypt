def encrypt_caesar(plaintext, shift=3):
    import string
    letters = string.ascii_letters
    abc = letters[:len(letters)//2]
    ABC = letters[len(letters)//2:]
    cipher_letters = abc[shift:]+abc[:shift]+ABC[shift:]+ABC[:shift]
    table = str.maketrans(letters, cipher_letters)
    ciphertext = plaintext.translate(table)
    return ciphertext


def decrypt_caesar(plaintext, shift=3):
    plaintext = encrypt_caesar(plaintext, -shift)
    return plaintext


encrypt_caesar("PYTHON", shift=3)
encrypt_caesar("python")
encrypt_caesar("Python3.6")
encrypt_caesar("")
decrypt_caesar("SBWKRQ")
decrypt_caesar("sbwkrq")
decrypt_caesar("Sbwkrq3.6")
decrypt_caesar("")
