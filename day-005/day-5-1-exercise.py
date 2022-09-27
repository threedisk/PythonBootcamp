# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# student_heights =[180, 124, 165, 173, 189, 169, 146]

## CODEBLOCK Untuk menghitung Sum menggunakan for loop
total_height=0
for height in student_heights:
    total_height += height
print(total_height)

## CODEBLOCK Untuk menghitung Len menggunakan for loop
total_student = 0
for student in student_heights:
    total_student += 1
print(total_student)
##
average = total_height / total_student
print(average)
print(round(average))
