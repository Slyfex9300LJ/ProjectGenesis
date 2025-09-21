import random

# Generate a list of 10 random integers between 1 and 100.
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Generated numbers: {random_numbers}")

# Calculate the average.
average = sum(random_numbers) / len(random_numbers)

print(f"The average of the numbers is: {average}")