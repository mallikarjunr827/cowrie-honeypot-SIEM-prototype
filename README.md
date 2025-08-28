-> Cowrie Honeypot SIEM

-Overview
This project implements a **Cowrie honeypot** deployed on an AWS EC2 instance to monitor and log SSH login attempts. The honeypot captures attacker IP addresses, usernames, and passwords, storing them in **JSON** and **CSV** formats, and generates a **PDF report** summarizing the failed login attempts. The project serves as a lightweight **Security Information and Event Management (SIEM)** tool for detecting and analyzing malicious activity targeting SSH services.

-Features
- Deploy Cowrie honeypot on AWS EC2 or any Linux environment
- Capture live SSH connection attempts from attackers
- Record attacker credentials and session details in structured logs
- Export failed login attempts to CSV for further analysis
- Generate an automated PDF report summarizing attacker activity
- Easily integrable with SIEM tools or monitoring dashboards
- Provides insights for cybersecurity training, research, or threat intelligence

-Files
- `cowrie.json` – Raw JSON log of honeypot activity
- `all_logs.json` – Consolidated logs for analysis
- `failed_logins.csv` – CSV of failed SSH login attempts
- `parse_cowrie_logs.py` – Python script to parse JSON logs
- `export_failed_logins.py` – Python script to export CSV
- `cowrie_report.pdf` – Generated PDF report summarizing failed logins
