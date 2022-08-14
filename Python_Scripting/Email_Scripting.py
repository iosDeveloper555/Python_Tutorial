import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You '''

#The mail addresses and password
sender_address = 'iosdeveloperamarendrabaitha@gmail.com'
sender_pass = 'Akumar@123'
receiver_address = 'kumaramarendra555@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')



'''
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


receiver_email = 'kumaramarendra555@gmail.com'
sender_email = 'iosdeveloperamarendrabaitha@gmail.com'
html = Template(Path('/Users/apple/Documents/Python/PyCharm_Project/Python_Scripting/index.html').read_text())
email = EmailMessage()
email['to'] = receiver_email
email['subject'] = 'Congt! Email from python!'

email.set_content(html.substitute({'name' : 'Amarendra'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

    smtp.ehlo()
    smtp.starttls()

    smtp.login(sender_email, 'Akumar@123')
    smtp.send_message(email)
    print("All good dear!")

'''