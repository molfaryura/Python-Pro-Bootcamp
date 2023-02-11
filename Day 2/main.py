print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

result = "{:.2f}".format((bill + bill * perc / 100) / people)

print(f"Each person should pay ${result}")
