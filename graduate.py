import smtplib
from email.mime.text import MIMEText 
account = "mzknchi18@gmail.com"
password = "momo8896"
to_email = "r32.perfume.180sx@gmail.com"
from_email = "mzknchi18@gmail.com"
subject = "テストメール"
message = "テストメール"
msg = MIMEText(message, "html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()
