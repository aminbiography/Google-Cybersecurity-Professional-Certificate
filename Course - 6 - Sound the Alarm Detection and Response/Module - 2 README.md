
# Advanced Network Analysis with Wireshark & tcpdump

---

## 1. What is the Difference Between Wireshark and tcpdump?
**Answer:**

**Wireshark**  
- Graphical user interface (GUI)  
- Deep packet inspection  
- Ideal for detailed analysis and visual troubleshooting  

**tcpdump**  
- Command-line interface (CLI)  
- Lightweight and scriptable  
- Best for remote systems and quick captures  

---

## 2. What is a Packet Capture (p-cap) File and How Is It Useful?
**Answer:**

A `.pcap` file stores captured network packets. It's useful for:

- Offline inspection  
- Sharing with teams for investigation  
- Forensic analysis and troubleshooting  
- Replaying network behavior  

---

## 3. What is Packet Sniffing, and Is It Legal?
**Answer:**

**Packet sniffing** is capturing and inspecting packets on a network.

Legal if:
- On private networks  
- With proper authorization  

Illegal if:
- Without consent  
- On third-party/public networks  

---

## 4. Common Use Cases for `tcpdump`
**Answer:**

- Real-time traffic monitoring  
- Filtering traffic by port, IP, or protocol  
- Saving packets to a file  
- Network troubleshooting  
- Detecting anomalies or malicious traffic  

---

## 5. How to Capture Only HTTP Traffic Using `tcpdump`
**Answer:**

```bash
sudo tcpdump -i eth0 port 80
```

---

## 6. `tcpdump` Flags: `-v`, `-w`, `-r`, and `-n`

| Flag | Description                  |
|------|------------------------------|
| `-v` | Verbose output               |
| `-w` | Write packets to a file      |
| `-r` | Read from a `.pcap` file     |
| `-n` | No name resolution (IP/Port) |

---

## 7. What is an IP Header and Why Is It Important?
**Answer:**

The IP header contains:

- Source/Destination IP addresses  
- TTL (Time To Live)  
- Protocol type (TCP/UDP)  
- Checksum for integrity  

**Why it's important:**  
It helps trace, validate, and analyze network traffic.

---

## 8. What is an Indicator of Compromise (IoC)?
**Answer:**

An **Indicator of Compromise (IoC)** is evidence of malicious activity, such as:

- Unusual IP addresses  
- Unexpected ports in use  
- Known malware file hashes  
- Suspicious or flagged domains  

---

## 9. What is the Significance of TTL (Time To Live)?
**Answer:**

- Limits the number of hops a packet can take  
- Prevents routing loops  
- Can help with OS fingerprinting or detecting spoofed packets  

---

## 10. How Do `tcpdump` and Wireshark Support Incident Response?
**Answer:**

| Tool      | Role in Incident Response                             |
|-----------|-------------------------------------------------------|
| `tcpdump` | Fast, remote, CLI-based packet capture                |
| Wireshark | Deep analysis with GUI and packet visualization       |
| Both      | Forensics, timeline creation, malware detection       |

---

## 11. What are Indicators of Attack (IoA) and How Do They Differ from IoCs?
**Answer:**

| Type | Description                                                                           |
|------|---------------------------------------------------------------------------------------|
| IoA  | Indicates malicious behavior or intent, like privilege escalation or lateral movement |
| IoC  | Evidence that a compromise has occurred, like malicious files or suspicious IPs       |

---

## 12. What is the Difference Between TCP and UDP Traffic in Analysis?
**Answer:**

| Feature     | TCP                             | UDP                      |
|-------------|---------------------------------|--------------------------|
| Type        | Connection-oriented             | Connectionless           |
| Reliability | Reliable (ACK, retransmit)      | Unreliable (best-effort) |
| Session     | Easier to track                 | Harder to track          |
| Use Cases   | HTTP, HTTPS, SSH, FTP           | DNS, VoIP, Streaming     |
| Performance | Slower due to handshakes        | Faster and lightweight   |

---

## 13. What is a MAC Address and How Is It Different from an IP Address?
**Answer:**

- **MAC Address**: A unique hardware-level identifier tied to a device’s NIC (persistent and local).  
- **IP Address**: A logical address used for routing on networks, which can change.  

**Summary**: MAC is hardware-bound, IP is network-bound.

---

## 14. Why Disable Name Resolution (`-n` or `-nn`) in `tcpdump`?
**Answer:**

- Skips reverse DNS lookups  
- Improves performance  
- Avoids unnecessary or alerting DNS queries during capture  

---

## 15. Common Filters Used in Wireshark/`tcpdump`
**Answer:**

**tcpdump filters:**

```bash
tcp port 80
ip src 192.168.1.1
port 443
tcp
```

**Wireshark filters:**

```wireshark
ip.addr == 192.168.1.1
tcp.port == 443
udp.port == 53
http
dns
```

---

## 16. What is the Role of the Checksum in IP Headers?
**Answer:**

- Used for error checking  
- Validates the integrity of the IP header  
- Can help detect malformed or tampered packets  

---

## 17. What are the Four Phases of the NIST Incident Response Lifecycle?
**Answer:**

1. Preparation  
2. Detection and Analysis  
3. Containment, Eradication, and Recovery  
4. Post-Incident Activity  

---

## 18. What Do the Flags `[S]`, `[P.]`, `[.]` Mean in `tcpdump` Output?
**Answer:**

| Flag  | Meaning                          |
|-------|----------------------------------|
| `[S]` | SYN – Start of TCP connection    |
| `[P.]`| PUSH + ACK – Data sent and ack'd |
| `[.]` | ACK – Acknowledgment only        |

---

## 19. How Can You Capture Traffic from All Interfaces Using `tcpdump`?
**Answer:**

```bash
sudo tcpdump -i any
```

---

## 20. What Is the Importance of Timestamps in Packet Captures?
**Answer:**

- Helps reconstruct timelines  
- Crucial for correlating with logs  
- Useful in forensic investigations  

```bash
tcpdump -tttt -i eth0
```

---

## tcpdump - Common Commands

### Basic Capture

```bash
sudo tcpdump -i eth0
```

### Filter by Protocol

```bash
sudo tcpdump -i eth0 tcp
sudo tcpdump -i eth0 udp
sudo tcpdump -i eth0 icmp
```

### Filter by IP Address

```bash
sudo tcpdump -i eth0 src 192.168.1.10
sudo tcpdump -i eth0 dst 10.0.0.5
```

### Filter by Port

```bash
sudo tcpdump -i eth0 port 443
sudo tcpdump -i eth0 src port 22
sudo tcpdump -i eth0 dst port 80
```

### Save and Read from File

```bash
sudo tcpdump -i eth0 -w capture.pcap
sudo tcpdump -r capture.pcap
```

### Disable DNS & Service Name Resolution

```bash
sudo tcpdump -i eth0 -nn
```

### Limit Number of Captured Packets

```bash
sudo tcpdump -i eth0 -c 10
```

### Verbose Output

```bash
sudo tcpdump -i eth0 -v
sudo tcpdump -i eth0 -vv
sudo tcpdump -i eth0 -vvv
```

---

## Wireshark - Common Display Filters

### IP Address Filters

```wireshark
ip.addr == 192.168.1.1
ip.src == 10.0.0.5
ip.dst == 8.8.8.8
```

### Port Filters

```wireshark
tcp.port == 443
udp.port == 53
tcp.srcport == 22
tcp.dstport == 80
```

### Protocol Filters

```wireshark
http
dns
icmp
tcp
udp
```

### TCP Flag Filters

```wireshark
tcp.flags.syn == 1
tcp.flags.ack == 1
tcp.flags.reset == 1
```

### Application Layer Filters

```wireshark
http.request
http.response
dns.qry.name == "example.com"
```

### Other Useful Filters

```wireshark
frame contains "password"
tcp contains "GET"
tcp.len > 0
```

---

## Helpful Links

- [Wireshark Official Documentation](https://www.wireshark.org/docs/)
- [tcpdump Man Page](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Awesome Cybersecurity Blue Team](https://github.com/hslatman/awesome-cybersecurity-blueteam)

---

## Extra Tips

### Use `tshark` for Command-Line Wireshark

```bash
tshark -r capture.pcap
```

### Allow `tcpdump` to Run Without `sudo`

```bash
sudo setcap cap_net_raw,cap_net_admin=eip $(which tcpdump)
```

---
