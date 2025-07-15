import smtplib
from email.message import EmailMessage

# Sender email credentials
sender_email = "sidhbabulal70@gmail.com"
sender_password = "wyznxmjohcykicnt"  # ⚠️ Use App Password, not your main password

# Receiver's email
receiver_email = "babulalsidhsidh@gmail.com"

# Create EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Test Email from Python'
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content('Hello! This is a test email sent from a Python script.')

# Send email using Gmail SMTP server
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Failed to send email: {e}")

