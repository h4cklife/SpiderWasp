"""

Reusables


"""

import config
import os
import sys
import http.client
import json
import subprocess
import smtplib
import copy
import re
from twilio.rest import Client
from datetime import date, datetime, timedelta
from time import sleep, strftime, gmtime, time


now = datetime.now()
f = '%Y-%m-%d %H:%M:%S'

def write_log(log):
    """
    write_log(log)
    :param log:
    :return:

    Save a log
    """
    if config.SERVICE_LOGS:
        fh = open('log/service.log', 'a')
        fh.write("[{}] {} {}".format(now.strftime(f), log, '\n'))
        fh.close()

def write_error(log):
    """
    write_error(log)
    :param log:
    :return:

    Save a log
    """
    if config.SERVICE_LOGS:
        fh = open('log/error.log', 'a')
        fh.write("[{}] {} {}".format(now.strftime(f), log, '\n'))
        fh.close()

def write_alert(log):
    """
    write_alert(log)
    :param log:
    :return:

    Save a log
    """
    if config.ALERT_LOGS:
        fh = open('log/alert.log', 'a')
        fh.write("[{}] {} {}".format(now.strftime(f), log, '\n'))
        fh.close()

def send_twilio_sms(to, message):
    """
    send_twilio_sms(to, message)
    :param to:
    :param message:
    :return:

    Send a SMS message to the client using our Twilio API
    This is basically, what Shadowfeed is charging users for. Message delivery.
    """
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    message_instance = client.messages.create(
        to="+{}".format(to),
        from_=config.TWILIO_NUMBER,
        body=message)

    write_alert("[TWILIO-ALERT] Sent to {0} : {1}".format(to, message))

    return message_instance.sid

def sendmail(to, body):
    """
    _sendmail(to, body)

    :param to:
    :param body:
    :return:

    Send an email

    """
    if config.EMAIL_ALERTS:
        sent_from = "{0}@{1}".format(config.SMTP_USER, config.SMTP_DOMAIN)
        subject = '{0} - Threat Identification'.format(config.APP)

        email_text = """  
        From: {0}\nTo: {1}\nSubject: {2}\n\n{3}
        """.format("{0}@{1}".format(config.SMTP_USER, config.SMTP_DOMAIN), to, subject, body)

        try:
            server = smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT)
            server.ehlo()
            server.login("{0}@{1}".format(config.SMTP_USER, config.SMTP_DOMAIN), config.SMTP_PASS)
            server.sendmail("{0}@{1}".format(config.SMTP_USER, config.SMTP_DOMAIN), to, email_text)
            server.close()
            write_alert("[EMAIL-ALERT] Sent to {0} : {1}".format(to, body))
        except Exception as e:
            write_log("Something went wrong sending email : {0}".format(e))
