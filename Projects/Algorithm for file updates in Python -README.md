# Portfolio of Mohammad Aminul Islam

## Name:
**Mohammad Aminul Islam**

## Portfolio Title:
**Algorithm for File Updates in Python**

---

## Professional Summary

My name is **Mohammad Aminul Islam**, and I specialize in **cybersecurity** and **web development**, with a focus on **automation**, **security compliance**, and **access control**. In a recent project, I developed an **automated Python algorithm** that efficiently manages and updates an **IP address allow list**, enhancing access control for restricted networks.

I am skilled in **programming**, **problem-solving**, and **analytical thinking**, and I am dedicated to securing organizational data by automating routine tasks, such as removing unauthorized access and maintaining compliance with security policies.

My expertise in **cloud and web security** enables me to strengthen an organization’s security posture, ensuring the **confidentiality, integrity, and availability** of critical systems. I aim to leverage my skills to help organizations **protect sensitive information** from emerging threats and continuously improve their security infrastructure.

---

## Project Description

In this project, I developed a **Python algorithm** to update a security allow list by **removing unauthorized IP addresses**. The allow list contains IP addresses permitted to access a restricted network.

The algorithm:
- Reads the allow list from a file
- Checks for unauthorized addresses from a separate remove list
- Removes them from the allow list
- Updates the file with the revised list

This process **automates access control** and ensures **security compliance**.

---

## Code Walkthrough

### 1. Open the Allow List File

Open the `allow_list.txt` file in read mode using `with open()` to ensure proper handling and automatic closure.

```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    # File is opened for reading
```

## 2. Read File Contents
Read the contents into a string using `.read()`:

```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    ip_addresses = file.read()

print(ip_addresses)  # Display file contents
```

## 3. Convert the String to a List
Convert the string into a list using `.split()` to allow manipulation:

```python
ip_addresses = ip_addresses.split()
print(ip_addresses)  # Verify the conversion
```

## 4. Define the Remove List
List of IPs to be removed from the allow list:

```python
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

for element in remove_list:
    print(element)  # Display elements being checked
```

## 5. Remove Unauthorized IPs
Check and remove IPs from the allow list:

```python
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

print(ip_addresses)  # Display updated list
```

## 6. Update the File with the Revised List
Convert the list back to a string and overwrite the original file:

```python
ip_addresses = "\n".join(ip_addresses)  # Join list elements with new lines

with open(import_file, "w") as file:
    file.write(ip_addresses)  # Overwrite file with updated list
```

## Summary

This Python algorithm automates the process of maintaining an allow list by:

- Reading IP addresses from a file  
- Converting them into a manipulatable list  
- Comparing with a remove list to detect unauthorized IPs  
- Removing unauthorized entries  
- Updating the file with only authorized IPs  

This supports **efficient access control** and ensures **policy compliance** for security teams.

---

## Conclusion

This project demonstrates my ability to develop **automated solutions** that enhance **security operations**.  
The Python algorithm efficiently updates a security allow list by removing **unauthorized IP addresses**, ensuring that only **authorized users** retain access to restricted networks.

By automating these processes:

- Security teams **save time**  
- **Reduce human error**  
- **Maintain compliance** with security protocols  

This project highlights my strengths in:

- **Programming**  
- **Cybersecurity**  
- **Problem-solving**  

I am committed to leveraging my cybersecurity expertise to **develop and implement solutions** that help organizations **protect sensitive data** and **stay ahead of emerging threats**.
