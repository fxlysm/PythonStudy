#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText
#############
#要发给谁，这里发给2个人
mailto_list=["3xxxxxxxx@qq.com","ixxxxxxxx@gmail.com"]
#####################
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.sina.com"           ##请注意，这里需要你的邮箱服务提供商已经为你开启了smtp服务
mail_user="axxxxxxx"  #你的email用户名
mail_pass="fxxxxxxxx"
mail_postfix="sina.com"
######################
def send_mail(to_list,sub,content):
#'''''
#to_list:发给谁
#sub:主题
#content:内容
#send_mail("aaa@126.com","sub","content")
#'''''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub #设置主题
    msg['From'] = me     #发件人
    msg['To'] = ";".join(to_list) #收件人
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"Hey subject","This is content"):
        print "发送成功"
    else:
        print "发送失败"