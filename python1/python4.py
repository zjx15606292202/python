# import random
# import string
#
# all_chas = string.ascii_letters + string.digits
#
# def randpass(n=8):
#     result = ''
#
#     for i in range(n):
#         ac = random.choice(all_chas)
#         result += ac
#
#     return result
#
# if __name__ == '__main__':
#     a = randpass()
#     print(randpass())
#     print(randpass(4))

# >>> import shutil
# >>> f1 = open('/etc/hosts')
# >>> f2 = open('/tmp/zj.txt','w')
# >>> shutil.copyfilepbj(f1,f2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'shutil' has no attribute 'copyfilepbj'
# >>> shutil.copyfileobj(f1,f2)
# >>> f1.close()
# >>> f2.close()
# >>> shutil.copy('/etc/hosts','/tmp/a.txt')
# '/tmp/a.txt'
# >>> shutil.copy('/etc/passwd','/tmp/')
# >>> shutil.copy2('/etc/passwd','/tmp/')
# '/tmp/passwd'
# >>> shutil.copytree('/etc/security','/tmp/anquan')
# '/tmp/anquan'
# >>> shutil.move('/tmp/zj.txt','/var/tmp/')
# '/var/tmp/zj.txt'
# >>> shutil.rmtree('/tmp/anquan')
#
# >>> import os
# >>> os.remove('/var/tmp/zj.txt')

# >>> a,b = 10,20
# >>> a
# 10
# >>> b
# 20
# >>> a,b = b,a
# >>> a
# 20
# >>> b
# 10
# >>> a,b= 10,20
# >>> t = a
# >>> a = b
# >>> b = t
# >>> a
# 20
# >>> b
# 10
# >>> a,c=10,30
# >>> a
# 10
# >>> c
# 30
# >>> a,c=c,a
# >>> a
# 30
# >>> c
# 10
# >>> import keyword
# >>> keywoed.kwlist
# >>> len(keyword.kwlist)
# >>> keyword.iskeyword('len')
# >>> 'for'in keyword.kwlist

# import os
#
#
# def get_fname():
#     while True:
#         fname = input('filename: ')
#         if not os.path.exists(fname):
#             break
#         print('文件已存在,请重试')
#
#     return fname
#
#
# def get_content():
#     content = []
#     while True:
#         line = input('("end" to quit)>')
#         if line == 'end':
#             break
#         content.append(line)
#
#     return content
#
#
# def wfile(fname, content):
#     with open(fname, 'w')as fobj:
#         fobj.writelines(content)
#
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = [line + '\n' for line in content]
#     wfile(fname, content)


# import os
#
#
# def get_fname():
#     while True:
#         fname = input('filename: ')
#         if not os.path.exists(fname):
#             break
#         print('文件已存在,请重试')
#
#     return fname
#
#
# def get_content():
#     content = []
#     while True:
#         line = input('("end" to quit)>')
#         if line == 'end':
#             break
#         content.append(line)
#
#     return content
#
#
# def wfile(fname, content):
#     with open(fname, 'w')as fobj:
#         fobj.writelines(content)
#
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = [line + '\n' for line in content]
#     wfile(fname, content)

# hi = 'hello'
# alist = [10,20,30]
#
# for ini in range(len(hi)):
#     print(ini,hi[ini])
# for ite in enumerate(alist):
#     print(item)
# for ind ,val in enumerate(alist):
#     print(ind,val)
# >>> '%s: %s' % ('bob',22)
# 'bob: 22'
# >>> '%s: %d' % ('bob',22)
# 'bob: 22'
# >>> '97 is %c' %97
# '97 is a'
# >>> '97 is %#o' %97
# '97 is 0o141'
# >>> '97 is %#x' %97
# '97 is 0x61'
# >>> '1000 is %e' % 10000
# '1000 is 1.000000e+04'
# >>> '10/3 is %f' % (10/3)
# '10/3 is 3.333333'
# >>> '10/3 is %d' % (10/3)
# '10/3 is 3'
# >>> '%10s%10s' % ('name','age')
# '      name       age'
# >>> '%-10s%-10s' % ('name','age')
# 'name      age

# import sys
# import subprocess
# import randpass
#
#
# def adduser(username,fname):
#     info = """用户信息:
# 用户名: %s
# 密码: %s
# """  % (username,password)
#      subprocess.call('useradd %s' % username,shell=True)
#      subprocess.call(
#          'echo %s | passwd --stdin %s' % (password,username),
#          shell=True
#      )
#
#      with open(fname,'a')as fobj:
#          fobj.write(info)
#
#
# if __name == '__main__':
#    password = randpass.randpass()
#    fname = '/tmp/mima.txt'
#    adduser(sys.argv[1],password,fname)
# >>> hi = 'hello world'
# >>> '  hello world  '.strip()
# 'hello world'
# >>> '  hello world  '.lstrip()
# 'hello world  '
# >>> '  hello world  '.rstrip()
# '  hello world'
# >>> hi.upper()
# 'HELLO WORLD'
# >>> hi.lower()
# 'hello world'
# >>> hi.startswith('h')
# True
# >>> hi.startswith('he')
# True
# >>> hi.endswith('abc')
# False
# >>> hi.replace('l','m')
# 'hemmo wormd'
# >>> hi.center(50)
# '                   hello world                    '
# >>> hi.center(50,'*')
# '*******************hello world********************'
# >>> hi.ljust(50,'*')
# 'hello world***************************************'
# >>> hi.rjust(50,'*')
# '***************************************hello world'
# >>> '12345'.isdigit()
# True
# >>> 'hao111'.isdigit()
# False
# >>> 'hao21423'.islower()
# True
# >>> alist = [10,20,30,'bob','alice']
# >>> alist[-1] = 100
# >>> alist
# [10, 20, 30, 'bob', 100]
# >>> alist.remove('bob')
# >>> alist
# [10, 20, 30, 100]
# >>> alist.append(25)
# >>> alist
# [10, 20, 30, 100, 25]
# >>> alist.sort
# <built-in method sort of list object at 0x7f60c9939688>
# >>> alist.sort()
# >>> alist
# [10, 20, 25, 30, 100]
# >>> alist.reverse()
# >>> alist
# [100, 30, 25, 20, 10]
# >>> alist.pop()
# 10
# >>> alist
# [100, 30, 25, 20]
# >>> alist.pop(1)
# 30
# >>> alist
# [100, 25, 20]
# >>> alist.insert(1,50)
# >>> alist
# [100, 50, 25, 20]
# >>> alist.extend('abc')
# >>> alist
# [100, 50, 25, 20, 'a', 'b', 'c']
# >>> alist.append('abc')
# >>> alist
# [100, 50, 25, 20, 'a', 'b', 'c', 'abc']
# >>> alist.index(30)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 30 is not in list


# >>> atuple.count(20)
# 2
# >>> atuple.index(20)
# 1
# >>> atuple[-1]append(4)
#   File "<stdin>", line 1
#     atuple[-1]append(4)
#                    ^
# SyntaxError: invalid syntax
# >>> atuple[-1].append(4)
# >>> atuple
# (10, 20, 30, 20, [1, 2, 3, 4])
# >>> atuple[-2].append(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'append'
# >>> atuple[-1].append(2)
# >>> atuple
# (10, 20, 30, 20, [1, 2, 3, 4, 2])
# >>> atuple[-1]
# [1, 2, 3, 4, 2]
# >>> a = (10)
# >>> len(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: object of type 'int' has no len()
# >>> type(a)
# <class 'int'>
# >>> a = (10,)
# >>> len(a)
# 1
# >>> type(a)
# <class 'tuple'>
# import keyword
# import string
#
# first_chs = string.ascii_letters + '_'
# other_chs = first_chs + string.digits
#
#
# def check_id(idt):
#     if keyword.iskeyword(idt):
#         return '%s 是关键字' % idt
#
#     if idt[0] not in first_chs:
#         return '首字母不合法'
#
#     for ind, ch in range(idt[1:]):
#         if ch not in others_chs:
#             return '第%s个字符不合法' % (ind + 2)
#     return '%s是合法的标识符' % idt
#
#
# if __name__ == '__main__':
#     idt = input('请输入合法字符: ')
#     print(check_id(idt))
# import os
#
# def get_fname():
#     while True:
#         fname = input('filename: ')
#         if not os.path.exists(fname):
#             break
#         print('文件已存在,请重试')
#     return fname
#
# def get_content():
#     content = []
#     while True:
#        line = input('("end" to quit) > ' )
#        if line == 'end':
#           break
#        content.append(line)
#     return content
#
# def wfile(fname,content):
#     with open(fname,'w') as fobj:
#         fobj.writelines(content)
#
#
# if __name__ == '__main__':
#    fname = get_fname()
#    content = get_content()
#    content = [line + '\n' for line in content]
#    wfile(fname,content)

# hi = 'hello'
# alist = [10, 200, 30, 40, 15, 35]
#
# for ind in range(len(hi)):
#     print(ind, hi[ind])
#
# # print(list(enumerate(alist)))
# for item in enumerate(alist):
#     print(item)
#
# for ind, val in enumerate(alist):
#     print(ind, val)
#
# print(list(reversed(alist)))   # 翻转
# for i in reversed(alist):
#     print(i)
#
# print(sorted(alist))           # 排序
# import sys
# import subprocess
# import randpass
#
# def adduser(username, password, fname):
#     info = """用户信息：
# 用户名：%s
# 密码：%s
# """ % (username, password)
#     subprocess.call('useradd %s' % username, shell=True)
#     subprocess.call(
#         'echo %s | passwd --stdin %s' % (password, username),
#         shell=True
#     )
#     with open(fname, 'a') as fobj:
#         fobj.write(info)
#
# if __name__ == '__main__':
#     password = randpass.randpass()
#     fname = '/tmp/mima.txt'
#     adduser(sys.argv[1], password, fname)
