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

-Overview of Installation(not completed instrections)
1. Launch an **Ubuntu AWS EC2 instance** or any Linux machine.
2. Update your system:
```bash
sudo apt update && sudo apt upgrade -
- Install Python 3 and required libraries
sudo apt install python3 python3-pip -y
pip3 install fpdf

- Clone this repository
git clone <your-repo-url>
cd cowrie-honeypot-siem
 - Usage

-Start the Cowrie honeypot:

cd ~/cowrie
source cowrie-env/bin/activate
./start.sh

-Monitor live logs:

tail -f ~/cowrie/var/log/cowrie/cowrie.log


Export failed login attempts to CSV:

python3 export_failed_logins.py

-Generate a PDF report of failed logins:

python3 generate_pdf_report.py

--Example Output

CSV Output (failed_logins.csv):

timestamp,src_ip,username,password
2025-08-28T19:47:07.219370Z,51.20.253.43,fakeuser,hackmehackmehackme
2025-08-28T19:47:20.201179Z,51.20.253.43,fakeuser,hackmeifucan
2025-08-28T19:47:27.543293Z,51.20.253.43,fakeuser,hackmeifucan

