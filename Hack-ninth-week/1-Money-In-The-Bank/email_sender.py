from tayna import from_email, email_psd
import smtplib
from email.mime.text import MIMEText


class Email_Sender:
    @staticmethod
    def send_email(to_email, msg_text):
        msg = MIMEText(msg_text)
        msg['Subject'] = 'Reset Password Python Hack'
        msg['To'] = to_email
        msg['From'] = from_email
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(from_email, email_psd)
        server.send_message(msg)
        server.quit()
