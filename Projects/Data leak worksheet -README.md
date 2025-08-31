# Data Leak Worksheet

## Incident Summary
A sales manager shared access to a folder of **internal-only documents** with their team during a meeting. The folder included:
- Files related to a **new, unreleased product**
- **Customer analytics**
- **Promotional materials**

After the meeting:
- Access to the folder **was not revoked**
- The manager **warned the team** not to share the materials without approval

### What Went Wrong:
During a video call, a sales team member:
- **Forgot the warning**
- Shared a **link to the internal folder**, not just the promotional materials
- The business partner **posted the folder link publicly** on social media

---

## Control: Least Privilege

### Issue(s)
- Sensitive file access was **granted without strict limitations**
- Access **was not revoked** post-meeting
- The sales rep **shared a full folder** instead of specific files

---

## Review: NIST SP 800-53 – AC-6

**AC-6: Least Privilege**  
The control emphasizes the need to:
- Grant **only necessary access** for tasks
- Implement **role-based restrictions**
- Use **automatic access revocation**
- Conduct **regular privilege audits**

---

## Recommendation(s)

1. **Implement automatic access revocation**  
   - Revoke access after meetings or task completion  
   - Reduces risk from forgotten or lingering permissions

2. **Enforce Role-Based Access Controls (RBAC)**  
   - Ensure users can **only access what their role requires**  
   - Prevents broad file exposure and minimizes mistakes

---

## Justification

- **Automatic revocation** ensures temporary access doesn’t become permanent risk
- **RBAC** limits sensitive data exposure by narrowing file access scope
- Together, they **reduce accidental leaks** and enforce a security-first culture

---

## Security Plan Snapshot

| **Function** | **Category**        | **Subcategory**                         | **Reference(s)**                   |
|--------------|---------------------|------------------------------------------|------------------------------------|
| Protect      | PR.DS: Data Security | PR.DS-5: Protections against data leaks | NIST SP 800-53: [AC-6](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) |

> NIST SP 800-53 outlines how to protect against data leaks using least privilege controls. It is a key part of the **NIST Cybersecurity Framework (CSF)**.

---

## NIST SP 800-53: AC-6 – Least Privilege

### **Control**
> Only the minimal access and authorization required to complete a task or function should be provided to users.

### **Discussion**
- Use processes, roles, and user accounts to **enforce least privilege**
- Prevent users from having higher access than necessary for business objectives

### **Control Enhancements**
- Restrict access **based on user role**
- **Automatically revoke** access after time or task completion
- Keep **activity logs** of account provisioning
- Conduct **regular audits** of user privileges

---

> **Note**: In the NIST SP 800-53 framework, "Least Privilege" is listed under Access Control as **AC-6**.

---

## Project Credit  
- **Project Executed & Presented By**: **Mohammad Aminul Islam** (Cybersecurity Analyst)  
- **Project Source**: Google Cloud Security Command Center hands-on project (Coursera)  
- **Guidance & Framework**: Google Cloud documentation & instructions  
- **Copyright**: © 2022 Google LLC. Google and the Google logo are trademarks of Google LLC. Other names may be trademarks of their respective companies.  
