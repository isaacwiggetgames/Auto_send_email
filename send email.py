import smtplib
from email.message import EmailMessage

# Email credentials
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password"  # Use an app password, NOT your real password

# Create the email
msg = EmailMessage()
msg["Subject"] = "Automated Email"
msg["From"] = EMAIL_ADDRESS # title of message
msg["To"] = "recipient@example.com"
msg.set_content("Hello, this is an automated email sent from Python!") # the message it sends

# Connect to SMTP server and send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Use the appropriate SMTP server
    server.starttls()  # Secure connection
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")
