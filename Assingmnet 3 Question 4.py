names = ["Sara", "Tashinga", "Changetai", "Ngoni"]
file_name = "names.txt"

# Write names to the file.
print(f"Writing names to {file_name}...")
with open(file_name, "w") as file:
    # Use with statement to ensure file is closed.
    for name in names:
        file.write(name + "\n")
        # Each name should be on a new line.

print(f"\nReading names from {file_name}...")
# Read names from the file and print to the console.
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())