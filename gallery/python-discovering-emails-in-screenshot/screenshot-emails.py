# Take screen shots
from PIL import Image
from PIL import ImageGrab
# Read environment variables
import os
# Parse HTML
import requests
import smtplib
# Send emails
from email.mime.text import MIMEText
# Regular expression parsing
import re
# convert image to text
from pytesseract import image_to_string

def get_emails() :
    """Take a screen shot, convert it to text, and return a list of emails"""
    # Take a screenshot
    screenshot = ImageGrab.grab()
    # Convert to text
    text = image_to_string(screenshot)
    # Parse text for email addresses
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return emails

def validate(addresses) :
    """Validate each address with an API, and return a list of valid addresses"""
    # Get a list of valid email addresses
    valid_addresses = []
    for address in addresses :
        # Validate email address
        response = requests.get('https://api.mailgun.net/v3/address/validate',
                                auth=('api', os.environ['MAILGUN_API_KEY']),
                                params={'address': address})
        # Check for valid email address
        if response.json()['is_valid'] :
            valid_addresses.append(address)
    return valid_addresses

# Get the sender and password from the environment variables
sender = os.environ['SENDER']
password = os.environ['PASSWORD']

def send_message(emails, subject, body) :
    """Send the message to all emails"""
    # Create a message
    message = MIMEText(body)
    # Set the subject
    message['Subject'] = subject
    # Set the sender
    message['From'] = sender
    # Set the recipients
    message['To'] = ', '.join(emails)
    # Send the message
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, emails, message.as_string())
    server.quit()

emails = get_emails()
valid_addresses = validate(emails)
if len(valid_addresses) > 0 :
    send_message(valid_addresses, 'New Email', 'New emails: ' + ', '.join(valid_addresses))

"oege.demoor@gmail.com , oedemoor@microsoft. , demooroege@gmail.com"
