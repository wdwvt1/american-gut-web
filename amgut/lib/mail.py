from __future__ import division

import smtplib
from email.mime.text import MIMEText
from amgut import media_locale
from amgut.lib.config_manager import AMGUT_CONFIG




def send_email(message, subject, recipient='americangut@gmail.com',
               sender=media_locale['HELP_EMAIL']):
    """Send an email from your local host """

    # Create a text/plain message
    msg = MIMEText(message)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    if AMGUT_CONFIG.smtp_ssl:
        smtplib.SMTP_SSL()
    else:
        s = smtplib.SMTP()
    s.connect(AMGUT_CONFIG.smtp_host, AMGUT_CONFIG.smtp_port)
    # try tls, if not available on server just ignore error
    try:
        s.starttls()
    except smtplib.SMTPException:
        pass
    s.ehlo_or_helo_if_needed()

    if AMGUT_CONFIG.smtp_user:
        s.login(AMGUT_CONFIG.smtp_user, AMGUT_CONFIG.smtp_password)

    s.sendmail(sender, [recipient], msg.as_string())
    s.quit()
