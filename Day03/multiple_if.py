#IF / ELIF / ELSE
#if condition1:
# do A
#elif condition2:
# do B
#else:
# do C

#MULTIPLE IF
#if condition1:
# do A
# if condition2:
# do B
#if condition3:
# do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    print("You can ride rollercoaster!")
    if age < 12:
        bill = 5
        print("Child tickets are pay $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are pay $7.")
    else:
        bill = 12
        print("Adult tickkets are pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        bill += 3
        print(f"YOur final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")