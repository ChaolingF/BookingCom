import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(to_mail,hotel_name,price):
    host = "smtp.gmail.com"
    port = 587
    mail_username = "erf81102@gmail.com"
    from_mail = mail_username
    mail_password = "XXXX"

    email_conn = smtplib.SMTP(host, port)
    email_conn.starttls()
    email_conn.login(mail_username, mail_password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "The Price of " + hotel_name
    msg['From'] = from_mail
    msg['To'] = to_mail
    mail_content = "The Price of " + hotel_name + " is: " + price
    content = MIMEText(mail_content,'plain','utf-8')
    msg.attach(content)

    email_conn.sendmail(mail_username, to_mail, msg.as_string())
    email_conn.quit()