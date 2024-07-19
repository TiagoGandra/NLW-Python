import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "lyj6e5njyd4uywye@ethereal.email"
    login = "lyj6e5njyd4uywye@ethereal.email"
    password = "zS3DsrJtnpkFdFKrtA"

    msg = MIMEMultipart()
    msg["from"] = "trips_confirmer@email.com"
    msg["to"]= ', '.join(to_addrs)

    msg["Subject"] = "Trip confirmation!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()