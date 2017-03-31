#coding:utf-8


file_name='foo.txt'


# with open(file_name,'r') as file:
#     for line in file:
#         print line

with open(file_name,'r') as file:
    lines=file.readlines()
    print lines
    for line in lines:
        print line.rstrip()



