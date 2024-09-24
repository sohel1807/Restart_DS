# Base class for all animals
class Animal:
    def __init__(self):
        # Setting the 'alive' attribute to True, assuming all animals are alive when created
        self.alive = True
      
    # Method to simulate eating behavior for the generic animal
    def eat(self):
        print("Animal is eating")

# Derived class that inherits from Animal
class Dog(Animal):
    # Overriding the 'eat' method to provide specific behavior for a dog
    def eat(self):
        print("Dog is eating")
    
    # Method to check and print if the dog is alive
    def check(self):
        print(self.alive)

# Creating an instance of the Dog class
dog = Dog()

# Calling the check method to see if the dog is alive
dog.check()

# Calling the overridden 'eat' method; this will call Dog's version, not the Animal class version
dog.eat()  

