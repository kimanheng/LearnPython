name = input("Enter your name: ")
total = 0
for letter in name:
    value = ord(letter)
    print("Character value:", value)
    total = total + value
print("The total sum of your ASCII name is", total)
