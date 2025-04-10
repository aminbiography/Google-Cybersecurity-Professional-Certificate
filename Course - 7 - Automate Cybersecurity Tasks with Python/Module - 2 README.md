# Understanding Functions, Modules & Readability in Python

## . Functions
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

## Built-in Functions
Built-in functions are standard Python functions that can be used without importing.

#### Examples:
- `print()` – displays output
- `type()` – returns the data type
- `max()` – returns the largest value
- `min()` – returns the smallest value
- `sorted()` – returns a sorted version of a list

---
---

## Modules & Libraries
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

## Comments & Readability

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

### Q11: How do you calculate the average or median in Python?

```python
import statistics

average = statistics.mean([10, 20, 30])
median = statistics.median([10, 20, 30])
```

---
