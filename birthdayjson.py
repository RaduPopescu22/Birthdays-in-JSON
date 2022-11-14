import json

class Birthdays:
    def __init__(self):
        # The standard list of birthdays of our database
        self.birthdays = {"Albert Einstein": "14.03.1879" , "Ada Lovelace":"10.12.1815" , "Benjamin Franklin":"17.01.1706"}
    # Function that returns the desired person's b-day
    def find_bday(self):
        name = input("What is the name of the person?\n")
        with open("birthday.json", "r") as f:
            info = json.load(f)
        try:
            return info[name]
        except KeyError:
            print("There is no such name in our database!")
    # Function to show all the registered birthdays in our database
    def check_bday(self):
        with open("birthday.json", "r") as f:
            info = json.load(f)
        print(f"We have the following b-days registered {info}")
    # Function to add anybody's birthday to our database
    def add_bday(self):
        name = input("What is the name of the person you want to add?\n")
        bday = input("What is their birthday date?\n")
        self.birthdays[name] = bday
        with open("birthday.json" , "w") as f:
            json.dump(self.birthdays,f)
        print("Your submission has been added to the database!")
    # Function to remove a person
    def remove_bday(self):
        name = input("What is the name of the person you want to remove?\n")
        with open("birthday.json", "r") as f:
            info = json.load(f)
        del info[name]
        with open("birthday.json" , "w") as f:
            json.dump(info,f)
        print("{} has been removed!".format(name))


bday = Birthdays()
response = ""
# Checking if birthday.json already exists in order to avoid overwriting user added birthdays
# everytime the program is open, if not, creating one and adding the standard b-day list of our database
try:
    with open("birthday.json" , "r") as j:
        pass
except FileNotFoundError:
    with open("birthday.json" , "w") as f:
        json.dump(bday.birthdays,f)

while response != "q":
    # Applying the function's based on the users choice
    response = input("Please choose between adding, finding, removing or checking for a birthday:\n")
    r = response.lower()
    if r == "add":
        bday.add_bday()
    elif r == "find":
        print(bday.find_bday())
    elif r == "check":
        bday.check_bday()
    elif r == "remove":
        bday.remove_bday()


