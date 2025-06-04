# Access Control, Encryption, Hashing, IAM & Monitoring in Cybersecurity

---

## Access Control & Authentication

### 1: What is the difference between authentication and authorization?
**Answer:**
- **Authentication**: Verifies *who* a user is (e.g., username/password).  
- **Authorization**: Determines *what* the user is allowed to access or do.

---

### 2: What are the three factors of authentication?
**Answer:**
1. **Knowledge** – Something the user *knows* (e.g., password, PIN)  
2. **Ownership** – Something the user *has* (e.g., OTP, smart card)  
3. **Characteristic** – Something the user *is* (e.g., fingerprint, facial scan)

---

### 3: What is Single Sign-On (SSO), and what are its benefits?
**Answer:** 
SSO allows users to log in once and access multiple systems.

**Benefits:**  
- Improves user experience  
- Reduces password fatigue  
- Minimizes attack surfaces  

---

### 4: What is Multi-Factor Authentication (MFA) and why is it important?
**Answer:** 
MFA requires two or more verification methods. It protects against unauthorized access from compromised credentials.

---

## Encryption & Hashing

### 5: What's the difference between symmetric and asymmetric encryption?
**Answer:**
- **Symmetric encryption**: Uses one secret key (e.g., AES).  
- **Asymmetric encryption**: Uses a public/private key pair (e.g., RSA).

---

### 6: What is hashing and how is it used in cybersecurity?
**Answer:**
Hashing converts data into a fixed-length digest, used to verify **data integrity**. A small change in input results in a completely different hash.

---

### 7: What is a hash collision?
**Answer:** 
When two different inputs produce the same hash. It’s a vulnerability that can be exploited to impersonate data.

---

### 8: What is salting in hashing?
**Answer:**
Salting adds a unique string to input before hashing to prevent **rainbow table attacks** and increase security.

---

## Authorization & IAM

### 9: What is the Principle of Least Privilege?
**Answer:**
Users should only be given the minimum access needed to do their job.

---

### 10: What is Role-Based Access Control (RBAC)?
**Answer:**
RBAC assigns permissions based on job roles, helping manage access efficiently and securely.

---

### 11: What is OAuth and how does it differ from basic auth?
**Answer:**
- **OAuth**: Uses API tokens for secure delegated access.  
- **Basic Auth**: Sends credentials with each request—less secure.

---

## Monitoring & Accounting

### 12: What is session hijacking?
**Answer:**
An attack where a hacker uses a stolen session ID to impersonate a legitimate user.

---

### 13: Why are access logs important?
**Answer:**
Access logs help detect unauthorized activity, track user actions, and support incident investigations.

---

### 14: What is the AAA framework in cybersecurity?
**Answer:**
- **Authentication** – Verifies identity  
- **Authorization** – Grants access  
- **Accounting** – Logs user activity

---

## General Security Concepts

### 15: What’s the difference between a data owner and a data custodian?
**Answer:**
- **Data Owner**: Decides who can access data  
- **Data Custodian**: Maintains the storage and protection of the data

---

### 16: What are the three categories of security controls?
**Answer:**
- **Technical** – E.g., encryption, firewalls  
- **Operational** – E.g., daily processes, user training  
- **Managerial** – E.g., audits, policies, security plans

---




