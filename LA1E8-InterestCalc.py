amount=int(input("Input Your Amount: "))
rate=float(input("Input Your Interest Rate (%): "))
year=input("Input Number of Year/s: ")
num_year=int(year)
print("After",year,"Years, Your Balance Will Be:", int(amount*(1+rate/100)**num_year))
