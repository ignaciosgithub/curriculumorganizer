import smtplib
import time
import imaplib
import email
import os

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail():
    ORG_EMAIL   = "@gmail.com"
    FROM_EMAIL  = "yourEmailAddress" + ORG_EMAIL
    FROM_PWD    = "yourPassword"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT   = 993  
    for a in os.listdir('.'):
        if "CurrentGmail" in a:
            FROM_EMAIL  = a.replace("CurrentGmail","") + ORG_EMAIL
        if "CurrentPassword" in a:
            FROM_PWD = a.replace("CurrentPassword","")
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        print(FROM_EMAIL)
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    bd =""
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body = msg
                    #print 'From : ' + email_from + '\n'
                    #print 'Subject : ' + email_subject + '\n'
                    #print msg
                    if msg.is_multipart():
                        for pl in msg.get_payload():
                            bd = bd+ pl.as_string()
                    else:
                        bd = msg.get_payload()
    
                    return email_from, email_subject, bd
    except Exception, e:
        print str(e)
