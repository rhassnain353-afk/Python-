print("----Welcome to the Student Marks Management System----")
marks_data = []
while True:
    print("\nPlease select an option:")
    print("1. Add Student Marks")
    print("2. View Student Marks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        student_name = input("Enter student name: ")
        English_marks = int(input("Enter student marks in English: "))
        math_marks = int(input("Enter student marks in Math: "))
        science_marks = int(input("Enter student marks in Science: "))
        urdu_marks = int(input("Enter student marks in Urdu: "))
        physics_marks = int(input("Enter student marks in Physics: "))

        print(f"English: {English_marks}, Math: {math_marks}, Science: {science_marks}, Urdu: {urdu_marks}, Physics: {physics_marks} marks for {student_name} have been added.")
        print(f"Total marks: {English_marks + math_marks + science_marks + urdu_marks + physics_marks}")
        marks_data.append((student_name, English_marks, math_marks, science_marks, urdu_marks, physics_marks))
    elif choice == '2':
        if marks_data:
            print("\n--- Student Marks ---")
            for name, eng, math, sci, urdu, phys in marks_data:
                print(f"Name: {name}")
                print(f"  English: {eng}")
                print(f"  Math: {math}")
                print(f"  Science: {sci}")
                print(f"  Urdu: {urdu}")
                print(f"  Physics: {phys}")
                print(f"  Total: {eng + math + sci + urdu + phys}")
        else:
            print("No student marks available.")

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")