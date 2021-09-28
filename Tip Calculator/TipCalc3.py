num_pep = int(input("How many people are paying? "))
tax = float(input("Tax Rate (%): "))
service = float(input("Service Rate (%): "))
num_dish = int(input("Number of Dishes: "))

dishes = []
price = []
for en in range(num_dish):
    en_number = str(en+1)
    dishes.append(input("Dish " + en_number + " Name: "))
    price.append(float(input("Dish " + en_number + " Price ($): ")))
print("======================Happy Restaurant Bill======================")
for res in range(num_dish):
    res_num = str(res+1)
    pc = str(price[res])
    tx = str(format(float(price[res]*tax/100), '.2f'))
    sr = str(format(float(price[res]*service/100), '.2f'))
    print("Cost For Dish " + res_num + " | " + dishes[res] + " :", pc + ", Tax: " + tx + ", Service: " + sr)
print("Subtotal Per Person: ", format((sum(price) + (sum(price)*(tax+service)/100))/num_pep, '.2f'))
print("Total Cost: ", format(sum(price) + (sum(price)*(tax+service)/100),'.2f'))
print("==================================================================")
print("Thank you for visiting \"Happy Restaurant\"")
print("Come again soon!")
