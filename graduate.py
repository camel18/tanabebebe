import sqlite3
import smtplib
from email.mime.text import MIMEText 

# con = sqlite3.connect('./necocchi.db')
# cur = con.cursor()
# cur.execute("SELECT * FROM users where password = ?")
# connection.commit()
# connection.close()

account = "necocchi.help@gmail.com"
password = "necocchi"
to_email = "r32.perfume.180sx@gmail.com"
from_email = "necocchi.help@gmail.com"
subject = "パスワードのお知らせです"
body = "あなたのパスワードを通知します。 <br> <br> password <br> <br> このパスワードは大切に保管してください。"
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()
