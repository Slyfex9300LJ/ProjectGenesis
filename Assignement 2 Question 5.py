from abc import ABC, abstractmethod

# Define the ABC
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        """Read method must be implemented by subclasses."""
        pass

    @abstractmethod
    def write(self, data):
        """Write method must be implemented by subclasses."""
        pass

# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        print(f"Reading text from file: {self.filename}")
        # Implementation to read from a text file
        return "text content"

    def write(self, data):
        print(f"Writing '{data}' to text file: {self.filename}")
        # Implementation to write to a text file

# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        print(f"Reading binary data from file: {self.filename}")
        # Implementation to read from a binary file
        return b"binary content"

    def write(self, data):
        print(f"Writing binary data to file: {self.filename}")
        # Implementation to write to a binary file

# Example usage
text_file = TextFileHandler("document.txt")
text_content = text_file.read()
text_file.write("Hello, World!")

print("-" * 20)

binary_file = BinaryFileHandler("image.bin")
binary_content = binary_file.read()
binary_file.write(b"\x00\x01\x02")