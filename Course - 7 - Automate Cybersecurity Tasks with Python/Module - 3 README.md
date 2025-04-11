# Python & Regex: Cybersecurity Automation

#### 1. What is an algorithm?
**Answer:** An algorithm is a set of rules or steps designed to solve a problem or perform a task.

---

### 2. How do you find the length of a string in Python?
**Answer:** Use the `len()` function.  
**Example:**  
```python
len("125")  # Output: 3
```
---

#### 3. How do you convert a string to uppercase in Python?
**Answer:** Use the ```.upper()``` string method.
```python
"bmoreno".upper()  # Output: "BMORENO"
```

---

#### 4. What is the index of the character "e" in the string "network"?
**Answer:** The index is 1. ```(Python uses 0-based indexing.)```

---

#### 5. How do you slice a string in Python?
**Answer:** Use bracket notation ```[start:end]```.
```python
device_id = "u899v381w363"
print(device_id[8:11])  # Output: 'w36'
```

---


#### 6. How do you concatenate two lists in Python?
**Answer:** Use the ```+``` operator.
```python
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list1 + list2)  # Output: [1, 2, 3, 'a', 'b', 'c']
```

---

#### 7. How do you remove an element from a list in Python?
**Answer:** Use ```.remove(value)```.
```python
my_list = [1, 2, 3, 4]
my_list.remove(4)  # List becomes [1, 2, 3]
```

---

#### 8. What does the ```re ``` module do in Python?
**Answer:** It enables working with regular expressions, useful for pattern matching in strings.

---

#### 9. What is a regular expression?
**Answer:**  A regex is a sequence of characters that defines a search pattern (e.g., for validating emails, IPs).

---

#### 10. How do you extract patterns using regex in Python?
**Answer:** Use ```re.findall(pattern, string)``` from the ```re``` module.
```python
import re
re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_file)
```

---

#### 11. What does ```\w+``` match in regex?
**Answer:** Matches one or more alphanumeric characters or underscores.
 - Examples matched: ``` "network", "email123", "9210" ```

---

#### 12. How do you add an item to the end of a list?
**Answer:** Use ``` .append() ```
```python
my_list = [1, 2, 3]
my_list.append("new_item")  # List becomes [1, 2, 3, "new_item"]
```

---
---

## Additional
---
## File Handling & Exception Handling in Python
---

#### How do you open a file in Python?  
**Answer:** Use the built-in `open()` function.  
**Example:**
```python
file = open("example.txt", "r")  # 'r' for read mode
```

---


#### What are the different file modes in Python?
**Answer:**

```'r'``` – Read (default)

```'w'``` – Write (overwrites file)

```'a'``` – Append

```'x'``` – Create (fails if file exists)

```'b'``` – Binary mode

```'t'``` – Text mode (default)

---

#### How do you read content from a file?
**Answer:** Use ```.read()```, ```.readline()```, or ```.readlines()```.
Example:

```python
with open("example.txt", "r") as f:
    content = f.read()
```

---


#### How do you write to a file in Python?
**Answer:** Use ```.write()``` method with ```'w'``` or ```'a'``` mode.
 - Example:

```python
with open("example.txt", "w") as f:
    f.write("Hello, world!")
 ```

---


#### What is the use of ```with open()``` statement?
**Answer:** It automatically closes the file after the block is executed, even if an error occurs.

#### What is exception handling?
**Answer:** It's a way to handle runtime errors and continue program execution using ```try```, ```except```, and ```finally```.

---

#### How do you handle exceptions in Python?
**Answer:** Use a ```try-except``` block.
 - Example:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

#### What is the purpose of ```finally``` block?
**Answer:** Code inside finally always runs, whether an exception occurs or not.

---

#### How do you raise your own exceptions?
**Answer:** Use the ```raise``` keyword.
 - Example:

```python
raise ValueError("Invalid input")
```

---

#### What is the use of else in exception handling?
**Answer:** The ```else``` block runs only if no exceptions occur in the ```try``` block.

---
