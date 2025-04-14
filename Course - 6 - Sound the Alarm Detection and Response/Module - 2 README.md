# Network Protocol Analyzer - Wireshark & tcpdump

---

## 1. What is the difference between Wireshark and tcpdump?
**Answer:**

**Wireshark**:
- Graphical user interface (GUI)
- Deep packet inspection
- Ideal for detailed analysis and visual troubleshooting

**tcpdump**:
- Command-line interface (CLI)
- Lightweight and scriptable
- Best for remote systems and quick captures

---

## 2. What is a packet capture (p-cap) file and how is it useful?
**Answer:**

A `p-cap` file stores captured network packets. It is useful for:
- Offline inspection
- Sharing with teams for investigation
- Forensic analysis and troubleshooting
- Replaying network behavior

---

## 3. What is packet sniffing, and is it legal?
**Answer:**

**Packet sniffing** is capturing and inspecting packets on a network.

**Legal** if done:
- On private networks
- With proper authorization

**Illegal** if done:
- Without consent
- On third-party/public networks

---

## 4. What are common use cases for tcpdump?
**Answer:**

- Real-time traffic monitoring
- Filtering traffic by port, IP, or protocol
- Saving packets to a file
- Network troubleshooting
- Detecting anomalies or malicious traffic

---

## 5. How do you capture only HTTP traffic using tcpdump?
**Answer:**

```bash
sudo tcpdump -i eth0 port 80
```

## 6. `tcpdump` Flags: `-v`, `-w`, `-r`, and `-n`
**Answer:**

| Flag | Description                      |
|------|----------------------------------|
| `-v` | Verbose output                   |
| `-w` | Write packets to a file          |
| `-r` | Read from a `.pcap` file         |
| `-n` | No name resolution (IP/Port)     |

---

## 7. What is an IP Header and Why Is It Important?
**Answer:**

The **IP header** includes:
- Source/Destination IP addresses  
- TTL (Time To Live)  
- Protocol information (TCP/UDP)  
- Checksum for integrity validation  

**Why it's important:**  
Used in investigations to trace, analyze, and validate network traffic.

---

## 8. What is an Indicator of Compromise (IoC)?
**Answer:**

An **Indicator of Compromise (IoC)** is **evidence of malicious activity**, such as:
- Unusual IP addresses  
- Unexpected ports in use  
- Known malware file hashes  
- Suspicious or flagged domains  

---

## 9. What is the Significance of TTL (Time To Live)?
**Answer:**

TTL helps prevent routing loops by **limiting the number of hops** a packet can take.

TTL values can be used to:
- Identify spoofed packets  
- Perform OS fingerprinting (based on default TTL values)

---

## 10. How Do `tcpdump` and `Wireshark` Support Incident Response?
**Answer:**

| Tool       | Role in Incident Response                                          |
|------------|--------------------------------------------------------------------|
| `tcpdump`  | Fast, remote, CLI-based packet capture                             |
| Wireshark  | Deep analysis with GUI and packet visualization                    |
| **Both**   | Forensics, timeline creation, malware detection                    |

**Tip**:  
Use `tcpdump` for quick capture or automation.  
Use **Wireshark** for deep-dive investigation and visual packet analysis.

---

## Want More?
**Answer:**

- [Wireshark Official Docs](https://www.wireshark.org/docs/)
- [tcpdump Documentation](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Awesome Cybersecurity Blue Team Resources](https://github.com/hslatman/awesome-cybersecurity-blueteam)

---
