print("Welcome to our app!")

def registration():
    """Signs up new user"""
    username = str(input("Enter username: "))

    while True:
        password1 = input("Enter password:(Must contain at least 8 characters, Uppercase, lowercase, numbers and special characters)")
        password2 = input("Confirm password: ")

        if password1 == password2:
            print("Please log in!")

            username1 = str(input("Enter username: "))
            password = input("Enter password: ")

            if username == username1 and password == password1:
                print("You have sucessfully logged in!")
                break
            else:
                print("Username or password incorrect. Try again!")

        else:
            continue

registration()


