
# Student Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


def main():

    print("===================================")
    print("       STUDENT GRADE CALCULATOR")
    print("===================================")

    # Get student details
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    subjects = ["Python", "Artificial Intelligence",
                "Mathematics", "English", "Science"]

    marks = []

    # Get marks for each subject
    print("\nEnter Marks (Out of 100)")

    for subject in subjects:

        while True:
            try:
                mark = float(input("Enter marks in " + subject + ": "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks! Enter between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

    # Calculate total and percentage
    total = sum(marks)
    percentage = total / len(subjects)

    # Calculate grade
    grade = calculate_grade(percentage)

    # Check pass or fail
    if all(mark >= 35 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    # Display student result
    print("\n===================================")
    print("          STUDENT RESULT")
    print("===================================")

    print("Student Name :", name)
    print("Roll Number  :", roll_no)

    print("-----------------------------------")
    print("Subject              Marks")
    print("-----------------------------------")

    for i in range(len(subjects)):
        print(subjects[i], ":", marks[i])

    print("-----------------------------------")
    print("Total Marks :", total, "/ 500")
    print("Percentage  :", round(percentage, 2), "%")
    print("Grade       :", grade)
    print("Result      :", result)

    print("===================================")
    print("       THANK YOU!")
    print("===================================")


# Run the program
if __name__ == "__main__":
    main()
