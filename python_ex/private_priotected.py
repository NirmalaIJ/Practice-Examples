'''Python implements encapsulation is through the use of access modifiers for class attributes and methods
Encapsulation is the idea of hiding the internal details of an object and exposing only the necessary information to the outside world
private attributes are denoted by a double underscore prefix before the attribute name (e.g. __private_attribute). The idea behind private attributes is that they can only be accessed within the class and should not be accessed from outside the class

private attributes is that they can only be accessed within the class and should not be accessed from outside the class
it is important to note that the double underscore syntax is just a convention and not a strict rule'''


class Person:
    def __init__(self, name, age):
        self.__private_attribute = 'This is a private attribute.'
        self.name = name
        self.age = age

person = Person('John Doe', 30)
print(person.__private_attribute)  # AttributeError: 'Person' object has no attribute '__private_attribute'



# is to create a method (a class function) that would return the value of the __private_attribute:

class Person:
    def __init__(self, name, age):
        self.__private_attribute = age
        self.name = name
        
    def get_private_attribute(self):
        return self.__private_attribute

person = Person('John Doe', 30)
print(person.get_private_attribute())  # 30
print(person.__private_attribute)      # AttributeError: 'Person' object has no attribute '__pri

#This protects the private attribute from being accidentally or intentionally modified from outside the class, maintaining the integrity of the class
#Protected Attributes in Python Classes
#Protected attributes in Python are denoted by a single underscore prefix before the attribute name (e.g. _protected_attribute). The idea behind protected attributes is similar to private attributes, in that they should not be accessed directly from outside the class. However, unlike private attributes, protected attributes can be accessed from within subclasses



class Person:
    def __init__(self, name, age):
        self._protected_attribute = 'This is a protected attribute.'
        self.name = name
        self.age = age


class Employee(Person):
    def display_protected_attribute(self):
        print(self._protected_attribute)


employee = Employee('Jane Doe', 25)
employee.display_protected_attribute()  # This is a protected attribute.
print(employee._protected_attribute)    # This is a protected attribute.



#Private Methods in Classes
#Just like private attributes, private methods in Python are denoted by a double underscore prefix before the method name (e.g. __private_method). Private methods are meant to be used only within the class and should not be accessed from outside the class:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __private_method(self):
        print('This is a private method.')

person = Person('John Doe', 30)
person.__private_method()        # AttributeError: 'Person' object has no attribute '__private_method'

#Just like private attributes, attempting to access private methods from outside the class results in an AttributeError.

