n=int(input("Enter cost in cents:"))
change=100-n
quarters=int(change//25) # 1 quarters=25 cents
dimes=int((change-25*quarters)//10) # 1 dime=10 cents
pennies=int((change-25*quarters-10*dimes)) # 1 penny=1 cent
print(quarters,"quarters")
print(dimes,"dimes")
print(pennies,"pennies")
