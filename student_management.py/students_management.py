students = []

def add_student(name, age, score):
    student = {"name": name, "age": age, "score": score}
    students.append(student)
    print(name, "added sucessfully! ")



def view_students() :
    if len(students) == 0:
         print("No student yet! ")
    else :
        for i, student in enumerate(students):
            print(i + 1, "-", student["name"], "| Age:", student["age"], "|Score:", student["score"])    



def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print("Found:", student["name"], "| Age:", student["age"], "| Score:", student["score"])
            return
    print(name, "not found!")



def delete_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(student["name"], "deleted successfully!")
            return
    print(name, "not found!")



def class_average():
    if len(students) == 0:
        print("No students yet!")
    else:
        total = sum(student["score"] for student in students)
        average = total / len(students)
        print("Class average:", average) 


while True:
    print("\n===== Student Management System =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Class average")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        score = int(input("Enter student score: "))
        add_student(name, age, score)

    elif choice == "2":
         view_students()

    elif choice == "3":
        name = input("Enter student name to search: ")
        search_student(name)

    elif choice == "4":
        name = input("Enter student name to delete: ")
        delete_student(name)

    elif choice == "5":
        class_average()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option, please choose 1-6")     


