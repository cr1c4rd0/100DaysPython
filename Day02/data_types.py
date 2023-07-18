#Data Types

#String
print("Hello")
#Impirimir el primer caracter del string
print("Hello"[0])

#Integer
print(2+5)
#Float
print(3141.59+2.6)
#Boolean
print(True)
print(False)

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit nombre: ")
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
suma = num1+num2
print(two_digit_number[0]+" + "+two_digit_number[1]+" = ", suma)