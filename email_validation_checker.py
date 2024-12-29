import re

# Corrected regular expression for email validation
email_condition = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@][a-zA-Z]+\.[a-zA-Z]{2,3}$"

# Taking email input from the user
user_email = input("Enter your email: ")

# Validating the email using the regex
if re.match(email_condition, user_email):
    print("Right email")
else:
    print("Wrong email")
