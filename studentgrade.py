marks = int(input("Enter marks of the student: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)

marks = []

for i in range(5):
    score = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

average = sum(marks) / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average Marks:", average)
print("Grade:", grade)
