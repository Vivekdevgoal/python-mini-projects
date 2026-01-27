import os 
import json 

cont_file= "contact.json"
cont = {}

def load_contact():
    global cont
    if os.path.exists(cont_file):
        with open(cont_file,'r') as cf:
            cont = json.load(cf)

def save_contact():
    with open(cont_file,'w') as cf:
        json.dump(cont, cf, indent = 4)

def add_contact():
    name = input("contact name:")
    phone = input("contact phone number:")
    email = input("contact email id: ")

    cont[name] = { "phone" : phone, "email" : email}
    save_contact()
    print("contact saved successfuly.")

def view_contact():
    if not cont:
        print("no contact yet.")
        return
    
    for name, info in cont.items():
        print(f"\tname = {name}")
        print(f"\tphone number = {info['phone']}")
        print(f"\temail id ={info['email']}")  
        print("\t**********************")

def delete_contact():
    global cont
    name = input("enter the name to delete the contact: ")

    if name not in cont:
        print("no contact to delete.")
        return
    
    if name in cont:
        del cont[name]
        save_contact()
        print("contact deleted successfully.")
        
def main():
    load_contact()
    while True:
        print("*****list of tasks*****")
        print("1. add contact to list.")
        print("2. view contact list.")
        print("3.delete contact from list.")
        print("4. exit from contact list.")

        choice = input("enter correct task no. to implement: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contact()

        elif choice == "3":
            delete_contact()

        elif choice == "4":
            print("existing from contact.")
            break

        else:
            print("enter the correct task number from menu.")
    
if __name__ == "__main__":
    main()
