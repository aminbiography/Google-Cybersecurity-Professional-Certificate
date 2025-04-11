# Python Basics: Quick Reference

## File Handling in Python

**## 1. How do you open a file in Python and ensure it closes properly after you're done?
**Answer:**  Use the `with` statement, which handles file opening and ensures automatic closure.

```python
with open("logs.txt", "r") as file:
    content = file.read()
```

#### 2: What are the different file modes in Python's open() function?  
**Answer:** 

- `"r"` – Read (default)
- `"w"` – Write (overwrites existing content)
- `"a"` – Append (adds to the end of file)
- `"r+"` – Read and write

---

## String and List Operations

#### 3. How can you convert a string of usernames into a list?
**Answer:**  Use `.split()`:

```python
usernames = "elarson jsoto abernard".split()
```

#### 4. How do you combine a list of strings into a single string?
**Answer:**   Use `.join()`:

```python
",".join(["elarson", "jsoto", "abernard"])
```

---

## Regular Expressions

#### 5. What is the purpose of `re.findall()` in Python?  
**Answer:**  It returns all non-overlapping matches of a pattern in a string.  
Example:

```python
import re
re.findall(r"\d+", "IP 192.168.1.100")  # ['192', '168', '1', '100']
```

#### 6. Explain the following regex patterns: 
**Answer:** 

- `\d`: Match a digit  
- `\s`: Match a space  
- `\w`: Match alphanumeric character or underscore  
- `+`: One or more of the preceding  
- `*`: Zero or more of the preceding  
- `{3}`: Exactly 3 occurrences  

---

## Debugging & Errors

#### 7: What are the main types of errors in Python?
**Answer:** 

- **Syntax Error** – Invalid Python syntax  
- **Logic Error** – Code runs but gives wrong output  
- **Exception** – Runtime error (e.g., `IndexError`, `TypeError`)  

#### 8: How do you handle logic errors during debugging?  
**Answer:** 

- Use `print()` statements to trace variables  
- Use a debugger with breakpoints  
- Read output and check flow of code carefully  

---

## Loops and Conditional Logic

#### 9: What is the difference between `if`, `elif`, and `else` in Python?
**Answer:** 

- `if`: First condition to check  
- `elif`: Additional condition, only checked if previous `if` or `elif` is False  
- `else`: Catches anything not caught above  

#### 10: How do you iterate over a list and break the loop early?
**Answer:** 

```python
for user in users:
    if user == "unauthorized":
        break  # Exit loop early
```

---

## Functions in Python

#### 11: How do you define a reusable function in Python?
**Answer:** 

```python
def greet(name):
    return "Hello " + name
```

#### 12: What is the difference between a parameter and an argument?
**Answer:** 

- **Parameter:** Variable listed in function definition  
- **Argument:** Actual value passed to function  

