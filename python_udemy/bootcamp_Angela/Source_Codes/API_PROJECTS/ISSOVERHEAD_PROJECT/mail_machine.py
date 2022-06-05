import smtplib
from email.mime.text import MIMEText

class Sendemail:
    def __init__(self, mail_subject, contents):
        self.my_email = "leeky16498@gmail.com"
        self.my_password = "tfcawoypiogozmwh"
        self.mail_subject = mail_subject
        self.contents = contents
    
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.my_email, self.my_password)

        msg = MIMEText(self.contents)
        msg['Subject'] = self.mail_subject

        smtp.sendmail(self.my_email, 'ssahri@naver.com', msg.as_string())
        smtp.close()
