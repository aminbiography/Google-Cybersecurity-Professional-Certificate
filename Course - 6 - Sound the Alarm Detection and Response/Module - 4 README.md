# Cybersecurity – Detection & Response 

## NIST Incident Response Lifecycle
**1: What is the NIST Incident Response Lifecycle and what are its phases?**  
**Answer:**  
The NIST Incident Response Lifecycle includes four phases:
1. **Preparation** – Establishing plans, tools, and resources.
2. **Detection and Analysis** – Identifying and analyzing security incidents.
3. **Containment, Eradication, and Recovery** – Limiting damage, removing threats, and restoring systems.
4. **Post-Incident Activity** – Reviewing and learning from the incident.

---

## IDS Systems
**2: What is the difference between a NIDS and a HIDS?**  
**Answer:**
- **NIDS** (Network-based IDS) monitors network traffic.  
- **HIDS** (Host-based IDS) monitors activity on individual endpoints.

---

## Suricata
**3: Explain the use of Suricata and what type of output it generates.**  
**Answer:**  
Suricata is an open-source IDS/IPS tool that detects threats using rules. It outputs data in **EVE JSON** format, ideal for parsing and ingestion into SIEM tools.

---

## SIEM Tools
**4: What is a SIEM and why is it important?**  
**Answer:** 
A **SIEM** (Security Information and Event Management) collects, normalizes, indexes, and analyzes log data across multiple sources. It helps in detecting threats, conducting investigations, and responding to incidents.

---

## Raw vs. Normalized Log Search
**5: What is the difference between raw log search and normalized data search in a SIEM?**  
**Answer:**
- **Raw Log Search** examines unstructured, original logs—useful for deep investigations.  
- **Normalized Data Search** works on structured, indexed data—faster and easier to query.

---

## Wildcards in SPL
**6: What are wildcards in SPL and how are they used?**  
**Answer:**
Wildcards (e.g., `*`) are used to match multiple similar values.  
Example: `fail*` matches "fail", "failed", "failure", etc.

---

## Phishing Investigation Example
**7: Describe a time you investigated a phishing incident. What steps did you take?**  
**Answer:** 
- Detected `signin.office365x24.com` in a phishing email.  
- Used Chronicle to analyze domain access and related HTTP POST requests.  
- Identified affected assets and observed credentials submission.  
- Blocked the domain and recommended email filter updates.

---

## IoCs vs. IoAs
**8: What are indicators of compromise (IoCs) and indicators of attack (IoAs)?**  
**Answer:**
- **IoCs** = Forensic evidence that an attack has occurred.  
- **IoAs** = Real-time patterns suggesting an ongoing attack.

---

## VirusTotal
**9: What is the role of VirusTotal in threat analysis?**  
**Answer:**
VirusTotal scans files, domains, and URLs using multiple antivirus engines. It helps analysts confirm if an object is malicious based on community and vendor flags.

---

## False Positive Handling
**10: How do you handle a false positive alert in an IDS?**  
**Answer:**
- Review the context of the alert  
- Cross-check with SIEM logs  
- Confirm legitimacy  
- Tune IDS rules to reduce noise

---

## Importance of Documentation
**11: What’s the importance of documentation in incident response?**  
**Answer:**
Documentation (like an incident handler's journal) ensures transparency, supports compliance, and provides a reference for lessons learned.

---

## Tools for Log Analysis
**12: What tools have you used for log analysis and what did you learn?**  
**Answer:** 
- **Splunk (SPL)** – Indexed search and filtering  
- **Chronicle (UDM)** – Normalized and raw log search  
- **Wireshark** – Deep packet inspection  
- **tcpdump** – CLI packet capture

---

## Alerts: True Positive vs. False Positive
**13: What is the difference between a false positive and a true positive alert?**  
**Answer:** 
- **False Positive**: Alert triggered by harmless activity.  
- **True Positive**: Alert correctly identifies a real threat.

---

## Incident Triage
**14: How would you prioritize multiple simultaneous incidents in a SOC environment?**  
**Answer:**
Use **triage** based on severity, business impact, and urgency. Incidents affecting critical systems or involving data exfiltration are prioritized.

---


