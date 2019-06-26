import smtplib

sender = "keshav.kummari@gmail.com"

receivers = "keshavckk@gmail.com"

message = """
From: KK <keshav.kummari@gmail.com>
To: keshavckk@gmail.com
MIME-Version: 1.0
Content-type: text/html
Subject: Email Test

<b>This is Test mail</b>
<h1>This is Headline</h1>
"""

try:
    smtpObject = smtplib.SMTP('smtp.gmail.com',587)
    smtpObject.sendmail(sender,receivers,message)
    print("Email has been sent Successfully!")
except Exception as e:
    print("Due to {e} mail was not delivered!")
