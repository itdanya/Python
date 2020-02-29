import smtplib
import codecs
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


sender = 'admin@example.com'
receiver = 'oshkindo@uromgaz.ru'

msg = MIMEMultipart()

msg['Subject'] = 'Test mail with attachment'
msg['From'] = sender
msg['To'] = receiver

filename = 'backup.txt'

with codecs.open(filename, 'r', 'utf-8') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

user = 'username'
password = 'password'

with smtplib.SMTP("zimbra.urom.local", 25) as server:

#    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("Successfully sent email")
