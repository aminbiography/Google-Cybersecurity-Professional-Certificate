# Advanced Linux Command Guide for Cybersecurity Analysts

## Authentication & Authorization

### 1: What is the difference between authentication and authorization?
**Answer:**  
- **Authentication** verifies **who someone is**.  
- **Authorization** determines **what resources a user can access**.

---

## User & Permission Management

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

## File Navigation & Management

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

## Help & Documentation

### 10: What does the ```man``` command do?
**Answer:**
Displays manual pages for Linux commands, including their usage and options.

---

### 11: What does the ```whatis``` command do?
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

## More CLI

### 14: How do you view the current user you're logged in as?
**Answer:**
```bash
whoami
```

---

### 15: How do you view your current working directory?
**Answer:**
```bash
pwd
```

---

### 16: How do you create a new directory?
**Answer:**
```bash
mkdir directory_name
```

---

### 17: How do you delete a file or directory?
**Answer:**
- Delete a file:
```bash
rm filename.txt
```
- Delete an empty directory:
```bash
rmdir foldername
```

---

### 18: How do you search for a file?
**Answer:**
```bash
find /path -name "filename"
```

---

### 19: How do you read a file one page at a time?
**Answer:**
```bash
less filename.txt
```

---

## Cybersecurity Context

- **Principle of Least Privilege:** Only assign the minimal permissions needed.
- **Avoid logging in as root directly.** Use ```sudo``` instead for traceability and safety.
- **Audit user access regularly** using tools like ```last```, ```who```, or ```checking /etc/passwd```.

---

## Filesystem Hierarchy Awareness (High-Level)

- ```/etc``` – config files

- ```/home``` – user home directories

- ```/var/log``` – system logs

- ```/bin, /sbin, /usr/bin``` – system binaries

---
---
