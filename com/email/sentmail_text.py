#coding=utf-8
import smtplib
from email.mime.text import MIMEText
def main():
    MAIL_FROM = 'fxlysm@126.com'
    MAIL_TO = ['814380399@qq.com',"fxlyfm@126.com"]#这里是向多人发送
    msg = MIMEText('我是内容',_charset='UTF-8')
    msg['Subject'] = 'python测试!'.decode("utf-8")
    msg['From'] = MAIL_FROM

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.126.com')
        smtp.login('fxlysm', 'liu501606')#用户名和密码
        smtp.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
        print 'email sent.suss'
        smtp.close()
    except Exception, e:
        print e

if __name__ == '__main__':
    main()