import json

try:
    with open("contact_data.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = []  

def save_data():
   with open("contact_data.json", "w") as file: 
      json.dump(contacts, file)

def add_contact(name, phone_number, email) :
  contact = {"name": name, "phone_number": phone_number, "email": email}
  contacts.append(contact)
  print(name, "added sucessfully ")
  save_data()
  



def view_contact():
  if len(contacts) == 0 :
    print("No contacts yet ")
  
  else:
    for i, contact in enumerate(contacts) :
      print(i + 1, "-", contact["name"], "| phone_number:", contact["phone_number"], "|email:", contact["email"])


def search_contact(name):
  for contact in contacts:
    if contact["name"].lower() == name.lower():
      print("Found:", contact["name"], "|phone_number:", contact["phone_number"], "Email:", contact["email"])
      return
  print(name, "not found ")


def delete_contact(name):
    for contact in contacts: 
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(name, "deleted sucessfully !")
            save_data()
            return
    print(name, " not found")
      
    
while True:
  print("\n===== Contact Book =====")
  print("1. Add contact: ")
  print("2. View all contacts: ")
  print("3. Search contact: ")
  print("4. Delete contact: ")
  print("5. Exit: ")

  choice = input("\nChoose an option: ")

  if choice == "1" :
       while True:
          try:
              name = input("Enter contact name: ")
              phone_number = int(input("Enter phone number: "))
              email = input("Enter email address: ")
              add_contact(name, phone_number, email)
              break
          except ValueError:
             print("Invalid input! Phone number must be digits only. Try again! ")

  elif choice == "2" :
    view_contact()

  elif choice == "3" :
    name = input("Enter contact name to search:  ")
    search_contact(name)

  elif choice == "4" :
    name = input("Enter contact name to delete: ")
    delete_contact(name)  

  elif choice == "5" :
     print("Goodbye") 
     break  
  else:
     print("Invalid option, please choose 1 - 6")
        



  

      
