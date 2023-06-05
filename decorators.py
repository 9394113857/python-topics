def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "password":
        return True
    else:
        return False

def login_required(func):
    def wrapper(*args, **kwargs):
        if is_authenticated():
            return func(*args, **kwargs)
        else:
            raise ValueError("Access denied. Please login first.")
    return wrapper

@login_required
def restricted_area():
    print("Welcome to the restricted area!")

@login_required
def another_function():
    print("This is another restricted function.")

def is_authenticated():
    return login()

def logout():
    print("Logged out successfully.")

# Main program
while True:
    # Authenticate user
    if is_authenticated():
        print("Login successful.")
        print("Available functions:")
        print("1. restricted_area")
        print("2. another_function")

        # Ask user to choose a function
        chosen_function = input("Enter the function to execute: ")

        # Execute the chosen function
        if chosen_function == "restricted_area":
            restricted_area()
        elif chosen_function == "another_function":
            another_function()
        else:
            print("Invalid function choice.")

        # Ask if the user wants to log out
        logout_choice = input("Do you want to log out? (yes/no): ")
        if logout_choice.lower() == "yes":
            logout()
            break  # Exit the loop and end the program
    else:
        print("Login failed. Access denied.")
        break  # Exit the loop and end the program
