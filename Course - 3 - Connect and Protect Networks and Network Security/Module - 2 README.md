# Network Security Essentials

---

### 1. What is the difference between a stateful and stateless firewall?

**Answer:**  
A **stateful firewall** tracks the state of active connections and makes decisions based on the context of traffic (e.g., part of an established session).  
A **stateless firewall** uses predefined rules and doesn’t keep track of traffic states, making it faster and easier to configure but generally less secure.

---

### 2. What is the role of a proxy server in network security?

**Answer:**  
A **proxy server** acts as an intermediary between users and external networks. It hides internal IPs, filters traffic, blocks malicious sites, and caches frequent data to boost speed and reduce direct server exposure.  
- **Forward proxy**: Used by clients to access external content  
- **Reverse proxy**: Used to protect and manage traffic to internal servers

---

### 3. What is IEEE 802.11, and how is it related to wireless security?

**Answer:**  
**IEEE 802.11** is a set of standards for wireless LAN (Wi-Fi) communication. It includes security protocols like **WEP**, **WPA**, **WPA2**, and **WPA3**—with WPA3 offering advanced protection via features like **128-bit encryption** and **Simultaneous Authentication of Equals (SAE)**.

---

### 4. How does a VPN protect data?

**Answer:**  
A **VPN** encrypts internet traffic and hides the user's IP using **encapsulation**—a method that wraps data in a secure tunnel. This ensures data confidentiality, especially over public networks, and blocks interception or tampering.

---

### 5. What is the difference between WireGuard and IPSec VPN protocols?

**Answer:**  
- **WireGuard**: Lightweight, fast, and simple to configure—ideal for modern high-speed applications.  
- **IPSec**: Older, complex, but highly supported—commonly used in site-to-site VPNs for secure enterprise connections.

---

### 6. What is a Demilitarized Zone (DMZ) in network security?

**Answer:**  
A **DMZ** is a network zone that separates the internal network from external access. Public-facing services like web and mail servers reside here to minimize risk to the secure internal network if compromised.

---

### 7. What are the benefits of subnetting in a network?

**Answer:**  
**Subnetting** splits a large network into smaller, manageable segments. Benefits include:  
- Improved performance and traffic isolation  
- Enhanced security through controlled access  
- Better organization and IP management via **CIDR** notation

---

### 8. What is encapsulation in VPNs, and why is it important?

**Answer:**  
**Encapsulation** is the process of wrapping data with additional headers and encrypting it. This hides sensitive content and ensures secure communication over untrusted networks, protecting against interception and data leaks.

---

### 9. How does a forward proxy differ from a reverse proxy?

**Answer:**  
- **Forward proxy**: Manages outbound requests from internal users to the internet.  
- **Reverse proxy**: Manages inbound requests from the internet to internal servers, masking internal infrastructure.

---

### 10. What is port filtering and why is it used?

**Answer:**  
**Port filtering** allows or blocks traffic based on port numbers. It limits access to specific services (e.g., only allowing HTTPS on port 443), reduces attack surfaces, and enhances overall network security.

---

