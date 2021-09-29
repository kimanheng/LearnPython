# The Encryption Function
def cipher_encrypt(message, key):
    encrypted = ""
    for c in message:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_new = chr((c_index + key) % 26 + ord('A'))
            encrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_new = chr((c_index + key) % 26 + ord('a'))
            encrypted += c_new
        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            encrypted += c
    return encrypted


# The Decryption Function
def cipher_decrypt(message, key):
    decrypted = ""
    for c in message:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_new = chr((c_index - key) % 26 + ord('A'))
            decrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_new = chr((c_index - key) % 26 + ord('a'))
            decrypted += c_new
        elif c.isdigit():
            c_new = (int(c) - key) % 10
            decrypted += str(c_new)
        else:
            decrypted += c
    return decrypted


choice = int(input("Caesir Cipher\n1. Encrypt Message\n2. Decrypt Message\nYour Choice: "))
if choice == 1:
    text = input("\nPlain Text: ")
    print("Encrypted message:",cipher_encrypt(text, 5))
elif choice == 2:
    text = input("\nCipher Text: ")
    print("Decrypted message:", cipher_decrypt(text, 5))
