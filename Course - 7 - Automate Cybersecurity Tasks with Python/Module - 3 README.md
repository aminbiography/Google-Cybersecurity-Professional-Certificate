```python
# 1. What is an algorithm?
# Answer: An algorithm is a set of rules or steps designed to solve a problem or perform a task.

# 2. How do you find the length of a string in Python?
# Answer: Use the len() function.
len("125")  # Returns 3

# 3. How do you convert a string to uppercase in Python?
# Answer: Use the .upper() string method.
"bmoreno".upper()  # Returns "BMORENO"

# 4. What is the index of the character "e" in the string "network"?
# Answer: The index is 1. (Python uses 0-based indexing.)

# 5. How do you slice a string in Python?
# Answer: Use bracket notation [start:end].
device_id = "u899v381w363"
print(device_id[8:11])  # Output: 'w36'

# 6. How do you concatenate two lists in Python?
# Answer: Use the + operator.
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]

# 7. How do you remove an element from a list in Python?
# Answer: Use .remove(value).
my_list = [1, 2, 3, 4]
my_list.remove(4)  # my_list becomes [1, 2, 3]

# 8. What does the re module do in Python?
# Answer: It enables working with regular expressions, useful for pattern matching in strings.

# 9. What is a regular expression?
# Answer: A regex is a sequence of characters that defines a search pattern (e.g., for validating email formats, IPs).

# 10. How do you extract patterns using regex in Python?
# Answer: Use re.findall(pattern, string).
import re
log_file = "IP: 192.168.0.1 accessed the server"
re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_file)
# Output: ['192.168.0.1']

# 11. What does \w+ match in regex?
# Answer: Matches one or more alphanumeric characters or underscores.
# Examples matched: "network", "email123", "9210"

# 12. How do you add an item to the end of a list?
# Answer: Use .append()
my_list = [1, 2, 3]
my_list.append("new_item")  # my_list becomes [1, 2, 3, 'new_item']
```

