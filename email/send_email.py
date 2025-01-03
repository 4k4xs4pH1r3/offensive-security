import smtplib
import dns.resolver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import re
import getpass

def analyze_dkim_failure(headers):
    """
    Analyzes Google DKIM-Signature header to identify potential reasons for DKIM authentication failure.

    Args:
        headers (dict): A dictionary of email headers.

    Returns:
        str: A string describing the potential reason for DKIM failure.
    """
    try:
        dkim_signature = headers['DKIM-Signature']
    except KeyError:
        return "DKIM-Signature header missing."

    try:
        # Split the DKIM-Signature header into its parts
        dkim_parts = dict(item.split('=', 1) for item in dkim_signature.split('; '))

        # Check if the 'd=' tag matches the 'From' domain
        from_domain = re.search(r'@(.*)', headers['From']).group(1)
        dkim_domain = dkim_parts.get('d')
        if dkim_domain != from_domain:
            return f"DKIM domain mismatch: 'd={dkim_domain}' does not match 'From' domain '{from_domain}'"

        # Check if the 's=' tag matches a valid selector in DNS
        dkim_selector = dkim_parts.get('s')
        try:
            dns.resolver.resolve(f'{dkim_selector}._domainkey.{dkim_domain}', 'TXT')
        except dns.resolver.NXDOMAIN:
            return f"Invalid DKIM selector: '{dkim_selector}._domainkey.{dkim_domain}' not found in DNS"

    except ValueError as e:
        return f"Error parsing DKIM-Signature header: {e}"

    return "Unknown DKIM failure reason."


def send_email(sender_email, sender_password, receiver_email, subject, body):
    """
    Sends an email with DKIM signature.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        receiver_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body.
    """
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == '__main__':
    # Email details
    sender_email = 'yourname@yourdomain.com'
    sender_password = getpass.getpass("Enter your email password: ")
    receiver_email = 'yourrecipiennt@gmail.com'
    subject = 'Test DKIM 1213'
    body = 'This is the email body.'

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body)

    # Analyze DKIM failure (replace with actual email headers)
    headers = {
        'From': 'yourname@yourdomain.com',
        'DKIM-Signature': 'v=1; a=rsa-sha256; d=gmail.com; s=20210112; c=relaxed/relaxed; q=dns/txt; i=@gmail.com; t=1678687600; h=From:To:Subject:Date:Message-ID; bh=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx; b=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    }
    failure_reason = analyze_dkim_failure(headers)
    print(f"Potential DKIM failure reason: {failure_reason}")

    # Open the default browser to authenticate with Google
    webbrowser.open('https://accounts.google.com/signin')
