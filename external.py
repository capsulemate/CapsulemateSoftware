import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendemail(to_addr_list):
    msg = MIMEMultipart()
    msg['Subject'] = "Medication not taken by John Doe"
    msg['From'] = "capsulematefydp@gmail.com"
    msg['To'] = to_addr_list
    body = "Hello, patient John Doe has not taken his medication scheduled for x, Regards, CapsuleMate"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login("capsulematefydp","!9Hdq!3cBEAa")
    text = msg.as_string()
    problems = server.sendmail('capsulematefydp@gmail.com', to_addr_list, text)
    print(problems)
    server.quit()

