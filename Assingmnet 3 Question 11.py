import requests
import sqlite3

## API GET Request Example
print("--- API GET Request ---")
try:
    # A public API endpoint for demonstration
    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    # Make the GET request to the API.
    response = requests.get(api_url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        data = response.json()
        print("Successfully retrieved data from the API.")
        print(data)
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API request: {e}")

print("\n--- SQLite Database Operations ---")
try:
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()

        # Corrected CREATE TABLE statement.
        cursor.execute('''CREATE TABLE IF NOT EXISTS products
                          (
                              id
                              INTEGER
                              PRIMARY
                              KEY,
                              name
                              TEXT,
                              price
                              REAL
                          )''')

        products_to_insert = [
            ('Laptop', 1200.50),
            ('Keyboard', 75.00),
            ('Mouse', 25.99)
        ]
        cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products_to_insert)

        conn.commit()
        print("Data inserted and committed successfully.")

        print("\n--- Retrieving data from the 'products' table ---")
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

except sqlite3.Error as e:
    print(f"A SQLite database error occurred: {e}")

