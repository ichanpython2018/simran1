import smtplib
   sender = 'simran.nielit@gmail.com'
   toaddrs = 'simran.nielit@gmail.com'
   msg = 'Why,Oh why!'
   username = 'user_me@gmail.com'
   password = 'pwd'
   server = smtplib.SMTP('smtp.gmail.com:587')
   server.starttls()
   server.login(simran.nielit@gmail.com, password)
   server.sendmail(sender, toaddrs, msg)
   server.quit()

'''sender = 'simran.nielit@gmail.com'
receivers = ['simran.nielit@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.server()
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except Exception:
   print ("Error: unable to send email")'''
