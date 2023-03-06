"""
New User:
(Registration)
- Print welcome message
- Take user input: username & Password - confirm password
- Ask user to login with given credentials
- login the user
- print logged in message

(Sign In)
- enter username and password
- Validate the data given
- log in user or retry with credentials.

(Update)
- update either username or password *change
- Password reset
"""
import re
import json

def to_json(username, password):
    """Save data to a json file"""
    credentials = {
                'username': username,
                'password': password
    }
    json_string = json.dumps(credentials)

    filename = 'pass.json'
    with open(filename, 'r+') as jsonFile:
        # First we load existing data into a dictionary
        file_data = json.load(jsonFile)
        # Join new_data with file_data inside users
        file_data["users"].append(credentials)
        # sets jsonFile current position at offset
        jsonFile.seek(0)
        # convert back to json.
        json.dump(file_data, jsonFile, indent = 4)
    jsonFile.close()

def from_json(filename='pass.json'):
    """Load data from json file
    Return - a dictionary containing data
    """
    with open(filename, 'r') as jsonFile:
        file_data = json.load(jsonFile)
        return file_data


def update(reg_username, reg_password):
    pass


def sign_in():
    """sign in the user into the system"""

    while True:
        print()
        print("Please log in!")
        print()

        login_username = str(input("Enter username: "))
        login_password = input("Enter password: ")

        def checker(file_data=from_json()):
            """check if user exists
            Return - True if the user exists otherwise False
            """
            file_data = from_json()
            users = file_data['users']

            # create user that will be used for lookup
            user_data = {
                'username': login_username,
                'password': login_password
            }

            for user in users:
                # check if the user combination exists in json
                if all(item in user.items() for item in user_data.items()):
                    return True
                return False


        if checker():
            print()
            print(f"You have successfully logged in as {login_username}")
            break
        else:
            print("Username or password incorrect. Try again!")
            continue


def registration():
    """Signs up new user"""
    print("Please create an account.")
    print()

    reg_username = str(input("Enter username: "))

    while True:
        print()
        reg_password1 = input("Enter password - (Must contain at least 8 characters, Uppercase, lowercase, numbers and special characters): ")
        # password validation
        regex_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if re.match(regex_pattern, reg_password1):
            while True:
                reg_password2 = input("Confirm password: ")

                if reg_password1 == reg_password2:
                    # save credentials to data storage(json)
                    to_json(reg_username, reg_password1)

                    print("You have successfully signed up!")
                    sign_in()
                    break
                else:
                    print()
                    print("Passwords do not match!")
                    continue
            break
        else:
            print("Password Must contain at least 8 characters, Uppercase, lowercase, numbers and special characters")
            continue

# Core of the app
print("Welcome to our app!")
print()

while True:
    answer = str(input("Do you already have an account? (Yes/No) \n (stop to exit): "))

    if answer.lower() == "yes" or answer.lower() == "y":
        sign_in()
        break
    elif answer.lower() == "no" or answer.lower() == "n":
        registration()
        break
    elif answer.lower() == "stop" or answer.lower() == "s":
        print("Thank you for passing by!")
        break
    else:
        print("Please Enter a choice from the given")
        continue
