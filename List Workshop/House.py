house = ["John", "Sally", "Joe", "Sue", "Ash"]

# Start at the first house
address = 0

# While the address is valid
while address < len(house):
    # Get the person at the given address
    person = house[address]

    # Print the person at the house
    print("House " + str(address+1) + " has " + person)

    # Go to the next address
    address = address + 1
