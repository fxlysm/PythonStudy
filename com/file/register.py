#coding:utf-8
myfile = open('info.txt','a')
while True:
    account =raw_input('Please input you account：')
    passward =raw_input('Please input you password：')
    if account == '':
        print "please input account again!"
        continue
    if passward == '':
        print  'plas input password again!'
        continue
    str1 ='%s:%s\n'%(account,passward)
    myfile.write(str1)
    myfile.flush()
    print '恭喜你，注册成功!'
    break
myfile.close()