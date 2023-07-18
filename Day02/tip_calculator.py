print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
many_people = int(input("How many people to split the bill? "))

#Calculation
total = (((percentage * bill) / 100) + bill ) / many_people
total = round(total, 2)
print("Each person should pay: $", total)