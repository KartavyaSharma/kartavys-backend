"""
SendGrid mail handler, sends emails to kartavyas and senders
"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def html_client_gen(target_name, target_email):
    """
    Generates HTML for mailing to client.

    :target_name:       (string) First name of sender
    :target_email:      (string) Email of sender

    :return: HTML template as an fstring to be used with SendGrid's API service
    """
    content = f''
    with open('web/sendgrid_mailers/templates/client.html', 'r') as f:
        for line in f.readlines():
            content+=line
    return content


def html_home_gen(fname, lname, email, message):
    """
    Generates HTML for mailing to private blog owner creator email ID.

    :fname:     (string) First name of sender
    :lname:     (string) Last name of sender
    :email:     (string) Email of sender
    :message:   (string) Message from sender

    :return: HTML template as an fstring to be used with SendGrid's API service
    """
    content = f''
    with open('web/sendgrid_mailers/templates/home.html', 'r') as f:
        for line in f.readlines():
            content+=line
    return content


def home_mailer(first_name, last_name, email, message):
    message = Mail(
        from_email=os.environ.get('SENDER'),
        to_emails=os.environ.get('TARGET'),
        subject='Sending with Twilio SendGrid is Fun',
        html_content=html_home_gen(first_name, last_name, email, message)
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return True 
    except Exception as e:
        return {'False': e.message}


def client_mailer(client_name, client_email):
    message = Mail(
        from_email=os.environ.get('SENDER'),
        to_emails=f'{client_email}',
        subject='Successful form submission on kartavyas.com!',
        html_content=html_client_gen(client_name, client_email)
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return True
    except Exception as e:
        return {'False': e.message}


