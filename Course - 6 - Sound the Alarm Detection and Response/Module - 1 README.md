# 

---

## Incident Response & Lifecycle

### 1. What are the four phases of the NIST Incident Response Lifecycle?
**Answer:**
- **Preparation**
- **Detection and Analysis**
- **Containment, Eradication, and Recovery**
- **Post-Incident Activity**

---

### 2. How would you differentiate an event from a security incident?
**Answer:**
- An **event** is any observable occurrence on a network or system (e.g., a login attempt).
- A **security incident** is an event that actually or potentially compromises confidentiality, integrity, or availability, or violates policy.

---

## Incident Response Roles & Teams

### 3. What are the main roles in a CSIRT (Computer Security Incident Response Team)?
**Answer:**
- **Security Analyst:** Investigates alerts.
- **Technical Lead:** Manages technical response.
- **Incident Coordinator:** Manages communication and coordination.

---

### 4. How does a SOC differ from a CSIRT?
**Answer:**
- A **SOC** monitors and responds to threats in real-time, often structured in tiers.
- A **CSIRT** is formed to handle incidents and may involve multiple departments.

---

## Documentation & Tools

### 5. Why is effective documentation critical in incident response?
**Answer:**
- It ensures clarity, supports compliance, reduces confusion during incidents, and allows future reference.

---

### 6. Name three types of documentation used in incident response.
**Answer:**
- Incident Handler’s Journal
- Playbooks
- Final Incident Reports

---

## Detection Tools (IDS, IPS, EDR, SIEM, SOAR)

### 7. How does an IDS differ from an IPS?
**Answer:**
- **IDS** detects and alerts but doesn’t stop threats.
- **IPS** detects, alerts, and **actively blocks** threats.

---

### 8. What is EDR and how does it differ from IDS/IPS?
**Answer:**
- **EDR** is installed on endpoints and uses behavioral analysis and automation to detect and respond to threats.

---

### 9. What does a SIEM tool do? Name two popular SIEM tools.
**Answer:**
- A **SIEM** collects, normalizes, and analyzes log data to detect threats and generate alerts.
- Examples: **Splunk**, **IBM QRadar**

---

### 10. Describe the SIEM process in three steps.
**Answer:**
1. Collect and aggregate data  
2. Normalize data  
3. Analyze data and generate alerts

---

### 11. What is the purpose of a SOAR tool?
**Answer:**
- **SOAR** automates incident response tasks and integrates tools/workflows for faster case handling.

---

## Detection Logic & Alert Types

### 12. What are the four detection outcomes in IDS systems?
**Answer:**
- **True Positive** – Real threat correctly detected  
- **False Positive** – Benign event flagged as threat  
- **True Negative** – No threat and no alert  
- **False Negative** – Real threat missed by system

---

## Investigation & Log Analysis

### 13. What is log normalization and why is it important in SIEM?
**Answer:**
- **Normalization** converts varied log formats into a consistent structure for easier analysis and correlation.

---

### 14. How do security analysts typically prioritize alerts?
**Answer:**
- By severity, confidence, affected assets, and potential business impact, often guided by SIEM rules or threat intel.

---

## Behavioral & Situational

### 15. In a real-world scenario, what would be your first step after receiving a critical alert about possible ransomware?
**Answer:**
1. Validate the alert  
2. Escalate if confirmed  
3. Begin containment (e.g., isolate machines)  
4. Document actions in the incident handler’s journal

---


