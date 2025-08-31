# Portfolio of Mohammad Aminul Islam

## Name:
**Mohammad Aminul Islam**

## Portfolio Title:
**Cybersecurity Incident Report: Network Traffic Analysis**

---

## Professional Summary

My name is **Mohammad Aminul Islam**. I am skilled in **programming**, **problem-solving**, and **analytical thinking**. I am committed to protecting organizations from cyber threats, particularly in **cloud and web security**. I am dedicated to ensuring the **confidentiality, integrity, and availability** of data and systems.

My goal is to utilize my skills and knowledge to help organizations **strengthen their security posture** and protect sensitive information from evolving threats.

---

## Objective

The objective of this project is to analyze network traffic and identify the root cause of a cybersecurity incident involving **DNS service inaccessibility**. Specifically, the project aims to:

- Investigate why DNS queries for the domain `www.foodparkrecipesforme.com` fail  
- Determine the cause of the “**UDP port 53 unreachable**” error  
- Document the steps taken to troubleshoot and resolve the issue  
- Propose a solution to restore DNS functionality and ensure reliable domain name resolution in the future  

This project highlights **practical skills** in network traffic analysis, troubleshooting, and incident resolution to address real-world cybersecurity challenges.

---

## Cybersecurity Incident Report: Network Traffic Analysis

### Part 1: Summary of the Problem in DNS and ICMP Traffic

- A DNS query for `www.foodparkrecipesforme.com` was sent via **UDP to port 53**.
- The response received was an **ICMP error**: `"UDP port 53 unreachable"`.
- This suggests that:
  - The DNS server at IP `203.0.113.2` is down or misconfigured
  - Or a firewall is blocking communication on **UDP port 53**

#### Possible Causes:
- DNS server is offline  
- Firewall misconfiguration  
- Network or hardware failure  

---

### Part 2: Data Analysis and Cause of the Incident

- **Time incident occurred**:  
  First logged at `13:24:32.192571` and persisted across multiple attempts

- **First failed DNS query**:  
  - Source IP: `192.51.100.15`  
  - Destination IP: `203.0.113.2`  
  - Result: ICMP error `UDP port 53 unreachable`  

- **How the IT team became aware**:  
  Users reported inability to access the website with the error “**destination port unreachable**”.

- **Actions taken by the IT team**:
  - Replicated the issue
  - Used `tcpdump` to capture network logs
  - Identified failed DNS queries and ICMP error responses

- **Key findings**:
  - Port affected: UDP port 53  
  - DNS server: `203.0.113.2`  
  - Source IP: `192.51.100.15`  
  - No service listening on port 53  
  - Repeated ICMP error messages observed  

- **Likely cause**:  
  - DNS service not running  
  - Firewall or network misconfiguration  

---

### Part 3: Tcpdump Log Summary

After analyzing `tcpdump`:

- Repeated **ICMP packets** confirmed the issue:  
  `"UDP port 53 unreachable"`  
- **UDP DNS queries** were sent to `203.0.113.2:53`  
- ICMP error messages consistently returned  
- Indicates that the DNS service is **not accessible or not running**  

---

### Part 4: Analysis and Recommended Solution

- **Time first reported**:  
  `13:24:32.192571`

- **Symptoms**:
  - Users received “**destination port unreachable**” error
  - All DNS requests to `www.foodparkrecipesforme.com` failed

- **Current status**:  
  Issue is ongoing — DNS queries continue to fail

- **Information discovered**:
  - Port 53 on `203.0.113.2` is not reachable  
  - ICMP errors suggest service is unavailable or blocked  

#### Recommended Steps:
1. Verify the DNS server at `203.0.113.2` is operational  
2. Check for firewall rules or policies blocking **UDP traffic on port 53**  
3. Restart or reconfigure the DNS service if it is down  
4. Retest DNS resolution and verify connectivity  

- **Suspected root cause**:  
  A misconfigured or offline DNS server or blocked UDP traffic due to firewall rules  

---

## Conclusion

This incident highlights the **critical importance of DNS server availability** and proper **network traffic monitoring**. The recurring `UDP port 53 unreachable` error suggests that the DNS server was either offline or inaccessible due to network/firewall misconfiguration.

By addressing the root cause — whether service downtime or firewall restrictions — **DNS functionality can be restored**, enabling domain name resolution for the affected website.

This case demonstrates my ability to:
- Diagnose and interpret network communication failures  
- Utilize tools like `tcpdump` for traffic analysis  
- Recommend actionable, technical solutions to restore service availability  

---

## Project Credit  
- **Project Executed & Presented By**: **Mohammad Aminul Islam** (Cybersecurity Analyst)  
- **Project Source**: Google Cloud Security Command Center hands-on project (Qwiklabs / Coursera)  
- **Guidance & Framework**: Google Cloud documentation & Qwiklabs instructions  
- **Copyright**: © 2022 Google LLC. Google and the Google logo are trademarks of Google LLC. Other names may be trademarks of their respective companies.  
