from flask import current_app
from flask_mail import Message

TestMessage = Message(
    "Test subject", 
    sender = config.mail.get('FROM'), 
    body='',
    html='',
)