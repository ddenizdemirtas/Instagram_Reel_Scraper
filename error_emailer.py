import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the email message
sender_email = 'your_email@example.com'
receiver_email = 'recipient_email@example.com'
subject = 'Test email'
message = 'This is a test email sent from Python.'

# Create a MIME message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the MIME object
msg.attach(MIMEText(message, 'Code errored'))

# Connect to the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'denizdemirtas@berkeley.edu'
smtp_password = 'PradaBagCauseTheyPradaMe03_'

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Send the email
text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)
server.quit()

print('Email sent.')
