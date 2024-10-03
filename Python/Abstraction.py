from abc import ABC, abstractmethod
#In Python, abstraction is implemented using the abc (Abstract Base Class) module. 
#An abstract class cannot be instantiated and requires derived classes to implement the abstract methods.
# Abstract class
class Animal(ABC):
    
    # Abstract method
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print("This animal is sleeping")
        
# Derived class that implements the abstract method
class Dog(Animal):
    
    def sound(self):
        print("Bark")

# Another derived class that implements the abstract method
class Cat(Animal):
    
    def sound(self):
        print("Meow")
        
# Trying to create an object of the abstract class will raise an error
# animal = Animal()  # This would raise an error

# Objects of derived classes
dog = Dog()
cat = Cat()

dog.sound()  # Output: Bark
cat.sound()  # Output: Meow
dog.sleep()  # Output: This animal is sleeping
