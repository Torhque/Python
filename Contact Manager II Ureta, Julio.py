## Julio Ureta CSC102

##For this assignment you will create a simple class hierarchy.
##You will create an inheritance relationship between two classes
##-- a Friend class and a Person class - Friend will inherit Person.

##Your Person class will have the following attributes:
##    first_name
##    last_name
##    phone_number
class Person():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""

##Both your Person class and your Friend class will have a get_info method.
##
##      For the Person class, the get_info method will return a string
##      with the full name and phone number of the person.
    def get_info(self):
        info = self.first_name + ' ' + self.last_name + "\n"
        info += self.phone_number + "\n"

        return info

##Your Friend class will have the following attributes:
##    email
##    birth_date
class Friend(Person):
    def __init__(self):
        super().__init__()
        self.email = ""
        self.birth_date = ""

    def get_info(self):
        info = super().get_info()
        info += self.email + "\n"
        info += self.birth_date

        return info

def display_main_menu():

##  Display menu for the user, then prompt them for a selection.
    global user_selection
    
    print("Please make a selection.")
    print("1. Add a contact.")
    print("2. Search for a contact by last name.")
    print("3. Exit the program.")

    user_selection = input("Enter 1, 2, or 3: ")
    user_selection = int(user_selection)

    return user_selection

def get_contact_choice():
    
##  Ask the user whether they want to add a normal person or friend.
    global contact_choice
    
    print("1. Add a person.")
    print("2. Add a friend.")

    contact_choice = input("Enter 1 or 2: ")
    contact_choice = int(contact_choice)

    return contact_choice

def add_person():
    
##  Create the person, then prompt the user for name and phone #
    global person
    person = Person()

    first_name_of_person = input("Enter their first name: ")
    person.first_name = first_name_of_person

    last_name_of_person = input("Enter their last name: ")
    person.last_name = last_name_of_person

    phone_number_of_person = input("Enter their phone number: ")
    person.phone_number = phone_number_of_person

    contacts.append(person)

def add_friend():
    
##  Create the friend object, then prompt the user for phone #, email, and birth date.    
    global friend
    friend = Friend()

    first_name_of_person = input("Enter their first name: ")
    friend.first_name = first_name_of_person

    last_name_of_person = input("Enter their last name: ")
    friend.last_name = last_name_of_person

    phone_number_of_person = input("Enter their phone number: ")
    friend.phone_number = phone_number_of_person

    email_of_friend = input("Enter their email: ")
    friend.email = email_of_friend

    birth_date_of_friend = input("Enter their birth date: ")
    friend.birth_date = birth_date_of_friend

    contacts.append(friend)

def search_by_last_name():
    
##  Prompt user for last name to search
    user_input = input("Enter a last name to search for.")

##  Display all the info for contacts that match the last name.
    for name in contacts:
        if user_input.lower() == name.last_name.lower():
            print (name.get_info())
    
def Main():

##  Create list to store the contacts.
    global contacts
    contacts = []
   
    quit_program = False
    
    while(quit_program == False):
        display_main_menu()

        if user_selection == 1:            
            get_contact_choice()

            if contact_choice == 1:                
                add_person()

            elif contact_choice == 2:                
                add_friend()

        elif user_selection == 2:            
            search_by_last_name()

        elif user_selection == 3:
            quit_program = True
            
Main()
