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
- `break`: Exits the loop.  
- `continue`: Skips the current iteration.

---

## 4. Cybersecurity Applications

✔ **Checking User Login Attempts**: Ensuring restricted access after multiple failed logins.  
✔ **Validating IP Addresses**: Matching login IPs with an allow-list using loops and conditions.  
✔ **Generating Employee IDs**: Automating ID creation using while loops.  

