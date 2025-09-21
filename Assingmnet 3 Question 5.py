# Sample list of Celsius temperatures.
celsius_temps = [0, 8, 25, 39, 40]

# Lambda function for Celsius to Fahrenheit conversion.
# The formula is F = C * 9/5 + 32.
c_to_f = lambda c: (c * 9/5) + 32

# Use map() to apply the lambda function to the list.
fahrenheit_temps = list(map(c_to_f, celsius_temps))

print(f"Celsius temperatures: {celsius_temps}")
print(f"Fahrenheit temperatures: {fahrenheit_temps}")