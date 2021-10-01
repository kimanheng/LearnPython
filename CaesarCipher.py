#All the calculation is done by using ASCII table to make sure everything is right.

# The Encryption Function
def cipher_encrypt(message, key):
    encrypted = "" #storage for new message
    
    #Loop for converting each letter
    for c in message: 
        
        #if it's uppercase
        if c.isupper(): 
            c_index = ord(c) - ord('A') #find index of the character
            c_new = chr((c_index + key) % 26 + ord('A')) #convert back to new letter (units after it)
            encrypted += c_new #add letter to encrypted var
            
        #if it's lowercase
        elif c.islower(): 
            c_index = ord(c) - ord('a') #find index of the character
            c_new = chr((c_index + key) % 26 + ord('a')) #convert back to new letter (units after it)
            encrypted += c_new #add letter to encrypted var
            
        #if it's digit
        elif c.isdigit(): 
            c_new = (int(c) + key) % 10 #convert number to the number after it
            encrypted += str(c_new) #add number to encrypted var
            
        #if it is just sign or space, just add it back   
        else:
            encrypted += c 
    return encrypted #return the value back


# The Decryption Function
def cipher_decrypt(message, key):
    decrypted = "" #storage for new message
    
    #Loop for converting each other
    for c in message: 
        
        #if the character is uppercase...
        if c.isupper(): 
            c_index = ord(c) - ord('A') #find index of the character
            c_new = chr((c_index - key) % 26 + ord('A')) #convert back to new letter (units before it)
            decrypted += c_new #add letter to decrypted var
            
        #if the character is lowercase...
        elif c.islower():
            c_index = ord(c) - ord('a') #find index of the character
            c_new = chr((c_index - key) % 26 + ord('a')) #convert back to new letter (units before it)
            decrypted += c_new #add letter to decrypted var
            
        #if it's digit
        elif c.isdigit():
            c_new = (int(c) - key) % 10 #convert number to the number before it
            decrypted += str(c_new) #add number to decrypted var
            
        #if it is just sign or space, just add it back     
        else:
            decrypted += c
    return decrypted #return the value back


#Collect User Input
choice = int(input("Caesir Cipher\n1. Encrypt Message\n2. Decrypt Message\nYour Choice: ")) 

#If the user type "1", ask user input and run def cipher_encrypted(message, key)
if choice == 1:
    text = input("\nPlain Text: ") #Ask for message (value go to var(message))
    num = int(input("Shifting(Number): ")) #Ask for how many units after it (value go to var(key))
    print("Encrypted message:",cipher_encrypt(text, num)) #Print back the (encrypted message) after running the function
    
#If the user type "2", ask user input and run def cipher_decrypted(message, key)   
elif choice == 2:
    text = input("\nCipher Text: ") #Ask for message (value go to var(message))
    num = int(input("Shifting(Number): ")) #Ask for how many units beofre it (value go to var(key))
    print("Decrypted message:", cipher_decrypt(text, num)) #Print back the (decrypted message) after running the function
