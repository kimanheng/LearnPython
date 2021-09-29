numbers = []
total = 0
times_add = int(input("How many numbers you want to add? "))
for x in range(times_add):
    numbers.append(int(input("Number "+str(x+1)+": ")))
    total = total + numbers[x]
print("Total:", total)
