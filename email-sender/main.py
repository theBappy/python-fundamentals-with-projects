import smtplib
import os

username = os.environ["username"]
password = os.environ["user_password"]

receiver_email = "example@gmail.com"

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo() #ESMTP protocol

smtp_server.starttls() #setting up to TLS connection

smtp_server.ehlo()


smtp_server.login(username, password)

msg_to_be_sent = "Hey how are you, I hope you are doing well! 💖"

smtp_server.sendmail(username, receiver_email, msg_to_be_sent)

smtp_server.quit()

