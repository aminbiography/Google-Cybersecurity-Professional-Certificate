# Access Controls Worksheet (Authorization / Authentication)

| **Section**      | **Details** |
|------------------|-------------|
| **Note(s)**      | - The incident was caused by a user identified as `Legal\Administrator`. <br> - The event log shows suspicious activity: a payroll event was added to `FAUX_BANK` at **8:29:57 AM on 10/03/2023**. <br> - The IP address used in the incident (`152.207.255.255`) is associated with the device `Up2-NoGud`. |
| **Issue(s)**     | - The account `Legal\Administrator` had **administrator-level access**, which may not have been necessary. <br> - No clear process to review or restrict access for **inactive or unauthorized accounts**. <br> - **Shared cloud drive usage** without individual user accountability increases security risks. |
| **Recommendation(s)** | - Replace shared cloud drive access with **individual user accounts** and **activity tracking**. <br> - Implement **Role-Based Access Control (RBAC)** to ensure users receive only the permissions needed. <br> - Enforce **Multi-Factor Authentication (MFA)** for all administrator-level accounts. |
