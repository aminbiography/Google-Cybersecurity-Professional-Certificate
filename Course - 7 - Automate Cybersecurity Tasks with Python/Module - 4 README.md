# Python Handbook for Cybersecurity Automation

---

## File Handling in Python

#### 1. How do you open a file in Python and ensure it closes properly after you're done?  
**Answer:** Use the `with` statement, which handles file opening and ensures automatic closure.

```python
with open("logs.txt", "r") as file:
    content = file.read()
```

#### 2. What are the different file modes in Python's `open()` function?  
**Answer:**

- `"r"` – Read (default)  
- `"w"` – Write (overwrites existing content)  
- `"a"` – Append (adds to the end of file)  
- `"r+"` – Read and write  

---

## String and List Operations

#### 3. How can you convert a string of usernames into a list?  
**Answer:** Use `.split()`:

```python
usernames = "elarson jsoto abernard".split()
```

#### 4. How do you combine a list of strings into a single string?  
**Answer:** Use `.join()`:

```python
",".join(["elarson", "jsoto", "abernard"])
```

---

## Regular Expressions

#### 5. What is the purpose of `re.findall()` in Python?  
**Answer:** It returns all non-overlapping matches of a pattern in a string.

```python
import re
re.findall(r"\d+", "IP 192.168.1.100")  # ['192', '168', '1', '100']
```

#### 6. Explain the following regex patterns:  
**Answer:**

- `\d` – Match a digit  
- `\s` – Match a space  
- `\w` – Match an alphanumeric character or underscore  
- `+` – One or more of the preceding  
- `*` – Zero or more of the preceding  
- `{3}` – Exactly 3 occurrences  

---

## Debugging & Errors

#### 7. What are the main types of errors in Python?  
**Answer:**

- **Syntax Error** – Invalid Python syntax  
- **Logic Error** – Code runs but gives wrong output  
- **Exception** – Runtime error (e.g., `IndexError`, `TypeError`)  

#### 8. How do you handle logic errors during debugging?  
**Answer:**

- Use `print()` statements to trace variables  
- Use a debugger with breakpoints  
- Read output and check the flow of code carefully  

---

## Loops and Conditional Logic

#### 9. What is the difference between `if`, `elif`, and `else` in Python?  
**Answer:**

- `if` – First condition to check  
- `elif` – Additional condition, checked only if previous ones are false  
- `else` – Catches anything not caught by previous conditions  

#### 10. How do you iterate over a list and break the loop early?  
**Answer:**

```python
for user in users:
    if user == "unauthorized":
        break  # Exit loop early
```

---

## Functions in Python

#### 11. How do you define a reusable function in Python?  
**Answer:**

```python
def greet(name):
    return "Hello " + name
```

#### 12. What is the difference between a parameter and an argument?  
**Answer:**

- **Parameter:** Variable listed in the function definition  
- **Argument:** Actual value passed to the function when calling it  

---

## List Comprehension in Python

#### 13. What is List Comprehension?  
**Answer:** List comprehension is a concise way to create lists in a single line of code, often replacing longer `for` loops.

---

### Syntax

```python
[expression for item in iterable if condition]
```

---

### Basic Example

```python
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]
```

---

### Cybersecurity Use Case: Filter Failed Login Attempts

```python
login_attempts = [200, 401, 403, 200, 401, 500]
failed = [code for code in login_attempts if code != 200]
# Output: [401, 403, 401, 500]
```

---

### Cleaning Data Example

```python
log_entries = ["allow", "deny", "", "allow", None, "deny"]
cleaned = [entry for entry in log_entries if entry]
# Output: ['allow', 'deny', 'allow', 'deny']
```

---

### Why Use List Comprehension?

-  More readable than traditional loops  
-  Faster execution  
-  Cleaner code, especially for filtering or transforming lists  

---

