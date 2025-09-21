def divide_numbers(numerator, denominator):
    """
    Divides two numbers, handling division by zero and type errors.
    """
    try:  # Use a try block to handle exceptions.
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        # Handle division by zero.
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Handle invalid input types.
        print("Error: Invalid input types. Please provide numbers.")

# Example :
print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"'a' / 2 = {divide_numbers('a', 2)}")