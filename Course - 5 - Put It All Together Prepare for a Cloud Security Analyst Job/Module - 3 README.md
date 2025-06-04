### Network Security: Common Attacks and Defenses

1. **What is a Denial of Service (DoS) attack?**  
   A DoS attack is a cyberattack where the attacker floods a network or server with excessive traffic, exhausting its resources and making it inaccessible to legitimate users. It typically originates from a single source.

2. **How is a DDoS attack different from a DoS attack?**  
   A DDoS (Distributed Denial of Service) attack uses multiple compromised devices from various locations to flood a target with traffic. Unlike a DoS attack, which comes from one source, DDoS attacks are harder to detect and mitigate due to their distributed nature.

3. **Can you explain a SYN flood attack and how it works?**  
   A SYN flood is a type of DoS attack where the attacker sends a large number of SYN requests to a server but never completes the TCP handshake. This leaves the server with half-open connections, consuming resources until it becomes unresponsive to legitimate traffic.

4. **What is packet sniffing and how can it be harmful?**  
   Packet sniffing is the practice of capturing and inspecting data packets on a network. While useful for diagnostics, it becomes malicious when attackers intercept private or sensitive information not intended for them.

5. **Differentiate between active and passive packet sniffing.**  
   - **Passive sniffing:** Monitors network traffic without altering it. It simply observes data.  
   - **Active sniffing:** Intercepts and possibly alters the data in transit, which can include redirecting packets or modifying their contents.

6. **What is IP spoofing?**  
   IP spoofing is a network attack where the attacker alters the source IP address in a packet to impersonate a trusted device, tricking systems into accepting it as legitimate traffic.

7. **What is a Smurf attack?**  
   A Smurf attack is a combination of a DoS and IP spoofing attack. The attacker sends spoofed ICMP requests to a network's broadcast address, causing all devices to reply to the victim's IP, overwhelming them with responses.

8. **How can you prevent packet sniffing attacks?**  
   - Use VPNs to encrypt network traffic.  
   - Prefer HTTPS over HTTP for secure web browsing.  
   - Avoid unprotected public Wi-Fi or ensure it’s used only with encryption enabled.  
   - Implement network segmentation and secure switches instead of hubs.

9. **What are replay attacks, and how do they work?**  
   A replay attack is when a malicious actor intercepts a data packet and resends it later to deceive the recipient. This can be used to bypass authentication or repeat transactions fraudulently.

10. **What are some methods to mitigate SYN flood attacks?**  
   - **SYN cookies** to prevent allocating resources before the handshake is complete.  
   - **Firewalls** to detect and limit suspicious SYN traffic.  
   - **Rate limiting** to control the number of connections per IP.  
   - **Intrusion Prevention Systems (IPS)** to identify and block malicious traffic patterns.


