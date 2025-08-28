from fpdf import FPDF
import base64

# Create instance of FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, 'Cowrie Honeypot Report', ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.multi_cell(0, 8, (
    "This report summarizes the activities captured by the Cowrie honeypot."
    " The honeypot was configured on an AWS EC2 instance and monitored SSH login attempts."
))

pdf.ln(5)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, 'Summary of Failed SSH Login Attempts', ln=True)

# Example failed login data
failed_logins = [
    {'timestamp': '2025-08-28T19:47:07.219370Z', 'src_ip': '51.20.253.43', 'username': 'fakeuser', 'password': 'hackmehackmehackme'},
    {'timestamp': '2025-08-28T19:47:20.201179Z', 'src_ip': '51.20.253.43', 'username': 'fakeuser', 'password': 'hackmeifucan'},
    {'timestamp': '2025-08-28T19:47:27.543293Z', 'src_ip': '51.20.253.43', 'username': 'fakeuser', 'password': 'hackmeifucan'}
]

# Table header
pdf.set_font("Arial", 'B', 12)
pdf.cell(50, 10, 'Timestamp', 1)
pdf.cell(40, 10, 'Source IP', 1)
pdf.cell(50, 10, 'Username', 1)
pdf.cell(50, 10, 'Password', 1)
pdf.ln()

# Table rows
pdf.set_font("Arial", '', 12)
for login in failed_logins:
    pdf.cell(50, 10, login['timestamp'], 1)
    pdf.cell(40, 10, login['src_ip'], 1)
    pdf.cell(50, 10, login['username'], 1)
    pdf.cell(50, 10, login['password'], 1)
    pdf.ln()

# Save PDF to file
pdf_file = 'cowrie_report.pdf'
pdf.output(pdf_file)
print(f'PDF generated: {pdf_file}')
