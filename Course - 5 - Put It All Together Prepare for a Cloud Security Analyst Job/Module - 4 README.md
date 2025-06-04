## FIREWALLS & NETWORK SECURITY

**1. What is the difference between a stateful and a stateless firewall?**  
**Answer:**  
A **stateful firewall** tracks the state of active connections and makes decisions based on the context of the traffic.  
A **stateless firewall** filters packets based only on predefined rules, without tracking the state of connections.

**2. What is a DDoS attack and how can it be mitigated?**  
**Answer:**  
A **Distributed Denial of Service (DDoS)** attack overwhelms a target with traffic from multiple sources, causing service outages.  
**Mitigation techniques include:**
- Implementing firewall rate limits  
- Using intrusion detection/prevention systems (IDS/IPS)  
- Filtering spoofed IP addresses  
- Employing cloud-based DDoS protection services

**3. Explain the TCP 3-way handshake.**  
**Answer:**   
1. **SYN** – The client sends a connection request.  
2. **SYN-ACK** – The server acknowledges the request and responds.  
3. **ACK** – The client confirms and establishes the connection.

---

## SECURITY HARDENING

**4. What is security hardening?**  
**Answer:**   
Security hardening is the process of reducing vulnerabilities and the attack surface by updating software, configuring devices securely, removing unused applications, and enforcing security policies.

**5. What are OS hardening tasks?**  
**Answer:**  
- Installing patch updates  
- Enforcing strong password policies and MFA  
- Disabling unused ports and services  
- Establishing a baseline configuration

**6. How does port filtering enhance network security?**  
**Answer:**    
Port filtering blocks or allows traffic through specific port numbers, limiting unwanted communication and protecting against attacks targeting unused or vulnerable ports.

---

## CLOUD SECURITY

**7. What is the shared responsibility model in cloud security?**  
**Answer:**  
In cloud security, the **Cloud Service Provider (CSP)** is responsible for securing the infrastructure, while the **organization** using the service is responsible for securing their data, configurations, and user access.

**8. What is cryptographic erasure?**  
**Answer:**  
It's a process of destroying encryption keys, making the encrypted data undecipherable and effectively “erased” from accessible use.

**9. How does IAM (Identity and Access Management) help in cloud security?**  
**Answer:**  
IAM helps manage **who** has access to cloud resources and **what actions** they can perform. Proper IAM configuration reduces the risk of unauthorized access.

---

## MONITORING & DETECTION

**10. What is a SIEM tool and why is it important?**  
**Answer:**   
A **Security Information and Event Management (SIEM)** tool collects and analyzes log data in real time, helping detect, investigate, and respond to security threats across the network from a single dashboard.

**11. What is network log analysis and how is it used?**  
**Answer:**  
Network log analysis is the review of logs from devices like firewalls and servers to identify **suspicious activity**, **anomalies**, or **policy violations**.

---

## THREATS & ATTACKS

**12. What is an IP spoofing attack?**  
**Answer:**   
An attacker sends packets with a forged source IP address to **disguise their identity** or **impersonate a trusted device**.

**13. What is a packet sniffing attack and how can it be prevented?**  
**Answer:**  
Packet sniffing captures data packets in transit.  
**Preventive measures:**
- Use encryption (HTTPS, SSL/TLS)  
- Segment the network  
- Use switched networks instead of hubs

**14. Explain the difference between active and passive packet sniffing.**  
**Answer:**  
- **Active sniffing:** Manipulates network traffic to intercept data.  
- **Passive sniffing:** Listens quietly on the network without altering traffic.

---

## TECHNICAL CONCEPTS & TOOLS

**15. What is the purpose of a VPN?**  
**Answer:**  
A **Virtual Private Network (VPN)** encrypts your internet connection and hides your IP address, allowing **secure data transmission** over public networks.

**16. What is network segmentation and why is it important?**  
**Answer:**   
It’s dividing a network into **smaller subnets** to limit access and contain potential security breaches, reducing the **impact of an attack**.

**17. How does a reverse proxy server differ from a forward proxy server?**  
**Answer:**  
- A **forward proxy** hides the **client** from the internet.  
- A **reverse proxy** hides **internal servers** from the internet and manages **incoming traffic**.

