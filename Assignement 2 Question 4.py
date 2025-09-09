# Class for a Dog
class Dog:
    def make_sound(self):
        return "Woof!"

# Class for a Cat
class Cat:
    def make_sound(self):
        return "Meow!"

# A function that works with any object that has a make_sound() method
def process_sound(sound_object):
    print(f"The animal says: {sound_object.make_sound()}")

# Example usage
dog = Dog()
cat = Cat()

# The same function works for both types of objects
process_sound(dog)
process_sound(cat)