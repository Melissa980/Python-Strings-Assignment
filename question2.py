# Question 2 Task 1 

def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Name length validation passed.")

# Example usage:
validate_name_length("John", "Doe") 
validate_name_length("J", "Doe")     

# Question 2 Task 2

def check_password_complexity(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return
    if not any(char.isupper() for char in password):
        print("Error: Password must contain at least one uppercase letter.")
        return
    if not any(char.islower() for char in password):
        print("Error: Password must contain at least one lowercase letter.")
        return
    if not any(char.isdigit() for char in password):
        print("Error: Password must contain at least one number.")
        return
    print("Password complexity check passed.")

# Example usage:
check_password_complexity("Passw0rd")   
check_password_complexity("abc123")     
check_password_complexity("PASSWORD")   

# Question 2 Task 3

import re

def validate_email_format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print("Email format validation passed.")
    else:
        print("Error: Email format is not valid.")

# Example usage:
validate_email_format("example@email.com")   
validate_email_format("invalid-email@")     
