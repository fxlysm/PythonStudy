#coding:utf-8

import  smtplib
from email.mime.text import MIMEText


msg = MIMEText(''
              '<html><head><title>by Python</title><head><body><h1><a href="http://www.python.org">Python by God</a></h1></body></html>',
              'html',
              'utf-8')
msg ['From']="814380399@qq.com"
msg ["To"]="814380399@qq.com"
msg['Subject']="python test"

server =smtplib.SMTP_SSL('smtp.qq.com',465)
server.set_debuglevel(1)
server.login("814380399@qq.com","gswqijotycjjbgba")  # 后面为授权码  在开通SMTP

server.sendmail("814380399@qq.com",["814380399@qq.com"],msg.as_string())

server.quit()