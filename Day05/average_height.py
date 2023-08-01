student_heights = input("Input a list of students heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = sum(student_heights)
print(student_heights)