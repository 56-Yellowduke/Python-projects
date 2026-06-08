import json

try:
    with open("product_data.json", "r") as file:
        product_inventory = json.load(file)
except:
    product_inventory = []

def save_data():
    with open("product_data.json", "w") as file:
        json.dump(product_inventory, file)

def add_inventory(name, price, quantity) :
    inventory = {"name": name, "price": price, "quantity": quantity}
    product_inventory.append (inventory)
    print(name, "added sucessfully")
    save_data()


def view_inventory():
    if len(product_inventory)  == 0 :
        print("No product inventory yet")

    else:
        for i, inventory in enumerate(product_inventory):
            print(i + 1, "-", inventory["name"], "|Price:", inventory["price"], "quantity:", inventory["quantity"])       


def search_inventory(name):
    for inventory in product_inventory :
        if inventory["name"]. lower() == name.lower():
            print("Found:", inventory["name"], "|Price:", inventory["price"], "quantity:", inventory["quantity"])    
            return
    print(name, "not found") 


def delete_inventory(name):
    for inventory in product_inventory :
        if inventory["name"].lower() == name.lower():
             product_inventory.remove(inventory)
             print(name, "deleted sucessfully !")
             save_data()
             return
    print(name, "not found!")

while True :
    print("\n ===== Product Inventory =====")    
    print("1. Add contact: ")
    print("2. View all contacts: ")
    print("3. Search contact: ")
    print("4. Delete contact: ")
    print("5. Exit: ")

    choice = input("\nChoose an option: ")

    if choice == "1" :
            name = input("Enter inventory name: ")
            price = int(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            add_inventory(name, price, quantity)

    elif choice == "2" :
            view_inventory()

    elif choice == "3" :
            name = input("Enter inventory name to search: ")
            search_inventory(name)

    elif choice == "4" : 
            name = input("Enter contact name to search: ")
            delete_inventory(name)

    elif choice == "5" :
            print("Goodbye")
            break
    else:
            print("Invalid option, please choose 1 - 6")        




        
   



                
