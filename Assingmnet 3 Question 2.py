def calculate_average(*args):
    """
    Calculates the average of a variable number of numbers.

    Args:
        *args: A variable number of numeric arguments.

    Returns:
        The average of the numbers. Returns 0 if no numbers are provided.
    """
    if not args:
        return 0
    return sum(args) / len(args)

# Example:
average1 = calculate_average(10, 20, 30, 40)
print(f"The average of 10, 20, 30, and 40 is: {average1}")

average2 = calculate_average(5, 10, 15)
print(f"The average of 5, 10, and 15 is: {average2}")