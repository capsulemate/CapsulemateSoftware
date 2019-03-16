import smtplib
import credentials
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def time(): 
    currentDT = datetime.datetime.now()
    return currentDT.strftime("%Y-%m-%d %H:%M:%S")

def sendemail(to_addr_list, med_name):
    msg = MIMEMultipart()
    msg['Subject'] = "Medication not taken by John Doe"
    msg['From'] = "capsulematefydp@gmail.com"
    msg['To'] = to_addr_list
    current_time = time()
    body = "Hello, patient John Doe has not taken his medication: {} scheduled to be taken by: {}".format(med_name,current_time)  + "\n  \n Regards, CapsuleMate"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    password = credentials.login['password']
    server.login("capsulematefydp", password)
    text = msg.as_string()
    problems = server.sendmail('capsulematefydp@gmail.com', to_addr_list, text)
    print(problems)
    server.quit()


