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
"""
import re

print("Welcome to our app!")
print()

def to_json(username, password):
    pass

def update(reg_username, reg_password):
    pass


def sign_in(reg_username=None, reg_password=None):
    """sign in the user into the system"""

    while True:
        print()
        print("Please log in!")
        print()

        login_username = str(input("Enter username: "))
        login_password = input("Enter password: ")

        if login_username == reg_username and login_password == reg_password:
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
                    print("You have successfully signed up!")
                    sign_in(reg_username=reg_username, reg_password=reg_password1)
                    break
                else:
                    print()
                    print("Passwords do not match!")
                    continue
            break
        else:
            print("Password Must contain at least 8 characters, Uppercase, lowercase, numbers and special characters")
            continue



registration()
