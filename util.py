#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "January 2020"


'''

vautare un machine name in entrata per rendere le allerte generiche

'''
import os
import sys
import smtplib
import hashlib
import subprocess
import email.utils
from email.mime.text import MIMEText

class VerifyLinux(object):
    assert ('linux' in sys.platform), "Function can only run on Linux systems."

class SendEmail(object):
    def __init__(self, message, recipient, sender, smtphost):
        self.message = message
        self.recipient = recipient
        self.sender = sender
        self.smtphost = smtphost
    
    def send_email(self):
        hostname = self.sender.split("@",1)[1].title() 
        msg = MIMEText(self.message)
        msg['To'] = email.utils.formataddr(('To', self.recipient))
        msg['From'] = email.utils.formataddr((hostname+'WatchDog', self.sender))
        msg['Subject'] = hostname + ' alert'
        server = smtplib.SMTP(self.smtphost, 25)
        server.sendmail(self.sender, [self.recipient], msg.as_string())
        server.quit()

class md5Checksum(object):
    def __init__(self, filename):
        self.filename = filename

    def calculate_checksum(self):
        hash_md5 = hashlib.md5()
        with open(self.filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

if __name__ == "__main__":
    VerifyLinux()
    recipient = 'londero@oats.inaf.it'
    sender = 'archivio@hactar' 
    smtphost = 'mail.oapd.inaf.it'  
    msg = 'Severe alert'
  
    print(VerifyLinux())
    #SendEmail(msg,recipient,sender,smtphost).send_email()
    #print(md5Checksum('/home/archivio/development/cleanNewdata/Schmidt/SC116314.fits.gz').calculate_checksum())
