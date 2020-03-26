import smtplib
from email.mime.text import MIMEText
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    # SMTP service
    mail_host = "smtp.163.com"  # SMTP server
    mail_user = "zhangzheming_282@163.com"  # username
    mail_pass = os.getenv('pass')  # password

    sender = 'zhangzheming_282@163.com'  # sender
    receivers = []  # receiver
    emails = request.GET.get('l').split(',')
    
    if len(emails) == 1:
        receivers.append(emails[0])
    elif len(emails) > 1:
        for i in emails:
            receivers.append(i)
    print(receivers)
    print(type(emails))
    print(emails)

    content = request.GET.get('content')
    print(content)
    # content = 'Python Send Mail !'
    title = 'Azure Server Alert info'  # topic
    message = MIMEText(content, 'plain', 'utf-8')  # content
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # ssl
        smtpObj.login(mail_user, mail_pass)  # valid
        smtpObj.sendmail(sender, receivers, message.as_string())  # send
        return HttpResponse('mail has been send successfully.')
    except smtplib.SMTPException as e:
        return HttpResponse('error is :' + str(e))
