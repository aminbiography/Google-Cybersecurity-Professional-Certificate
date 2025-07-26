# Portfolio of Mohammad Aminul Islam

## Name:
**Mohammad Aminul Islam**

## Portfolio Title:
**File Permissions in Linux**

---

## Project Description

The research team at my organization needed to update the **file permissions** for specific files and directories within the `projects` directory. The existing permissions did not reflect the proper level of authorization. To improve **system security** and **access control**, I performed several tasks to inspect and update file and directory permissions accordingly.

---

## Check File and Directory Details

To determine the existing permission settings, I used the `ls` command with the `-la` option:

```bash
ls -la projects
```

## Understanding the Permissions Command

The following command is used to inspect file and directory details:

```bash
ls -la
```

## This Command:

```bash
ls -la
```

## Performs the Following:

- Lists all files, **including hidden ones** (those starting with a dot `.`)
- Displays detailed metadata: **permissions**, **owners**, **file size**, and **modification date**

---

## Example Output Analysis

- `drafts/` → a **directory**  
- `.project_x.txt` → a **hidden file**  
- `project_t.txt`, `project_k.txt`, etc. → **regular files**

The first column in each output line shows a **10-character string** representing the file type and permission structure.

---

## Understanding the Permissions String

Permission strings follow this format: `-rwxrwxrwx`

| Position | Represents     | Description                                      |
|----------|----------------|--------------------------------------------------|
| 1st      | File Type      | `d` = directory, `-` = regular file              |
| 2–4      | User (Owner)   | `r` (read), `w` (write), `x` (execute)           |
| 5–7      | Group          | Same as above, for group members                 |
| 8–10     | Others         | Same as above, for all other system users        |

---

## Example:

```bash
-rw-rw-r--
```

## File Permission Breakdown

- `-` → Regular file  
- `rw-` → User has **read** and **write** permissions  
- `rw-` → Group has **read** and **write** permissions  
- `r--` → Others have **read-only** access  

---

## Change File Permissions

### Remove Write Access for Others

The organization decided that **others should not have write access**.

To remove write permission from `project_k.txt`, I used:

```bash
chmod o-w project_k.txt
ls -la project_k.txt
```

## Change Permissions on a Hidden File

The file `.project_x.txt` was archived and should be **read-only** for both the **user** and **group**.

```bash
chmod u-w .project_x.txt
chmod g-w .project_x.txt
chmod g+r .project_x.txt
ls -la .project_x.txt
```

**Changes Made to `.project_x.txt`**:

- Removed **write access** from **user**
- Removed **write access** from **group**
- Ensured **read access** remains for **group**

---

## Change Directory Permissions

Only the `researcher2` user should have **execute access** to the `drafts/` directory:

```bash
chmod g-x drafts
ls -la drafts
```

`g-x` removes execute permission from the **group**.

Since `researcher2` already had execute access, **no further changes were needed**.

---

## Summary

In this task, I:

- Used `ls -la` to inspect detailed file and directory permissions  
- Applied `chmod` to update access rights  
- Modified permissions for:

  - **Regular files**
  - **Hidden files**
  - **Directories**

These updates ensured that permission settings aligned with the organization’s **security policy**, maintaining proper **access control** across the system.

---

## Key Skills Demonstrated

- **Linux file system security**
- **Command-line proficiency**
- **Access control logic**
- Effective use of `chmod`, `ls`, and permission string interpretation

By executing these permission changes, I contributed to strengthening the **security posture** of the organization’s research infrastructure.
