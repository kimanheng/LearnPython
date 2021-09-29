num_pep = int(input("How many people are paying? "))
tax = float(input("Tax Rate (%): "))
service = float(input("Service Rate (%): "))
num_dish = int(input("Number of Dishes: "))

dishes = []
price = []
for en in range(num_dish):
    dishes.append(input("Dish " + str(en+1) + " Name: "))
    price.append(float(input("Dish " + str(en+1) + " Price ($): ")))
print("======================Happy Restaurant Bill======================")
for res in range(num_dish):  
    pc = str(price[res])
    tx = str(format(float(price[res]*tax/100), '.2f'))
    sr = str(format(float(price[res]*service/100), '.2f'))
    print("Cost For Dish " + str(res+1) + " | " + dishes[res] + " :", pc + ", Tax: " + tx + ", Service: " + sr)
print("Subtotal Per Person: ", format((sum(price) + (sum(price)*(tax+service)/100))/num_pep, '.2f'))
print("Total Cost: ", format(sum(price) + (sum(price)*(tax+service)/100),'.2f'))
print("==================================================================")
print("Thank you for visiting \"Happy Restaurant\"")
print("Come again soon!")
