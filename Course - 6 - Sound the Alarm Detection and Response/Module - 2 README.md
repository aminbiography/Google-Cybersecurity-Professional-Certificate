# Advanced Network Analysis Wireshark & tcpdump

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

# Advanced Network Analysis

## 11. What are Indicators of Attack (IoA) and how do they differ from IoCs?
**Answer:**

- **IoA (Indicator of Attack)**: Describes **intent or behavior**, such as privilege escalation or lateral movement attempts.
- **IoC (Indicator of Compromise)**: Shows **evidence** that an attack has occurred, like malware file hashes or suspicious IPs.

---

## 12. What is the difference between TCP and UDP traffic in analysis?
**Answer:**

| Feature                | TCP                          | UDP                          |
|------------------------|------------------------------|-------------------------------|
| Type                   | Connection-oriented          | Connectionless                |
| Reliability            | Reliable (ACK, retransmit)   | Unreliable (best-effort)      |
| Session Tracking       | Easier to track sessions     | Harder to track               |
| Use Cases              | HTTP, HTTPS, SSH, FTP        | DNS, VoIP, Streaming          |
| Performance            | Slower, handshake required   | Faster, lightweight           |

---

## 13. What is a MAC address and how is it different from an IP address?
**Answer:**

- **MAC Address**: A unique hardware-level identifier assigned to a device's NIC. It is persistent and local.
- **IP Address**: A logical address assigned within a network. It may change based on network configuration.
-  MAC is hardware-bound, IP is network-bound.

---

## 14. Why is disabling name resolution (`-n` or `-nn`) in tcpdump important?
**Answer:**

- Prevents **reverse DNS lookups**.
- **Improves speed** of packet capture and display.
- Avoids **alerting attackers** through unintended DNS queries.

---

## 15. What are common filters used in Wireshark/tcpdump?
**Answer:**

**tcpdump filter examples**:
```bash
tcp port 80              # Capture HTTP traffic
ip src 192.168.1.1       # Traffic from a specific source IP
port 443                 # HTTPS traffic
tcp                      # All TCP traffic
```

---

## 16. What is the Role of the Checksum in IP Headers?
**Answer:**

- Used for **error-checking**
- Ensures the **IP header's integrity**
- Helps analysts **spot malformed or tampered packets**

---

## 17. What are the Four Phases of the NIST Incident Response Lifecycle?
**Answer:**

1. **Preparation**
2. **Detection and Analysis**
3. **Containment, Eradication, and Recovery**
4. **Post-Incident Activity**

> This framework is essential for structured incident response and continuous improvement.

---

## 18. What Do the Flags `[S]`, `[P.]`, `[.]` Mean in tcpdump Output?
**Answer:**

- `[S]` → **SYN** – Initiates a TCP connection (handshake)
- `[P.]` → **Push + ACK** – Sends data with acknowledgment
- `[.]` → **ACK only** – Acknowledges receipt

These flags help analyze **TCP session states** and identify **abnormal communication patterns**.

---

## 19. How Can You Capture Traffic from All Interfaces Using tcpdump?
**Answer:**

```bash
sudo tcpdump -i any
```

---

## 20. What Is the Importance of Timestamps in Packet Captures?
**Answer:**

- **Helps reconstruct the timeline** of network events  
- **Crucial for log correlation** and alert investigations  
- **Aids in forensic analysis** and threat hunting  

---

## Final Tip: Build Your Own Cheat Sheet!

Keep a personal **packet analysis cheat sheet** in your GitHub repository with:

- Common `tcpdump` and **Wireshark commands**
- Filtering syntax and **real-world use cases**
- **TCP/IP header structure** reference
- Common **TCP flag meanings**
- **Redacted sample capture outputs**
- **Incident response steps** and templates

---

## Helpful Links

- [Wireshark Official Documentation](https://www.wireshark.org/docs/)
- [tcpdump Man Page](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Awesome Cybersecurity Blue Team](https://github.com/hslatman/awesome-cybersecurity-blueteam)

---


# Common tcpdump and Wireshark Commands

---

## tcpdump - Common Commands

### Basic Capture

```bash
sudo tcpdump -i eth0
```

# tcpdump Command Cheatsheet


# Filter by Protocol
```bash
sudo tcpdump -i eth0 tcp
```
```bash
sudo tcpdump -i eth0 udp
```
```bash
sudo tcpdump -i eth0 icmp
```

# Filter by IP Address
```bash
sudo tcpdump -i eth0 src 192.168.1.10
```
```bash
sudo tcpdump -i eth0 dst 10.0.0.5
```

# Filter by Port
```bash
sudo tcpdump -i eth0 port 443
```
```bash
sudo tcpdump -i eth0 src port 22
```
```bash
sudo tcpdump -i eth0 dst port 80
```

# Save to File and Read from File
```bash
sudo tcpdump -i eth0 -w capture.pcap
```
```bash
sudo tcpdump -r capture.pcap
```

# Disable DNS & Service Name Resolution
```bash
sudo tcpdump -i eth0 -nn
```

# Limit Number of Captured Packets
```bash
sudo tcpdump -i eth0 -c 10
```

# Verbose Output
```bash
sudo tcpdump -i eth0 -v
```
```bash
sudo tcpdump -i eth0 -vv
```
```bash
sudo tcpdump -i eth0 -vvv
```

---

# Wireshark - Common Filters

> Wireshark uses **display filters** (not capture filters like tcpdump)

---

## IP Address Filters

```wireshark
ip.addr == 192.168.1.1
ip.src == 10.0.0.5
ip.dst == 8.8.8.8
```
## Wireshark - Common Display Filters

### Port Filters
```wireshark
tcp.port == 443
```
```wireshark
udp.port == 53
```
```wireshark
tcp.srcport == 22
```
```wireshark
tcp.dstport == 80
```

## Protocol Filters
```wireshark
http
```
```wireshark
dns
```
```wireshark
icmp
```
```wireshark
tcp
```
```wireshark
udp
```

## TCP Flag Filters
```wireshark
tcp.flags.syn == 1
```
```wireshark
tcp.flags.ack == 1
```
```wireshark
tcp.flags.reset == 1
```

## Application Layer Filters
```wireshark
http.request
```
```wireshark
http.response
```
```wireshark
dns.qry.name == "example.com"
```

## Other Useful Filters
```wireshark
frame contains "password"
```
```wireshark
tcp contains "GET"
```
```wireshark
tcp.len > 0
```





