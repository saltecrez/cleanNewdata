#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "January 2020"

import gzip
import smtplib
import hashlib
import email.utils
from email.mime.text import MIMEText
from logging_class import LoggingClass

log = LoggingClass('',True).get_logger()

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
        try:
            server = smtplib.SMTP(self.smtphost, 25)
        except Exception as e:
            msg = "SMTP connection excep - SendEmail.send_email -- " 
            log.error("{0}{1}".format(msg,e))
        else:
            server.sendmail(self.sender, [self.recipient], msg.as_string())
            server.quit()

class md5Checksum(object):
    def __init__(self, filename):
        self.filename = filename

    def calculate_checksum(self):
        try:
            hash_md5 = hashlib.md5()
            if self.filename is None:
                pass
            else: 
                with open(self.filename, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
                return hash_md5.hexdigest()
        except Exception as e:
            msg = "Checksum calculation excep - md5Checksum.calculate_checksum -- "
            log.error("{0}{1}".format(msg,e))

    def get_checksum_gz(self):
        try:
            fopen = gzip.open(self.filename, 'rb')
            fcontent = fopen.read()
            chks = hashlib.md5(fcontent).hexdigest()
            fopen.close()
            return chks
        except Exception as e:
            msg = "Checksum calculation excep - md5Checksum.get_checksum_gz -- "
            log.error("{0}{1}".format(msg,e))

if __name__ == "__main__":
    recipient = 'londero@oats.inaf.it'
    sender = 'archivio@hactar' 
    smtphost = 'mal.oapd.inaf.it'  
    msg = 'Severe alert'
  
    SendEmail(msg,recipient,sender,smtphost).send_email()
    print(md5Checksum('/home/archivio/development/cleanNewdata/Schmidt/SC116457.fits').calculate_checksum())
