total = int(input("Bill Total Amount: "))
num_pep = int(input("Number of People: "))
tax = float(input("Tax Rate (%): "))
service = float(input("Service Rate (%): "))
print("Total Amount With Tax and Service:", format(total+(total*(tax+service)/100), '.2f'))
print("Total Amount Per Person With Tax and Service:", format((total+(total*(tax+service)/100))/num_pep, '.2f'))
