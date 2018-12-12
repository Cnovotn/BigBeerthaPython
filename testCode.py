from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from instagram.client import InstagramAPI
import requests, json 
import smtplib
import os,email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

import Algorithmia

input = {
  "format": "SplitToSubvideos",
  "data": {
      "input": {
          "inputVideoUrl": "data://pixvana/examples/Baseball_Stadium_Fly_Over.mp4"
    },
      "output": {
          "collection": "data://.algo/temp",
          "prefix": "baseballSubVideos",
          "extension": "mp4",
          "zippedOutput": False
    }
  }
}
client = Algorithmia.client('simmCXDB77PoR6mqaxg8E5T/mDf1')
algo = client.algo('media/VideoAlgorithms/0.2.5')
print(algo.pipe(input).result)

# def send_mail(send_from, send_to, subject, text, file):
    
#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = send_to
#     msg['Date'] = " Use any date time module to insert or use email.utils formatdate"
#     msg['Subject'] = subject
    
#     msg.attach( MIMEText(text) )
#     part = MIMEBase('application', "octet-stream")
#     fo=open(files,"rb")
#     part.set_payload(fo.read() )
#     Encoders.encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
#     msg.attach(part)

#     smtp = smtplib.SMTP("smtp.gmail.com",587) #Email id  for yahoo use smtp.mail.yahoo.com
#     smtp.ehlo()
#     smtp.starttls  #in yahoo use smtplib.SMTP_SSL()
#     smtp.ehlo()
#     smtp.login("ur id","password") #Edit
#     sent=smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.close()
#     return sent
    

# s=send_mail("clayton-oscar@msn.com","clayton-novotney@msn.com","Mail test","Message","Path to file")  # Edit
# if (s.keys()==[]):
#     print "Message Sent!!!!!!!!!"
# else:
#     print "Error!!!!"