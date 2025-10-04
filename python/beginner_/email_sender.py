from email.message import EmailMessage
import ssl
import smtplib

email_sender = "thebappy575@gmail.com"
email_password = "skjl kbyn betz ztgq"

email_receiver = "xadak84072@gddcorp.com"
subject = "Python Email Sender"
body = """
    This is a email sender testing by Python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



