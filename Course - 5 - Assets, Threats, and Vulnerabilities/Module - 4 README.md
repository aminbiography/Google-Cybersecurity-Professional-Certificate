# Cybersecurity Threat Modeling, Exploits & Mitigation Strategies

---

## Threat Modeling & Web Exploits

### 1. What is threat modeling, and why is it important?
**Answer:**  
Threat modeling is the process of identifying assets, vulnerabilities, and threats in order to anticipate and mitigate risks before an attack occurs.

---

### 2. What are the six steps of a standard threat modeling process?
**Answer:**
1. Define the scope  
2. Identify threats  
3. Characterize the environment  
4. Analyze threats  
5. Mitigate risks  
6. Evaluate findings

---

### 3. Can you explain what PASTA is in cybersecurity?
**Answer:**  
PASTA (Process for Attack Simulation and Threat Analysis) is a risk-centric threat modeling framework used to simulate attacks and analyze risks. It includes seven stages to align security with business objectives.

---

### 4. What’s the difference between reflected, stored, and DOM-based XSS?
**Answer:**
- **Reflected XSS**: Script is sent in a request and reflected in the response.  
- **Stored XSS**: Script is permanently stored on the server and executed on page load.  
- **DOM-based XSS**: Script is executed on the client side via DOM manipulation.

---

### 5. How does a SQL injection attack work, and how can it be prevented?
**Answer:**  
SQL injection occurs when unfiltered input is inserted into a SQL query.  
**Prevention techniques:**
- Prepared statements  
- Input validation and sanitization  
- Escaping special characters

---

## Malware & Threats

### 6. What are some common types of malware?
**Answer:**
- Virus  
- Worm  
- Trojan horse  
- Ransomware  
- Spyware  
- Rootkit  
- Fileless malware

---

### 7. What is cryptojacking and how can it be detected?
**Answer:**  
Cryptojacking is malware that secretly uses system resources to mine cryptocurrency.  
**Detection signs:**
- System slowdown  
- High CPU usage  
- Crashes  
- Increased electricity usage  
- Detected by IDS tools

---

## Social Engineering

### 8. What are social engineering attacks and examples?
**Answer:**  
Social engineering exploits human behavior to bypass security.  
**Examples:**
- Phishing  
- Smishing  
- Vishing  
- Baiting  
- Quid pro quo  
- Tailgating  
- Spear phishing  
- Whaling

---

## Access Control & Security Practices

### 9. What is the difference between an attack surface and an attack vector?
**Answer:**  
- **Attack surface**: All possible entry points into a system  
- **Attack vector**: The specific method or path used to exploit a system

---

### 10. What is the purpose of access controls in cybersecurity?
**Answer:**  
Access controls enforce the AAA framework:  
- **Authentication**  
- **Authorization**  
- **Accounting**

---

### 11. What is the principle of least privilege?
**Answer:**  
Give users the **minimum level of access** required for their tasks to reduce risk and limit damage in case of compromise.

---

## Security Defenses

### 12. How do prepared statements prevent SQL injection?
**Answer:**  
Prepared statements separate SQL logic from user inputs, preventing attackers from injecting malicious SQL code.

---

### 13. What tools help detect/prevent malware?
**Answer:**
- Intrusion Detection Systems (IDS)  
- Antivirus/Antimalware software  
- Email filters  
- Regular patching  
- User security training

---

### 14. What are best practices to protect web applications?
**Answer:**
- Sanitize user input  
- Use prepared statements  
- Enforce HTTPS  
- Set Content Security Policies  
- Perform vulnerability scans  
- Secure APIs

---

### 15. What are the three states of data and how to protect them?
**Answer:**
- **Data at rest** → Encrypt with AES  
- **Data in transit** → Use TLS/SSL  
- **Data in use** → Use access controls and secure session management

---



