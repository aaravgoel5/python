def calculate_gpa(grades):
    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    total_grade_points = sum(grade_points.get(grade, 0) for grade in grades)
    return total_grade_points / len(grades) if grades else 0.0

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_grade():
    while True:
        grade = input("Enter the grade (A, B, C, D, or F): ").upper()
        if grade in ['A', 'B', 'C', 'D', 'F']:
            return grade
        else:
            print("Invalid grade. Please enter A, B, C, D, or F.")

def main():
    try:
        num_courses = get_positive_integer("Enter the number of courses: ")
        grades = []
        for i in range(num_courses):
            print(f"\nEnter details for course {i + 1}:")
            grade = get_grade()
            grades.append(grade)

        gpa = calculate_gpa(grades)
        print("\nYour GPA is: {:.2f}".format(gpa))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
