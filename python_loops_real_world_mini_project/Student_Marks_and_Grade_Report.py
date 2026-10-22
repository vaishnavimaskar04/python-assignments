# Student Marks and Grade Report

students = int(input("Enter number of students: "))

total_marks = 0
pass_count = 0
fail_count = 0

for i in range(1, students + 1):

    name = input("\nEnter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Marks must be between 0 and 100.")
    else:

        total_marks = total_marks + marks

        if marks >= 75:
            grade = "A"
            pass_count = pass_count + 1

        elif marks >= 60:
            grade = "B"
            pass_count = pass_count + 1

        elif marks >= 50:
            grade = "C"
            pass_count = pass_count + 1

        elif marks >= 40:
            grade = "D"
            pass_count = pass_count + 1

        else:
            grade = "Fail"
            fail_count = fail_count + 1

        print("Student:", name)
        print("Grade:", grade)

class_average = total_marks / students

print("\n----- Class Summary -----")
print("Class Average:", class_average)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)