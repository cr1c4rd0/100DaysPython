#if condition:
    #if another condition:
        #do this
    #else:
        #do this
#else:
    #do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    print("You can ride rollercoaster!")
    if age < 12:
        print("Please pay $5.")
    elif age <= 18 
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
 