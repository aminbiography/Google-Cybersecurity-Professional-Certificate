# Risk Register – Banking Environment

## Operational Environment Overview
The bank operates in a coastal region with low crime rates. It employs 100 on-premises and 20 remote staff. With 2,000 individual and 200 commercial customer accounts, the bank relies on secure data handling and strong compliance. Marketing partnerships with a sports team and local businesses amplify its visibility. Regulatory compliance requires robust cash availability and data security.

---

## Risk Assessment Table

| **Asset**                | **Risk(s)**                        | **Description**                                                | **Likelihood** | **Severity** | **Priority (L × S)** |
|--------------------------|------------------------------------|----------------------------------------------------------------|----------------|--------------|-----------------------|
| Funds                   | Business email compromise          | Employee is tricked into revealing confidential data           | 2              | 3            | 6                     |
| Compromised user database | Data breach via poor encryption     | Customer records are weakly encrypted                          | 3              | 3            | 9                     |
| Financial records       | Leak from public backup server     | Sensitive backups are accessible on public servers             | 3              | 3            | 9                     |
| Funds                   | Theft                               | Bank's safe left unlocked                                      | 1              | 3            | 3                     |
| Operations              | Supply chain disruption             | Delays from hurricanes or coastal storms                       | 2              | 2            | 4                     |

---

## Risk Matrix

|               | **Low (1)** | **Moderate (2)** | **Catastrophic (3)** |
|---------------|-------------|------------------|-----------------------|
| **Certain (3)** | 3           | 6                | 9                     |
| **Likely (2)**  | 2           | 4                | 6                     |
| **Rare (1)**    | 1           | 2                | 3                     |

> **Priority Score Formula:** `Likelihood × Severity`  
> Use the result to determine which risks to address first.

---

## Key Takeaways

- **High-priority risks (score 9):** Database compromise and financial record leaks must be mitigated immediately.
- **Moderate-priority (4–6):** Phishing exposure and supply chain vulnerabilities require strong controls.
- **Low-priority (≤3):** Theft is less likely but still critical due to its severity if it occurs.
- **Environmental factors** (e.g., hurricanes) and **employee access control** are recurring concerns.

---

## Recommendations

- Enforce strong encryption for all customer data.
- Conduct regular phishing simulations and employee training.
- Audit access to backup servers; remove public access immediately.
- Improve physical security protocols (e.g., safe checks).
- Develop disaster recovery plans addressing supply chain disruptions.

---

## Project Credit  
- **Project Executed & Presented By**: **Mohammad Aminul Islam** (Cybersecurity Analyst)  
- **Project Source**: Google Cloud Security Command Center hands-on project (Coursera)  
- **Guidance & Framework**: Google Cloud documentation & instructions  
- **Copyright**: © 2022 Google LLC. Google and the Google logo are trademarks of Google LLC. Other names may be trademarks of their respective companies.  
