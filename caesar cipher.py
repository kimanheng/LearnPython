# The Encryption Function
def encrypt(message, key):
    encrypted = ""  # storage for new message
    for _ in message:  # loop for every letters in the message
        if _.isupper():  # if the letter is uppercase
            encrypted += chr((ord(_) - ord('A') + key) % 26 + ord('A'))  # First it convert the letter to number
            # by subtract the number value of that letter with the number value of 'A', then we add the key
            # After we add the key, we divide it by 26, but we only take the reminder and add the number value of 'A'.
            # Finally after we add everything, we convert the result to character
            # Then add that result into the variable encrypted
        elif _.islower():  # if the letter is lowercase
            encrypted += chr((ord(_) - ord('a') + key) % 26 + ord('a'))  # First it convert the letter to number
            # by subtract the number value of that letter with the number value of 'a', then we add the key
            # After we add the key, we divide it by 26, but we only take the reminder and add the number value of 'a'.
            # Finally after we add everything, we convert the result to character
            # Then add that result into the variable encrypted
        else:  # if it's not letter (number, punctuation, space)
            encrypted += _  # preserve the number, punctuation and space as it is
    return encrypted  # return the variable encrypted (string)


# The Decryption Function
def decrypt(message, key):
    decrypted = ""  # storage for new message
    for _ in message:  # loop for every letters in the message
        if _.isupper():  # if the letter is uppercase
            decrypted += chr((ord(_) - ord('A') - key) % 26 + ord('A'))  # First it convert the letter to number
            # by subtract the number value of that letter with the number value of 'A' then we subtract the key
            # After we add the key, we divide it by 26, but we only take the reminder and add the number value of 'A'.
            # Finally after we add everything, we convert the result to character
            # Then add that result into the variable encrypted
        elif _.islower():  # if the letter is lowercase
            decrypted += chr((ord(_) - ord('a') - key) % 26 + ord('a'))  # First it convert the letter to number
            # by subtract the number value of that letter with the number value of 'a' then we minus the key
            # After we add the key, we divide it by 26, but we only take the reminder and add the number value of 'a'.
            # Finally after we add everything, we convert the result to character
            # Then add that result into the variable encrypted
        else:  # if it's not letter (number, punctuation, space)
            decrypted += _  # preserve the number, punctuation and space as it is
    return decrypted  # return the variable decrypted (string)


# The User Inputs
choice = int(input("Caesar Cipher\n1. Encrypt Message\n2. Decrypt Message\nYour Choice: "))  # Ask for user choice
text = input("Your Message: ")  # User input for var message in function
num = int(input("Shifting(Number): "))  # User input for var key in function
if choice == 1:  # If user use to encrypted the message
    print("Encrypted Message:", encrypt(text, num))  # Print the encrypted message by running the encrypt function
elif choice == 2:  # If user use to decrypt the message
    print("Decrypted Message:", decrypt(text, num))  # Print the decrypted message by running the decrypt function
