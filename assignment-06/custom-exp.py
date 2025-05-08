# Define the custom exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    print("Age is valid")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError:
    print("Please enter a valid number for age")
except InvalidAgeError as e:
    print(f"Invalid age: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")