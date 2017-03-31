#coding:utf-8
with open('foot.txt','w') as file:
    file.write("my name is lambert")

    # W 权限：如果没有该文件则创建文件  如果有 测覆盖文件
    # a 权限：如果没有该文件则创建文件  如果有 则追加文件本

    with open('foot2.txt', 'w') as file:
        file.write("www.python.org")
        file.seek(0, 0)
        print  file.tell()
        file.seek(3,0)
        print  file.tell()
        file.seek(5,1)
        print  file.tell()
        file.seek(2,0)
        print  file.tell()
        file.seek(1,2)
        print  file.tell()
        #seek() 修改访问文件位置
        #File_object.seek(offet,whence)
        #whence:
        #0  表示从头计算
        #1 表示以当前位置为原点计算
        # 2 表示以文件结尾为原点进行计算
