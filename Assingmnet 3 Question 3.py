def get_number_with_error_handling():
    """
    Prompts the user for a number and handles ValueError exceptions.
    """
    while True:
        try:  # Use a try block to catch ValueError exceptions.
            number = int(input("Please enter a number: "))
            return number
        except ValueError:
            # Print an error message and prompt the user again.
            print("Your input is Invalid. Enter a valid number.")

# Example :
valid_number = get_number_with_error_handling()
print(f"You entered the valid number: {valid_number}")