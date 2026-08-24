import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS
students(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT, 
       age INTEGER, 
       score REAL
    )    
""")  




def add_student(name, age, score):
    student = {"name": name, "age": age, "score": score}
    cursor.execute("INSERT INTO students (name, age, score) VALUES (?, ?, ?)", (name, age, score))
    conn.commit()
    print(name, "added sucessfully! ")



def view_students() :
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if len(students) == 0:
         print("No student yet! ")
    else :
        for student in students :
            print(student[0], "-", student[1], "Age:", student[2], "| Score:", student[3]) 



def search_student(name):
    cursor.execute("SELECT * FROM students Where name = ?", (name,))
    student = cursor.fetchone()
    if student:
        print("Found:", student[1], "|Age:", student[2], "|Score:", student[3])
    else:
        print(name, "not found!")



def delete_student(name):
            cursor.execute("DELETE FROM students WHERE name = ?", (name,))
            conn.commit()
            print(name, "deleted successfully!")
           



def class_average():
    cursor.execute("SELECT AVG(score) FROM students")
    average = cursor.fetchone()[0]
    if average is None:
        print("No students yet. ")
    else : 
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
        while True :
            try:
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                score = int(input("Enter student score: "))
                add_student(name, age, score)
                break
            except ValueError:
                print("Invalid input! Age and score must be numbers. Try again! ")

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



conn.commit()
