# Define a custom exception class.
class NegativeNumberError(Exception):
    """Raised when a number is negative."""
    pass

def check_positive(number):
    """
    Raises a NegativeNumberError if the number is negative.
    """
    if number < 0:
        raise NegativeNumberError("The number cannot be negative.")

        # Raises this exception if a given number is negative.
    return "The number is positive or zero."

# Demonstrate the use in a try block.
try:
    print(check_positive(5))
    print(check_positive(-1))
except NegativeNumberError as e:
    print(f"Caught an exception: {e}")