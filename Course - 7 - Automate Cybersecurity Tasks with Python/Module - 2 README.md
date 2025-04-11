# Understanding Functions, Modules & Readability in Python

## 1. Functions
- A **function** is a reusable section of code.
- Defined using the `def` keyword, e.g., `def function_name():`.
- Functions can **return** values using the `return` statement.
- **Arguments** are data passed when calling a function.
- **Parameters** are variables listed in the function definition.

---

#### What is a function in Python?
A function is a reusable block of code designed to perform a specific task. Functions help improve code organization, readability, and reduce repetition.

---

#### How do you define a function in Python?

```python
def function_name(parameters):
    # function body
```

---

#### What are parameters and arguments?
- **Parameters** are variables listed inside the parentheses in the function definition.
- **Arguments** are the actual values passed into the function when it is called.

---

#### What is a return statement in Python?
A `return` statement sends data back from a function to the caller and exits the function. It allows the result to be stored or used later.

---
---

## 2. Built-in Functions
Built-in functions are standard Python functions that can be used without importing.

#### Examples:
- `print()` – displays output
- `type()` – returns the data type
- `max()` – returns the largest value
- `min()` – returns the smallest value
- `sorted()` – returns a sorted version of a list

---
---

## 3. Modules & Libraries
- A **module** is a Python file with additional functions, variables, and classes.
- A **library** is a collection of modules.
- The **Python Standard Library** includes useful modules like:
  - `re`, `csv`, `time`, `datetime`, `statistics`

#### What is the difference between a module and a library?
- A **module** is a Python file that contains functions, variables, or classes.
- A **library** is a collection of related modules.

#### How do you import modules or libraries in Python?

```python
import statistics                     # Import entire module
from statistics import mean, median  # Import specific functions
```

---
---

## 4. Comments & Readability

#### What is the purpose of comments in Python?
Comments explain code and improve readability for others (or your future self).

#### Single-line comment:
```python
# This is a comment
```

#### Multi-line comment (docstring):
```python
"""
This function calculates remaining attempts.
"""
```

---

#### What is the PEP 8 style guide?
PEP 8 is Python’s official style guide. It includes recommendations for:
- Code formatting
- Indentation (4 spaces)
- Naming conventions
- Writing clean, readable code

---

#### What is the difference between global and local variables?
- **Global variables** are defined outside functions and accessible throughout the program.
- **Local variables** are defined inside a function and only accessible within that function.

---

#### Why is code readability important in Python?
Readable code is easier to understand, maintain, and debug—especially in collaborative environments. It helps teams work more efficiently and reduces errors.

---

#### How do you calculate the average or median in Python?

```python
import statistics

average = statistics.mean([10, 20, 30])
median = statistics.median([10, 20, 30])
```

---
---

# Additional 
## Python Classes and Objects

#### What is a class in Python?
**Answer:**  
A class in Python is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that the objects created from it will have.

---

#### What is an object in Python?
**Answer:**  
An object is an instance of a class. It is created using the class definition and can access the class's attributes and methods.

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()  # my_dog is an object of the Dog class
my_dog.bark()   # Output: Woof!
```

---


#### What is the __init__ method?
**Answer:**  
The __init__ method is a constructor in Python that is automatically called when a new object is created. It is used to initialize the object's attributes.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)  # Output: Alice
```

---


#### What is the purpose of self?
**Answer:**  
self represents the instance of the class and allows access to its attributes and methods. It must be the first parameter of any method in the class.

#### How do you create a class with multiple attributes and methods?
**Answer:** 
Define them inside the class using __init__ for attributes and separate functions for methods.

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print(f"{self.name} works in {self.department}")
```

---


#### What is inheritance in Python?
**Answer:** 
Inheritance allows a class (child) to inherit the attributes and methods of another class (parent).

```python
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    pass

c = Car()
c.move()  # Output: Moving...
```

---


#### What is method overriding?
**Answer:** 
Method overriding allows a child class to provide a specific implementation of a method already defined in its parent class.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()  # Output: Meow
```

---


#### What is encapsulation?
**Answer:** 
Encapsulation is the practice of hiding the internal state of an object and requiring all interaction to be performed through methods.

#### What is the difference between a class attribute and an instance attribute?
**Answer:** 
 - Class Attribute: Shared by all instances of the class.
 - Instance Attribute: Unique to each instance.

```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
```

---


#### What is the @classmethod and @staticmethod decorator?
**Answer:** 
 - @classmethod: Takes cls as first parameter, used to access class attributes.
 - @staticmethod: Doesn't take self or cls, behaves like a normal function inside a class.

```python
class MyClass:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def greet():
        print("Hello!")
```

---
---
