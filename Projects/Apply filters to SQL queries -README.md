# Apply Filters to SQL Queries  
**Project: Security Analysis Using SQL in MariaDB**

---

## Project Description

In this activity, we investigated potential security issues in the organization's database by writing SQL queries to filter and retrieve specific data. The goal was to identify:

- Failed login attempts  
- Suspicious activity  
- Employee data by department and location  

This process demonstrates the **practical application of SQL** to solve real-world **cybersecurity scenarios**.

---

## Data Schema

### `log_in_attempts` Table Sample:

| event_id | username | login_date | login_time | country | ip_address  | success |
|----------|----------|------------|------------|---------|-------------|---------|
| 101      | jdoe     | 2022-05-09 | 18:45:00   | USA     | 192.168.1.1 | FALSE   |
| 102      | asmith   | 2022-05-09 | 19:30:00   | Canada  | 192.168.1.2 | FALSE   |
| 103      | bbrown   | 2022-05-09 | 22:15:00   | Mexico  | 192.168.1.3 | FALSE   |
| 104      | mjones   | 2022-05-09 | 20:10:00   | USA     | 192.168.1.4 | FALSE   |

---

### `employees` Table Sample:

| employee_id | device_id | username | department         | office  |
|-------------|-----------|----------|---------------------|---------|
| 101         | D123      | jdoe     | Marketing           | East 1  |
| 102         | D124      | asmith   | Marketing           | East 2  |
| 103         | D125      | bbrown   | Finance             | West 1  |
| 104         | D126      | mjones   | Sales               | East 3  |
| 105         | D127      | sgreen   | Information Tech    | West 2  |
| 106         | D128      | dperez   | Sales               | East 4  |
| 107         | D129      | lgomez   | Marketing           | East 5  |

---

## SQL Queries & Explanations

### Retrieve After-Hours Failed Login Attempts

```sql
SELECT event_id, username, login_date, login_time, country, ip_address, success  
FROM log_in_attempts  
WHERE success = FALSE  
  AND login_time > '18:00';
```

**Purpose**: Identify unauthorized or unusual login activity after business hours.

---

### Retrieve Login Attempts on Specific Dates

```sql
SELECT event_id, username, login_date, login_time, country, ip_address, success  
FROM log_in_attempts  
WHERE login_date = '2022-05-09'  
   OR login_date = '2022-05-08';
```

**Purpose**: Review login activity on known suspicious days.

---

### Retrieve Login Attempts Outside of Mexico

```sql
SELECT event_id, username, login_date, login_time, country, ip_address, success  
FROM log_in_attempts  
WHERE country NOT LIKE 'MEX%'  
  AND country NOT LIKE 'Mexico%';
```

**Purpose**: Filter out activity originating from Mexico to assess foreign access.

---

### Retrieve Employees in Marketing (East Offices)

```sql
SELECT employee_id, device_id, username, department, office  
FROM employees  
WHERE department = 'Marketing'  
  AND office LIKE 'East%';
```

**Purpose**: Identify Marketing team members working in East region offices.

---

### Retrieve Employees in Finance or Sales

```sql
SELECT employee_id, device_id, username, department, office  
FROM employees  
WHERE department = 'Finance'  
   OR department = 'Sales';
```

**Purpose**: Target roles vulnerable to fraud or phishing attempts.

---

### Retrieve All Employees Not in IT

```sql
SELECT employee_id, device_id, username, department, office  
FROM employees  
WHERE department <> 'Information Technology';
```

**Purpose**: Isolate non-IT employees for focused training or access reviews.

---

## Summary

In this task, I:

- Queried login records and employee data using SQL  
- Applied filters using `WHERE`, `AND`, `OR`, `NOT`, `LIKE`, and `<>` operators  
- Detected after-hours access attempts  
- Segmented data by department, location, and country

---

## Key Skills Demonstrated

- Cybersecurity-aware data querying  
- SQL filtering logic and best practices  
- Threat detection via structured queries  
- Practical use of MariaDB SQL syntax  

This hands-on exercise shows how SQL is a valuable tool for **cybersecurity operations**, enabling accurate detection, audit, and reporting of security-related events.
