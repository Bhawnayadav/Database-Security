# -*- coding: utf-8 -*-


import  smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "ALERT"
body = "This is an Security System Alert. Kindly look for the attachement and do the required steps "
sender_email = "Secure.DBsystem@gmail.com "
receiver_email = "Secure.DBsystem@gmail.com "
password = "vitbhopal "

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

filename = "Alert.pdf"  

with open('Log_Report.pdf ', "rb") as attachment:

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
  
encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text) 

print('\n ') 
print('---EMAIL SEND TO THE EMAIL-ID. KINDLY CHECK---' )
print('\n')