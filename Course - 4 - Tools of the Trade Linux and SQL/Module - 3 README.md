# Authentication & Authorization

### 1: What is the difference between authentication and authorization?
**Answer:**  
- **Authentication** verifies **who someone is**.  
- **Authorization** determines **what resources a user can access**.

---

# User & Permission Management

### 2: What does the `chmod` command do?
**Answer:** 
Changes file or directory **permissions** for user (`u`), group (`g`), or others (`o`).  
**Example:**
```bash
chmod u+w,g-r file.txt
```
- Adds write for user
- Removes read for group

---

### 3: What are the three types of file permissions in Linux?
**Answer:** 
Read (r) – View file contents

Write (w) – Modify file contents

Execute (x) – Run a file (for scripts/programs)

---

### 4: Which commands require sudo or root privileges?
**Answer:** 
- useradd – Add new user
- userdel – Delete a user
- chown – Change file ownership

---

### 5: How do you change file ownership in Linux?
**Answer:**
Use the chown command.
Example:
```bash
sudo chown username filename
```
---

# File Navigation & Management

### 6: What does ```cd ..``` do?
**Answer:**
Navigates up one level in the directory tree.

---

### 7: How do you list all files, including hidden ones, in a directory?
**Answer:**
Use:
```bash
ls -la
```

---

### 8: How do you create a new file from the command line?
**Answer:**
Use:
```bash
touch filename.txt
```

---

### 9: How do you search for a string inside a file?
**Answer:**
Use:
```bash
grep "search_term" filename.txt
```

---

# Help & Documentation

### 10: What does the ```man``` command do?
**Answer:**
Displays manual pages for Linux commands, including their usage and options.

---

## 11: What does the ```whatis``` command do?
**Answer:**
Gives a brief one-line description of a command.

---

### 12: What does the ```apropos``` command do?
**Answer:**
Searches manual page descriptions for keywords, useful when you don’t remember the exact command.

---

### 13: How do you find a command to create a new group in Linux?
**Answer:**
Use:
```bash
apropos create group
```

---
---
