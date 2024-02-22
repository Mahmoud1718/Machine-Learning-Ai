# Create a simple class named Calculator
class Calculator:
    def __init__(self):
        print("Welcome to the Calculator!")

    def sum(self, x, y):
        return x + y

    def mull(self, x, y):
        return x * y

# Take an object from the Calculator class
calc_obj = Calculator()

# Explain in a few words why we call 'self' in methods:
# The 'self' parameter is a convention in Python and represents the instance of the class. 
# It allows methods to access and modify the object's attributes.

# Explain the four pillars of OOP:
# - Encapsulation: Bundling data and methods that operate on that data into a single unit (class).
# - Abstraction: Hiding the complex implementation details and showing only the necessary features.
# - Inheritance: Allows a class to inherit properties and behavior from another class.
# - Polymorphism: Objects of different classes can be treated as objects of a common base class.

# Explain why we use OOP in our code:
# OOP provides a modular and structured way to design and organize code. It promotes code reuse, making it easier to maintain, understand, and scale.

# Create a new class named SciCalc inheriting from Calculator
class SciCalc(Calculator):
    def power(self, x, y):
        return x ** y

# Take an object from the SciCalc class
sci_calc_obj = SciCalc()

# After inheriting, the SciCalc class has access to the methods of the Calculator class without the need to rewrite them.
# The unnecessary code (constructor and sum, mull methods) is removed from the SciCalc class, as it inherits those from Calculator.
