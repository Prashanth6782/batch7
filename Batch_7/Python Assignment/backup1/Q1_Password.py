import re
# Import the regex library
def check_password_strength(password):
    
    """
    Check the strength of a password based on the following criteria:
    - Minimum length: 8 characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit (0-9)
    - Contains at least one special character (e.g., !, @, #, $, %)
    
    Args:
    password (str): The password string to check.
    
    Returns:
    tuple: A boolean indicating the strength of the password and a message detailing any issues.
    """
    
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character (e.g., !, @, #, $, %)."
    
    return True, "The password is strong."

def main():
    print("Password must meet the following criteria:")
    print("- Minimum length: 8 characters")
    print("- Contains both uppercase and lowercase letters")
    print("- Contains at least one digit (0-9)")
    print("- Contains at least one special character (e.g., !, @, #, $, %)")
    
    password = input("\nEnter a password to check its strength: ")
    
    is_strong, message = check_password_strength(password)
    
    print(message)

if __name__ == "__main__":
    main()