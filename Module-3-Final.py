import os
import re

contact_list = {}

user_name = input("Hello user! May I get your first name? ").capitalize()

def add_contact():
    email_pattern = r"\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}\b"
    ind_num = len(contact_list.keys()) + 1
    user_contact_name = input("Contact's Name: ").title()
    user_contact_number = input("Contact's Phone No.: ")
    user_email = input("Contact's E-mail Address: ")


    if len(user_contact_number) == 10 and user_contact_number.isnumeric() and re.findall(email_pattern, user_email):
        contact_list[f"Contact {ind_num}"] = {"Name" : user_contact_name, "Phone Number" : user_contact_number, "Email Address" : user_email}   

    return f"{user_name}, {user_contact_name}'s contact information was saved."
def edit_contact():
    pass
def delete_contact():
    pass
def search_contact():
    pass

def export_contact():
    pass

user_start = input(f"It's nice to meet you {user_name}. Do you wish to use the Contact Management System? Y/N: ").capitalize()
if user_start == "Y":
    while True:
        print("\nWelcome to the Contact Management System!\n\tMenu\n\t____\n1. Add Contact\n2. Edit Existing Contact\n3. Delete Contact\n4. Search For a Contact\n5. Display Contacts\n6. Export Contacts\n7. Exit")
        try:
            user_choice = int(input("Please enter a number that corresponse with your inquiry: "))
            match user_choice:
                case 1:
                    print(add_contact())
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print(contact_list)
                case 6:
                    pass
                case 7:
                    print(f"Thank you for using the Contact Management System {user_name}! Goodbye")
        except ValueError:
            print(f"{user_name}, please select a number between 1-7...")
elif user_start == "N":
    print(f"Have a nice day {user_name}!")
else:
    pass

