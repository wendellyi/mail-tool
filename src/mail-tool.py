#! /usr/bin/env python
# coding: utf-8

import os
import sys
from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import getopt

def usage():
    print "使用:"
    print "\t%s -f haha@163.com -p xixi -a file.txt -t heihei@163.com -s \"this is a test\"" % (sys.argv[0])

def sendFildByMail(config):
    message = MIMEMultipart()
    message['from'] = config['from']
    message['to'] = config['to']
    message['Reply-To'] = config['from']
    message['Subject'] = config['subject']
    message['Date'] = time.ctime(time.time())

    message['X-Priority'] = '3'
    message['X-MSMail-Priority'] = 'Normal'
    message['X-Mailer'] = 'wendell client'
    message['X-MimeOLE'] = 'product by wendell client v1.0.00'

    # 注意这一段
    f = open(config['file'], 'rb')
    file = MIMEApplication(f.read())
    f.close()
    file.add_header('Content-Disposition', 'attachment',
                    filename = os.path.basename(config['file']))
    message.attach(file)
    smtp = SMTP(config['server'], config['port'])
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(config['username'], config['password'])

    print 'OK'
    print 'Send ...'

    smtp.sendmail(config['from'], [config['from'], config['to']], message.as_string())

    print 'OK'
    smtp.close()

if __name__ == '__main__':
    SUBJECT = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:p:t:a:s:h', ['from=', 'password=', 'to=', 'attach=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit()

    for opt, value in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-f", "--from"):
            FROM = value
        elif opt in ("-p", "--password"):
            PASSWORD = value
        elif opt in ("-t", "--to"):
            TO = value
        elif opt in ("-a", "--attach"):
            ATTACH = value
        elif opt in ("-s", "--subject"):
            SUBJECT = value

    username = FROM.split("@")[0]
    domain = FROM.split("@")[1]
    smtp_server = "smtp.%s" % domain

    if 0 == len(SUBJECT):
        SUBJECT = "send by python"

    parameter = {
        'from': FROM,
        'to': TO,
        'subject': SUBJECT,
        'file': ATTACH,
        'server': smtp_server,
        'port': 25,
        'username': username,
        'password': PASSWORD}
    print parameter        
    sendFildByMail(parameter)
        
