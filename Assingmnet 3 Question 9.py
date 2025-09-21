import re

# I. Extract all email addresses from a text[cite: 25].
text = "Contact us at support@example.com or info@domain.org for help."
emails = re.findall(r"\S+@\S+", text)
print(f"Extracted email addresses: {emails}")

# II. Validate a date in "YYYY-MM-DD" format[cite: 26].
date1 = "2025-09-21"
date2 = "21-09-2025"
date_pattern = r"^\d{4}-\d{2}-\d{2}$"
print(f"Is '{date1}' a valid date? {bool(re.match(date_pattern, date1))}")
print(f"Is '{date2}' a valid date? {bool(re.match(date_pattern, date2))}")

# III. Replace all occurrences of a word[cite: 27].
sentence = "The cat sat on the mat. The cat is black."
new_sentence = re.sub(r"cat", "dog", sentence)
print(f"Original sentence: {sentence}")
print(f"Modified sentence: {new_sentence}")

# IV. Split a string by non-alphanumeric characters[cite: 28].
data_string = "Hello, world! How are you? 123"
words = re.split(r"[^a-zA-Z0-9]+", data_string)
print(f"Split words: {words}")