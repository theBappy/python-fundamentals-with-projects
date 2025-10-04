import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
                   
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, recipient_email, msg.as_string())
        
        print("✅Email sent successfully!") 
                   
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    recipient = "example@gmail.com"
    subject = "Test email from Python world"
    body = "This is a test email sent using Python and Gmail SMTP."
    send_email(recipient, subject, body)