class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Bark!
print(cat.make_sound())  # Output: Meow!
