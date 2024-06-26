import os
import re

names = {}
phone_num = {}
emails = {}

def add_contact():
    pass
def edit_contact():
    pass
def delete_contact():
    pass
def search_contact():
    pass
def display_contact():
    pass
def export_contact():
    pass

user_name = input("Hello user! May I get your first name? ").capitalize()

user_start = input(f"It's nice to meet you {user_name}. Do you wish to use the Contact Management System? Y/N: ").capitalize()
if user_start == "Y":
    print("\nWelcome to the Contact Management System!\n\tMenu\n\t____\n1. Add Contact\n2. Edit Existing Contact\n3. Delete Contact\n4. Search For a Contact\n5. Display Contacts\n6. Export Contacts\n8. Exit")
    user_choice = input("Please enter a number that corresponse with your inquiry: ")
    match user_choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print(f"Thank you for using the Contact Management System {user_name}! Goodbye")
elif user_start == "N":
    print(f"Have a nice day {user_name}!")
else:
    pass

