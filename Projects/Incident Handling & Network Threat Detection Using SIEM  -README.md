# Portfolio of Mohammad Aminul Islam

## Name:
**Mohammad Aminul Islam**

## Portfolio Title:
**Incident Handling & Network Threat Detection Using SIEM and Packet Analysis Tools**

---

## Professional Summary

I am **Mohammad Aminul Islam**, a cybersecurity practitioner with hands-on experience in **incident response**, **threat detection**, and **network traffic analysis**. Through real-world simulations and investigative use of industry tools, I have developed a strong skill set in identifying and mitigating cyber threats such as **phishing attacks**, **malware infections**, and **data exfiltration**.

My expertise includes working with tools like **Chronicle SIEM**, **Splunk**, **Wireshark**, and **Suricata** to analyze security events, uncover anomalies, and strengthen organizational defenses. I follow structured methodologies such as the **NIST Incident Response Framework**, ensuring a complete cycle of detection, containment, eradication, and post-incident analysis to continuously improve security posture.

---

## Objective

The goal of this project was to simulate and document real-world cybersecurity incidents to enhance practical response capabilities. This involved detecting and analyzing **phishing attacks**, **malware infections**, and **suspicious network activity** using a range of forensic and monitoring tools. The objective was to strengthen **threat visibility**, sharpen **investigative skills**, and develop **incident handling techniques** aligned with professional cybersecurity operations and best practices.

---

## Incident Handling & Threat Investigation Journal

| Date       | Entry | Description                                                                  | Tool(s) Used         | Who                                                                 | What                                                                                                     | When                                | Where                                                                | Why                                                                                     | Additional Notes                                                                                                                                               |
|------------|-------|------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 05-02-2024 | 01    | Analyzed a phishing email incident to determine affected assets.             | Chronicle SIEM       | Unknown attacker using phishing campaign.                           | Employees received phishing email with suspicious domain; credentials may be exposed.                   | Jan 30, 2024 – 10:45 AM UTC         | Multiple employees received phishing emails.                         | Email bypassed filters and was opened by users.                                        | Investigated domain reputation and HTTP POSTs in Chronicle; containment and stricter filters planned.                                                         |
| 01-02-2024 | 02    | Investigated a suspicious file hash.                                         | VirusTotal, Splunk   | Potential attacker distributing malware via email.                  | Employee downloaded attachment that triggered alert.                                                    | Jan 31, 2024 – 2:15 PM UTC          | Employee laptop (HOST-123).                                           | Executable bypassed endpoint security.                                                | VirusTotal flagged hash; Splunk confirmed execution; file quarantined, system reimaged.                                                                        |
| 28-01-2024 | 03    | Performed packet capture to detect unauthorized traffic.                     | Wireshark            | Captured traffic for 10 minutes.                                    | Applied filters to detect outbound exfiltration to suspicious IP.                                       | Incident identified post-capture    | IP confirmed as known C2 server via threat intelligence.            | Compromised host was leaking data.                                                     | Host isolated, credentials reset, logs saved for further forensics.                                                                                             |
| 25-01-2024 | 04    | Created and tested a custom Suricata rule for HTTP traffic.                  | Suricata             | Analyst defined custom IDS rule.                                    | Tested on replayed malicious traffic; rule triggered as expected.                                       | During testing phase in lab         | Rule deployed in production IDS after validation.                    | Improve phishing detection via HTTP GET monitoring.                                   | Rule improved detection accuracy; plan to refine logic for broader detection scope.                                                                              |

---

## Reflections / Notes

- **Wireshark Challenge**:  
  Initially difficult due to the volume and complexity of network data. Gained confidence after practicing with filters and understanding protocols.

- **NIST Framework Insight**:  
  I now recognize that **detection** is just one part of the cycle—**containment**, **eradication**, and **post-incident analysis** are equally critical for improving security.

- **SIEM Experience**:  
  Enjoyed working with **Splunk** and **Chronicle**. Their powerful search and correlation capabilities, especially Splunk’s **SPL queries**, made complex analysis manageable and insightful.

---

## Conclusion

This project not only deepened my **technical abilities**, but also enhanced my understanding of **structured incident response**.

Working with tools like **Wireshark** was initially challenging due to the volume and complexity of packet data. However, with consistent practice, I became confident in **filtering** and **protocol analysis**.

I also came to value the **full incident response lifecycle** defined by the **NIST Framework**—understanding that detection is just the beginning, and that **containment, eradication, and recovery** are equally vital.

Using **SIEM platforms like Splunk and Chronicle**, I gained practical experience in **event correlation**, **anomaly detection**, and **advanced querying**, preparing me for real-world roles in **cybersecurity operations**.

This hands-on project has solidified my **passion for threat detection and response**, and has equipped me with skills that align with current industry demands.

---


## Project Credit  
- **Project Executed & Presented By**: **Mohammad Aminul Islam** (Cybersecurity Analyst)  
- **Project Source**: Google Cloud Security Command Center hands-on project (Coursera)  
- **Guidance & Framework**: Google Cloud documentation & instructions  
- **Copyright**: © 2022 Google LLC. Google and the Google logo are trademarks of Google LLC. Other names may be trademarks of their respective companies.  
