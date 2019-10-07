"""

CONFIGURATIONS

"""

""" SPIDERWASP CONFIGURATION """

APP             = "SpiderWasp"
USER_AGENT      = 'SWv0.5'
EMAIL_ALERTS    = True
TWILIO_ALERTS   = True
SERVICE_LOGS    = True
ALERT_LOGS      = True
THREAD_COUNT    = 1

""" TWILIO CONFIGURATION """

TWILIO_ACCOUNT_SID      = ''
TWILIO_AUTH_TOKEN       = ''
TWILIO_NUMBER           = ''
TWILIO_TEST_SID         = ''
TWILIO_TEST_AUTH_TOKEN  = ''

""" 
SEND MAIL CONFIGURATION 

Requires App Password, and Less Secure Apps 

App Password : https://support.google.com/mail/?p=InvalidSecondFactor
Less Secure  : https://support.google.com/accounts/answer/6010255#more-secure-apps

"""

SMTP_HOST   = "smtp.gmail.com"
SMTP_PORT   = 465
SMTP_DOMAIN = "gmail.com"
SMTP_USER   = ""
SMTP_PASS   = ""