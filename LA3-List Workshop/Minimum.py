number = [5, 3, 3, 2, 6]

# Assume the first element is the biggest
biggest = number[0]

index = 0
while index < len(number):
    if number[index] < biggest:
        smallest = number[index]
    index = index + 1

print(smallest)
