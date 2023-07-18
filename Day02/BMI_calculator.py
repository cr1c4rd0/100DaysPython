#Instructions

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

#BMI = weight(kg) / height**2 (m**2)

get_height = input("Enter your height: ")
get_weight = input("Enter your weight: ")

#Conversion
set_height = float(get_height)
set_weight = int(get_weight)

bmi = int(set_weight / (set_height) ** 2)

print(bmi)