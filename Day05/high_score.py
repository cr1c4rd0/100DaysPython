students_scores = input("Input a list of students scores: ").split()
print(type(students_scores))
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)

# min funcion para sacar el valor mínimo de una lista
print(min(students_scores))

#Utilizando for 
highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest socre in the class is: {highest_score}")
