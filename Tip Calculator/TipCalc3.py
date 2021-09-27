num_pep = int(input("How many people are paying? "))
tax = float(input("Tax Rate (%): "))
service = float(input("Service Rate (%): "))
num_dish = int(input("Number of Dishes: "))

dishes = []
price = []
for en in range(1, num_dish+1):
    en_number = str(en)
    dishes.append(input("Dish " + en_number + " Name: "))
    price.append(float(input("Dish " + en_number + " Price ($): ")))
print("======================Happy Restaurant Bill======================")
for res in range(1, num_dish+1):
    res_num = str(res)
    pc = str(price[res-1])
    tx = str(format(float(price[res-1]*tax/100), '.2f'))
    sr = str(format(float(price[res-1]*service/100), '.2f'))
    print("Cost For Dish " + res_num + " | " + dishes[res-1] + " :", pc + ", Tax: " + tx + ", Service: " + sr)
print("Subtotal Per Person: ", (sum(price) + (sum(price)*(tax+service)/100))/num_pep)
print("Total Cost: ", sum(price) + (sum(price)*(tax+service)/100))
print("===========Thank you for visiting \"Dinner Restaurant\"==========")
print("========================Come again soon!=========================")
