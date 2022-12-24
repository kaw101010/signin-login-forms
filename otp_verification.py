import math
import random
import smtplib
from config import origin_mail, origin_pw, port, time
from email.message import EmailMessage

def otp():
    dig =  "0123456789"
    otp = ""
    # 5 digit OTP generation
    for i in range(5):
        otp += random.choice([i for i in dig])
    return otp

def otp_ver(mail):
    server = smtplib.SMTP('smtp.gmail.com', port, timeout = time)
    server.starttls()
    msg = EmailMessage()
    code = otp()
    # Subject for email
    msg['Subject'] = "OTP for Email Verification"
    msg['From'] = origin_mail
    msg['To'] = mail
    # Email content
    msg.set_content(f'Hi. Welcome to your journey. \nYour OTP is {code}.\nDo not share your OTP with anyone. \nRegistered Email.')
    server.login(origin_mail,origin_pw)
    # Message sent
    server.send_message(msg)
    server.quit()
    return code
