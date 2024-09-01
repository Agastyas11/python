def compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 365), (365*time)))
    compound_interest = amount - principal
    print(f"\nCompound interest (in days) is ${round(compound_interest, 2)}")
    print(f"Your total is {round((principal + compound_interest), 2)}")


print("Welcome to the compound interest calculator.\n")
UserBalance = int(input("Please input your current balance (in dollars).\n"))
BankRate = int(input("What is the interest rate (in %) for your respective bank?\n"))
AmountOfTime = int(input("Please enter the number of years the money is invested\n"))
print('\n'*10)

compound_interest(UserBalance, (BankRate/100), AmountOfTime)
print(f"-Your Values-\nYour Balance: ${UserBalance}.\nYour Bank's interest rate: {BankRate}%.\nNumber of Years "
      f"Invested: {AmountOfTime} years.")