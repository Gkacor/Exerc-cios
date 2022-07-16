student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

height_total = 0
for height in student_heights:
    height_total = height_total + height

student_number = 0
for students in student_heights:
    student_number += 1

average = round(height_total / student_number)
print(average)