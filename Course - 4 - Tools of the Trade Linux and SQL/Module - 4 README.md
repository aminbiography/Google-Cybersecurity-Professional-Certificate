# Linux & SQL For Cybersecurity Analyst

## LINUX & COMMAND LINE

**1. What is the difference between an absolute path and a relative path in Linux?**  
**Answer:**  
An absolute path starts from the root directory (`/`) and shows the complete path to a file or directory. A relative path starts from the current directory.

**2. What is the purpose of the `sudo` command in Linux?**  
**Answer:**  
`sudo` allows a permitted user to execute a command as the superuser (root) or another user, enabling access to administrative privileges.

**3. What are permissions in Linux? How can you view and change them?**  
**Answer:**  
Permissions define read (`r`), write (`w`), and execute (`x`) access for owner, group, and others.  
- To view: `ls -l`  
- To change: `chmod` command (e.g., `chmod 755 filename`)

**4. What is the role of the shell in Linux?**  
**Answer:**  
The shell is a command-line interpreter that lets users interact with the Linux OS by typing commands.

---

## SQL BASICS

**5. What is SQL and why is it important for a security analyst?**  
**Answer:**  
SQL (Structured Query Language) is used to query, manage, and manipulate data stored in relational databases. Analysts use SQL to investigate incidents, analyze logs, and detect anomalies.

**6. What is a primary key in a relational database?**  
**Answer:**  
A primary key is a column (or set of columns) in a table that uniquely identifies each row and cannot be null or duplicated.

**7. What is a foreign key?**  
**Answer:**  
A foreign key is a column in one table that refers to the primary key in another table, used to maintain referential integrity between related tables.

**8. What is the difference between WHERE, HAVING, and GROUP BY in SQL?**  
**Answer:**  
- `WHERE`: Filters rows before aggregation.  
- `GROUP BY`: Groups rows that have the same values.  
- `HAVING`: Filters groups after aggregation.

---

## SQL FILTERING & CONDITIONS

**9. What does the LIKE operator do in SQL?**  
**Answer:**  
`LIKE` is used to search for a specified pattern in a column. `%` is used as a wildcard.  
Example: `name LIKE 'Dr.%'` matches all names starting with "Dr."

**10. How does BETWEEN work in SQL?**  
**Answer:**  
`BETWEEN` filters for values within a range, inclusive of the boundary values.  
Example:  
```sql
date BETWEEN '2023-01-01' AND '2023-03-01';
```

**11. What's the difference between = and != in SQL?**
**Answer:** 
- ```=``` checks for equality
- ```!=``` or ```<>``` checks for inequality

---

## SQL JOINS

**12. What is an INNER JOIN?**
**Answer:** 
Returns only the matching rows between two tables based on a specified condition (usually a shared column).

**13. What is a LEFT JOIN and how is it different from a RIGHT JOIN?**
**Answer:** 
- ```LEFT JOIN``` returns all rows from the left table and matching rows from the right table.
- ```RIGHT JOIN``` returns all rows from the right table and matching rows from the left table.
Non-matching values return ```NULLs```.

**14. What is a FULL OUTER JOIN?**
**Answer:** 
Returns all rows from both tables. If there's no match, the result will contain ```NULLs``` for missing values.

---

## AGGREGATE FUNCTIONS

**15. What are aggregate functions in SQL? Give examples.**
**Answer:** 
Functions that perform calculations on a set of values and return a single result:
- ```COUNT()```: Number of rows
- ```SUM()```: Total of a numeric column
- ```AVG()```: Average
- ```MAX()``` / ```MIN()```: Highest / Lowest value

---

## REAL-WORLD SCENARIOS

**16. How would you find failed login attempts after business hours?**
```sql
SELECT * FROM log_in_attempts  
WHERE login_time > '18:00' AND success = FALSE;
```

**17. How would you find remote employees who made login attempts?**
```sql
SELECT *  
FROM log_in_attempts  
INNER JOIN employees_remote  
ON log_in_attempts.username = employees_remote.username;
```

**18. How would you find all employees who are not in the IT department?**
```sql
SELECT *  
FROM employees  
WHERE department != 'Information Technology';
```

**19. How do you find all login attempts not from Mexico?**
```sql
SELECT *  
FROM log_in_attempts  
WHERE NOT country LIKE 'MEX%';
```

---

## MISCELLANEOUS

**20. What’s the difference between a GUI and CLI?**
- GUI (Graphical User Interface) uses windows, icons, and buttons for interaction.
- CLI (Command Line Interface) requires typing commands. CLI is more powerful for automation and scripting.



