import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import urlencode
import os

SMTP_SERVER = 'mail.hasten.shop'
SMTP_PORT = 587
SMTP_USERNAME = 'hello@hasten.shop'
SMTP_PASSWORD = 'Hasten123456$'
SENDER_EMAIL = 'hello@hasten.shop'
RECIPIENT_EMAIL = 'hastensports@outlook.com'

def send_promo_email(name, email):
    
    # Get the path to the 'email_confirmation.html' file in the 'templates' folder
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'email_promo.html')

    with open(template_path, 'r') as file:
        html_content = file.read()

    # Replace placeholders in the HTML content with actual values
    html_content = html_content.replace('{name}', name)
    html_content = html_content.replace('{email}', email)

    # Create the user's email message
    user_subject = 'HAS10 - Your Exclusive Promo Code is Here! 🌟'
    user_message = MIMEMultipart()
    user_message['From'] = SENDER_EMAIL
    user_message['To'] = email
    user_message['Subject'] = user_subject
    user_message.attach(MIMEText(html_content, 'html'))

    # Send email emails
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, user_message.as_string())

