import os
import re

contact_list = {}

user_name = input("Hello user! May I get your first name? ").capitalize()

def add_contact():
    email_pattern = r"\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"
    ind_num = len(contact_list.keys()) + 1
    user_contact_name = input("Contact's Name: ").title()
    user_contact_number = input("Contact's Phone No.: ")
    user_email = input("Contact's E-mail Address: ")

    if len(user_contact_number) == 10 and user_contact_number.isnumeric() and re.findall(email_pattern, user_email):
        contact_list[f"Contact {ind_num}"] = {"Name" : user_contact_name, "Phone Number" : user_contact_number, "Email Address" : user_email}   
        return f"{user_name}, {user_contact_name}'s contact information was saved under Contact {ind_num}."
    elif len(user_contact_number) != 10:
        return f"{user_name}, you entered an invalid phone number..."
    elif user_email != re.findall(email_pattern, user_email):
        return f"{user_name}, you entered an invalid email address..."       

def edit_contact():
    email_pattern = r"\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"
    contact_num = input("Please enter the contact you wish to edit: ").capitalize()

    if contact_num in contact_list.keys():
        found_contact = contact_list[contact_num]
        print("1. Name\n2. Phone Number\n3. Email Address")
        user_choice_1 = int(input("Please select a number for the data you with to revise: "))
        if user_choice_1 == 1:
            contact_name_edit = input("What is the new name of this contact?: ").capitalize()
            found_contact["Name"] = contact_name_edit
            return f"Revision saved"
        elif user_choice_1 == 2:
            contact_phone_edit = input("What is the new phone number of this contact?: ")
            if len(contact_phone_edit) == 10:
                found_contact["Phone Number"] = contact_phone_edit
                return f"Revision saved"
            else:
                return f"{user_name}, you entered an invalid number"           
        elif user_choice_1 == 3:
            contact_email_edit = input("What is the new email address of this contact?: ")
            if re.findall(email_pattern, contact_email_edit):
                found_contact["Email Address"] = contact_email_edit
                return f"Revision saved"
            else:
                return f"{user_name}, you entered an invalid email address"
        else:
            return f"{user_name}, you picked an invalid option..."
        
def delete_contact():
    contact_num = input("Please enter the contact you wish to remove: ").capitalize()
    if contact_num in contact_list.keys():
        contact_list.pop(contact_num)
        return f"{user_name}, {contact_num} was removed successfully"

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
                    print(edit_contact())
                case 3:
                    print(delete_contact())
                case 4:
                    pass
                case 5:
                    if len(contact_list) == 0:
                        print(f"{user_name}, your contact list is empty.")
                    else:
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

