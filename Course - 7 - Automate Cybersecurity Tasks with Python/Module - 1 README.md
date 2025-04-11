# Cybersecurity Python: Key Concepts

## Why choose Python for automation?
✔ Python is easy to read and resembles human language.  
✔ Python follows standard coding guidelines.  
✔ Python has strong online support.  

### Python in Cybersecurity:
✔ Log analysis  
✔ Malware analysis  
✔ Access control management  
✔ Intrusion detection  
✔ Compliance checks  
✔ Network scanning  

---

## 1. Basics of Python

### Programming & Automation  
Automating repetitive tasks using Python.  

### Variables  
Containers that store data for processing.

```python
x = 10         # Integer
y = 3.14       # Float
name = "John"  # String
is_active = True  # Boolean
```

### Additional Data Types

- **Tuple**: Immutable collection, defined using `()`.  
  Example: `("wjaffrey", 13, True)`  
- **Dictionary**: Key-value pairs, defined using `{}`.  
  Example: `{1: "East", 2: "West"}`  
- **Set**: Unordered collection of unique values, defined using `{}`.  
  Example: `{"jlanksy", "drosas", "nmason"}`  

### Data Structures

```python
my_list = [1, 2, 3]           # List
my_tuple = (1, 2, 3)          # Tuple
my_set = {1, 2, 3}            # Set
my_dict = {"a": 1, "b": 2}    # Dictionary
```

---

## 2. Conditional Statements

- **if, elif, else**: Execute code based on conditions.  
- **Comparison Operators**: `==, !=, >, <, >=, <=`  
- **Logical Operators**: `and, or, not`  

### Example:

```python
x = 7

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

Or,
```
failed_attempts = 4
  if failed_attempts > 3:
    print("Account Locked")
```

---


## 3. Iterative Statements (Loops)
### **Creating Loops in Python**
Loops help automate repetitive tasks. Python supports:
**For loops** - Used when iterating over a known sequence (lists, strings, ranges).  
**While loops** - Used when repeating an action until a condition is met.

### **For Loop**: Iterates over sequences (lists, strings, range).  

```python
for i in range(3):
    print("Connection Failed")
```

### **While Loop**: Runs as long as a condition is True.  

```python
count = 1
while count < 5:
    print("Warning")
    count += 1
```

### **Loop Control:**
- `break`: Break: Exits the loop early when a condition is met.  
- `continue`: Skips the current iteration and proceeds to the next.

---

### **Break: Exits the loop early when a condition is met.**

```python
# print("\n--- Break: Exits the loop early when a condition is met ---")

for i in range(10):
    if i == 5:
        break  # Stops the loop at 5
    print(i)
```


### Continue: Skips the current iteration and proceeds to the next.
```python
# print("\n--- Continue: Skips the current iteration and proceeds to the next ---")

for i in range(5):
    if i == 3:
        continue  # Skips printing 3
    print(i)
```

## 4. Cybersecurity Applications

✔ **Checking User Login Attempts**: Ensuring restricted access after multiple failed logins.  
✔ **Validating IP Addresses**: Matching login IPs with an allow-list using loops and conditions.  
✔ **Generating Employee IDs**: Automating ID creation using while loops.  


---
---

## Additional Compleate Concepts 

# 1. Variables & Data Types
```Python
x = 10         # Integer
y = 3.14       # Float
name = "John"  # String
is_active = True  # Boolean
```
---

# 2. Data Structures
```Python
my_list = [1, 2, 3]           # List
my_tuple = (1, 2, 3)          # Tuple
my_set = {1, 2, 3}            # Set
my_dict = {"a": 1, "b": 2}    # Dictionary
```
---

# 3. Conditional Statements
```Python
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

---

# 4. Loops
```Python
for i in range(5):
    print(i)  # 0 to 4

while x > 0:
    print(x)
    x -= 1
```

---

# 5. Functions
```Python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

# 6. Classes & Objects
```Python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hi, I'm {self.name}!"

p = Person("Bob")
print(p.say_hello())
```

---

# 7. File Handling
```Python
with open("file.txt", "w") as f:
    f.write("Hello, World!")

with open("file.txt", "r") as f:
    print(f.read())
```
---

# 8. Exception Handling
```Python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
---

# 9. List Comprehension
```Python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```
---

# 10. Importing Modules
```Python
import math
print(math.sqrt(16))  # 4.0
```
---
---

