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
- Virus &#8594; Malicious code that attaches to legitimate programs or files and spreads when executed, often damaging data or systems.
- Worm &#8594; A self-replicating malware that spreads without user interaction, typically through networks, causing disruptions and resource overload.
- Trojan horse &#8594; Malware disguised as legitimate software, which tricks users into installing it, then secretly performs malicious actions.
- Ransomware &#8594; Locks or encrypts a victim’s data and demands payment (a ransom) to restore access.
- Spyware &#8594; ecretly monitors user activity, collecting sensitive information like keystrokes, passwords, or browsing habits.
- Rootkit &#8594; A stealthy malware that gives attackers administrative access to a system and hides its presence from detection tools.
- Fileless malware &#8594; Operates without installing files on the system; instead, it runs in memory, making it hard to detect with traditional antivirus tools.

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
- Phishing &#8594; A type of cyber attack where attackers send fraudulent emails to trick people into revealing sensitive information. 
- Smishing &#8594; Phishing via SMS text messages, aiming to steal personal data or spread malware.
- Vishing &#8594; Voice phishing; attackers use phone calls to impersonate legitimate entities and extract confidential information. 
- Baiting &#8594; Involves offering something enticing (like free software or USB drives) to lure victims into a trap that leads to malware or data theft. 
- Quid pro quo &#8594; An attacker offers a service or benefit (like IT help) in exchange for access or information, often under false pretenses. 
- Tailgating &#8594; A physical security breach where someone follows an authorized person into a restricted area without proper credentials.
- Spear phishing &#8594; A targeted phishing attack aimed at a specific individual or organization, using personal details to appear legitimate.
- Whaling &#8594; A type of spear phishing that targets high-level executives or important figures in an organization.

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
- **Data at rest** &#8594; Encrypt with AES  
- **Data in transit** &#8594; Use TLS/SSL  
- **Data in use** &#8594; Use access controls and secure session management

---



