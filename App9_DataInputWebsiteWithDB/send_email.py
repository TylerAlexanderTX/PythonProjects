from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="test@gmail.com"
    from_password="testpass"
    to_email=email

    subject="Height Data"
    message="Hello, your height is <strong>%s</strong>. Average height is %s. Number of polls taken: %s" % (height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)