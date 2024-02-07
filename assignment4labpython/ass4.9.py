'''Write a program in python that accepts a string to setup a passwords. Your entered password
must meet the following requirements:
 The password must be at least eight characters long.
 It must contain at least one uppercase letter.
 It must contain at least one lowercase letter.
 It must contain at least one numeric digit.
 Your program should perform this validation.'''

def is_valid_password(password):
   
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False

    return True

user_password = input("Enter your password: \n")

if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")
