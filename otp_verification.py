import os
import math
import random
import smtplib
from config import origin_mail, origin_pw, port

def otp():
    dig =  "0123456789"
    otp = ""
    for i in range(5):
        otp += random.choice([i for i in dig])
    return otp

email_send = smtplib.SMTP('smtp.gmail.com', port)
email_send.starttls()

def otp_ver(mail):
    email_send.login(origin_mail,origin_pw)
    code = otp()
    email_send.sendmail(origin_mail,mail,f"Hi. Welcome to your journey. \nYour OTP is {code}\n. Registered Email send through SMTPLIB")
    check = input("Enter OTP: ")
    if check == code:
        return True
    else:
        return False



