class student:
    def __init__(self, name, age, score):
        self.name = name
        self.age= age 
        self.score = score


    def get_grade(self):
        if self.score >= 70 :
            return "A"
        elif self.score >= 60 :
            return "B"
        elif self.score >= 50 :
            return "C"
        else:
            return "Fail"
        
    def to_dict(self):
        return{"Name": self.name, "Age": self.age, "Score": self.score}    

duke = student("Duke", 22, 85)
print(duke.get_grade())
print(duke.to_dict())


import json 

students = []

try:
    with open("students_oop.json", "r") as file:
            students_data = json.load(file)
except:
    students_data = []      


def save_data():
    with open("students_oop.json", "w") as file:
        json.dump(students_data, file)



def add_student(name, age, score):
    new_student = student(name, age, score)
    students_data.append(new_student.to_dict())
    print(name, "Added successfully!")
    save_data()


def view_students():
    if not students_data:
        print("No students found.")
    else:
        for student in students_data:
            print(student)


def search_student(name):
    for i in students_data:
        if i["Name"].lower() == name.lower():
            print(i)
            return
        

def delete_student(name):
    for i in students_data:
        if i ["Name"].lower() == name.lower():
            students_data.remove(i)
            print(name, "Deleted sucessfully!")
            save_data()


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

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
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
  








 



