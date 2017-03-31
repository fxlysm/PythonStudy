#coding:utf-8

import  smtplib
from email.mime.text import MIMEText
from  email.mime.multipart import  MIMEMultipart
msg = MIMEMultipart()
fj1=MIMEMultipart(open('123.txt','rb').read(),'base64','gbk')
fj1["CONTENT-TYPE"]='application/octet-stream'
fj1['Content-Disposition'] = 'attachment';filename="123.txt"
msg.attach(fj1)

msg ['From']="814380399@qq.com"
msg ["To"]="814380399@qq.com"
msg['Subject']="python test"

server =smtplib.SMTP_SSL('smtp.qq.com',465)
server.set_debuglevel(1)
server.login("814380399@qq.com","gswqijotycjjbgba")  # 后面为授权码  在开通SMTP

server.sendmail("814380399@qq.com",["814380399@qq.com"],msg.as_string())

server.quit()