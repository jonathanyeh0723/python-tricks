import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email:

    def __init__(self, sender_address, sender_passwd):
        self.sender_address = sender_address
        self.sender_passwd = sender_passwd

    def send(self, receiver_address, subject, content, attach_file_name):

        message = MIMEMultipart()
        message['From'] = self.sender_address
        message['To'] = receiver_address
        message['Subject'] = subject

        message.attach(MIMEText(content, 'plain'))
        attach_file = open(attach_file_name, 'rb')

        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Disposition', 'attachment',
                           filename=attach_file_name)
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.sender_address, self.sender_passwd)
        text = message.as_string()
        session.sendmail(self.sender_address, receiver_address, text)
        session.quit()

        return f'Send email to {receiver_address}.'
