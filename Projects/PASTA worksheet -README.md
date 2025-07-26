# PASTA Worksheet – Sneaker Company

---

## I. Business and Security Objectives

| Objective                                                                                   |
|---------------------------------------------------------------------------------------------|
| The app will process transactions securely to protect user payment information.             |
| User data privacy is a priority, ensuring compliance with regulations (e.g., GDPR, PCI DSS).|
| Buyers and sellers should interact via messaging and ratings features.                      |

---

## II. Technical Scope

**Technologies Used:**

| Technology                     |
|-------------------------------|
| Application Programming Interface (API) |
| Public Key Infrastructure (PKI)        |
| SHA-256                              |
| SQL                                   |

**Priority Focus (SQL):**

SQL is prioritized because the app's database handles sensitive data like credentials, transactions, and inventory. SQL injection is a critical risk that must be mitigated early in the design process.

---

## III. Application Decomposition

**Data Flow Summary:**

| Step                              | Description                                             |
|----------------------------------|---------------------------------------------------------|
| 1. User sends search request     | App forwards the request to the server                 |
| 2. Server queries the database   | Retrieves sneaker listings                             |
| 3. Data sent to client           | Listings are displayed to the user via the interface   |

---

## IV. Threat Analysis

| Threat Type  | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| Internal     | Misconfigured database permissions allow unauthorized access.             |
| External     | SQL injection can expose or manipulate sensitive user data.               |

---

## V. Vulnerability Analysis

| Vulnerability               | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| SQL Injection              | User inputs are not sanitized, enabling malicious SQL commands              |
| Weak Session Management    | Insecure session tokens can lead to hijacking or replay attacks             |

---

## VI. Attack Modeling

**Attack Tree Summary:**

| Element        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Asset**      | User data (login credentials, payment details)                              |
| **Threat**     | SQL injection targeting user inputs                                          |
| **Vulnerability** | No input validation; unparameterized SQL queries                        |
| **Attack Path**| Attacker inputs SQL commands to gain unauthorized data access               |

---

## VII. Risk Mitigation Controls

| Control                                   | Purpose                                                       |
|------------------------------------------|---------------------------------------------------------------|
| Input Validation & Sanitization          | Prevents malicious user input                                 |
| Prepared Statements & Parameterized SQL  | Prevents SQL injection                                         |
| Secure Session Management                | Protects against hijacking with encryption and expiry settings|
| Data Encryption (AES & TLS)              | Protects data at rest and in transit                          |

---

**Summary:**
The PASTA threat model identified SQL as a high-priority risk area due to its role in storing sensitive data. By analyzing internal and external threats, we outlined vulnerabilities and attack paths, then recommended controls to reduce risk exposure and ensure regulatory compliance.
