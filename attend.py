attendance_record = []

def take_atten(student_id):
    if student_id in attendance_record:
        print("Student with ID {} is already marked present.".format(student_id))
    else:
        attendance_record.append(student_id)
        print("Student with ID {} marked present.".format(student_id))



def view_atten():
    print("Attendance Record:")
    if not attendance_record:
        print("No students marked present yet.")
    else:
        for student_id in attendance_record:
            print("Student ID: {}".format(student_id))



def main():
    while True:
        print("Mark Attendance (Press 1)")
        print("View Attendance (Press 2)")

        choice = input("Enter your choice: ")



        if choice == '1':
            try:
                id = int(input("Enter an integer: "))
            except ValueError:
                input("Invalid input. Please enter an integer: ")
            
            take_atten(id)
        elif choice == '2':
            view_atten()
        else:
            print("Invalid choice. Please enter a valid option.")



if __name__ == "__main__":
    main()
