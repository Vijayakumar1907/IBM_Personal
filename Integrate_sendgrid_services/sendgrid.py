import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='sujiths12340@gmail.com',
    to_emails='sujith2435@gmail.com',
    subject='Sending this for your Fashion Strike',
    html_content='<strong>Here is your Fashion Recommender which will helps you to be perfect to impress</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)