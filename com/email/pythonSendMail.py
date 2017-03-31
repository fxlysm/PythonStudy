#coding:utf-8

import smtplib
from email.mime.text import MIMEText

#1、需要我们有发送的内容，并且内容需要按照邮件的格式进行封装
#msg = MIMEText("hello world,send by while","plain","utf-8") #我们构建了内容
msg = MIMEText("你吃了吗？","plain","utf-8") #我们构建了内容

#2、类似于我们写信封的形式
msg["Subject"] = "来着while的关心" #定义邮件的标题
msg["From"] = "675635708@qq.com" #定义邮件的发信人
msg["To"] = "1378400685@qq.com"  #定义邮件的收信人
#3、登录到SMTP服务器
server = smtplib.SMTP_SSL("smtp.qq.com",465) #实例化SMTP服务器
server.login("675635708@qq.com","dyvkfpbzyhqkbdhh") #使用自己的邮箱账号和SMTP授权码进行登录
server.sendmail("675635708@qq.com",["1378400685@qq.com"],msg.as_string()) #发送邮件
server.quit() #退出服务器


"""
#/usr/bin/python
#!/usr/bin/python
#coding:utf-8

import sys
import pyinotify

import smtplib
from email.mime.text import MIMEText

def sendMAIL(content):
    msg = MIMEText(content,"plain","utf-8")

    msg["Subject"] = "来着while的关心"
    msg["From"] = "675635708@qq.com"
    msg["To"] = "1378400685@qq.com"

    server = smtplib.SMTP_SSL("smtp.qq.com",465)
    server.login("675635708@qq.com","dyvkfpbzyhqkbdhh")
    server.sendmail("675635708@qq.com",["1378400685@qq.com"],msg.as_string())
    server.quit()




class MyEvent(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self,event):
        cont = "%s is modify"%event.name
        sendMAIL(cont)
        print(cont)

def main(path):
    wm = pyinotify.WatchManager()
    wm.add_watch(path,pyinotify.ALL_EVENTS,rec=True)
    event = MyEvent()
    noti = pyinotify.Notifier(wm,event)
    noti.loop()

if __name__ == "__main__":
    path = sys.argv[1]

"""
