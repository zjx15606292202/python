#
#
# stack = []
# def push_it():
#     itm = input('数据: ').strip()
#     if item:
#         stack.append(itm)
#
#
#
# def pop_it():
#     if stack:
#         print('弹出了%s' % stack.pop())
#     else:
#         print('\033[31;1m空\033[0m')
#
#
# def view_it():
#     print('\033[32;1m%s\033[0m' % stack)
#
#
#
# def show_menu():
#     cmds = {'0': push_it,'1': pop_it, '2': view_it}
#     prompt = """(0) 压战
#   (1) 出战
#   (2) 查询
#   (3) 退出
#   请选择(0/1/2/3): """
# while True:
#           choice = input(prompt).strip()[0]
#           if choice not in '0123':
#                print('无效输入')
#                continue
#           if choice == '3':
#                print('bye')
#                break
#           cmds[choice]()
#           # if choice == '0':
#           #      push_it()
#           # elif choice == '1':
#           #      pop_it()
#           # else:
#           #      view_it()
#
# if __name__ == '__main__':
#     show_menu()
# >>> adict = ['name':'bob','age':20]
#   File "<stdin>", line 1
#     adict = ['name':'bob','age':20]
#                    ^
# SyntaxError: invalid syntax
# >>> adict = {'name':'bob','age':20}
# >>> adict
# {'name': 'bob', 'age': 20}
# >>> dict(['ab','cd',('name','niu')])
# {'a': 'b', 'c': 'd', 'name': 'niu'}
# >>> {}.fromkeys(['niy','li','wang'],'male')
# {'niy': 'male', 'li': 'male', 'wang': 'male'}
# >>> 'age' in adict
# True
# >>> for key in dict
#   File "<stdin>", line 1
#     for key in dict
#                   ^
# SyntaxError: invalid syntax
# >>> for key in dict:
# ... print('%s:%s' % (key, adict[key]))
#   File "<stdin>", line 2
#     print('%s:%s' % (key, adict[key]))
#         ^
# IndentationError: expected an indented block
# >>> '%(name)s is %(age)s years old' % adict
# 'bob is 20 years old'
>>> list(adict.values())
# ['bob', 20]
# >>> adict.get('phone','110')
# '110'
# >>> adict
# {'name': 'bob', 'age': 20}
# >>> adict.popitem()
# ('age', 20)
# >>> adict.pop('name')
# 'bob'
# >>> adict.pop('age')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'age'
# >>> adict.update({'aaa':100,'bbb':200})
# >>> adict
# {'aaa': 100, 'bbb': 200
# userdb = {}
# def register():
#     username = input('username: ')
#     if username not in userdb:
#         password = input('password: ')
#         userdb[username] = password
#     else:
#         print('用户已存在')
#
#
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass("password: ")
#     if userdb.get(username) != password:
#         print('登陆失败')
#     else:
#         print('登陆成功')
#
#
#
#
# def show_menu():
#     cmds = {'0':register,'1':login}
#     prompt = """(0) 注册
# (1) 登陆
# (2) 退出
# 请输入你的选择(0/1/2): """
#     while True:
#          choice = input(prompt).strip()[0]
#          if choice not in '012':
#              print('无效输入,请重试')
#              continue
#          if choice == '2':
#              print('bye')
#              break
#          cmds[choice]()
#
#
#
# if __name__ == '__main__':
#    show_menu()
#!/usr/bin/env python3
# import getpass
# userdb = {}
# def register():
#     username = input('username: ')
#     if username not in userdb:
#         password = input('password: ')
#         userdb[username] = password
#     else:
#         print('用户名已存在')
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass("password: ")
#     if userdb.get(username) != password:
#         print('登录失败')
#     else:
#         print('登陆成功')
#
#
# def show_menu():
#     cmds = {'0':register,'1':login}
#     prompt = """(0) 注册
# (1) 登陆
# (2) 退出
# 请选择(0/1/2): """
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice  not in '012':
#             print('无效输入')
#         if choice == '2':
#             print('bye-bye')
#             break
#         cmds[choice]()
#
#
#
#
#
#
# if __name__ == '__main__':
#      show_menu()

# import time
# import sys
#
# n = 0
# print('#' * 20,end='')
#
# while True:
#    print('\r%s@%s' % ('#'* n,'#' * (19-n)),end='')
#    sys.stdout.flush()
#    n += 1
#    time.sleep(0.3)
#    if n == 20:
#       n = 0

# >>> aset = set('hello')
# >>> aset
# {'h', 'l', 'e', 'o'}
# >>> bset = set('how')
# >>> aset | bset
# {'l', 'o', 'h', 'w', 'e'}
# >>> bset
# {'h', 'w', 'o'}
# >>> aset & bset
# {'h', 'o'}
# >>> aset - bset
# {'l', 'e'}
# >>> bset -aset
# {'w'}
# >>> cset = set('ho')
# >>> cset.issubset(aset)
# True
# >>> aset.issubset(cset)
# False
# >>> aset.intersection(bset)
# {'h', 'o'}
# >>> aset
# {'new', 'hello', 'e', 'h', 'o', 'world', 'l'}
# >>> cset
# {'h', 'o'}
# >>> bset
# {'w', 'h', 'o'}
# >>> aset.union(bset)
# {'new', 'hello', 'e', 'h', 'w', 'o', 'world', 'l'}
# >>> aset.difference(bset)
# {'new', 'hello', 'e', 'world', 'l'}
# >>> aset
# {'new', 'hello', 'e', 'h', 'o', 'world', 'l'}
# >>> nset
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'nset' is not defined
# >>> bset
# {'w', 'h', 'o'}
# cp /etc/passwd /tmp/mima
#
# with open('/tmp/mima')as f:
#    aset = set(f)
#
#
# with open('/tmp/passwd')as f:
#    bset = set(f)
#
# with open('/tmp/result.txt','w') as f:
#    f.writelines(aset -bset)

# >>> import time
# >>> time.time()
# 1544599652.7615678
# >>> time.ctime()
# 'Wed Dec 12 15:27:48 2018'
# >>> time.lcaltime()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'time' has no attribute 'lcaltime'
# >>> time.localtime()
# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=12, tm_hour=15, tm_min=28, tm_sec=20, tm_wday=2, tm_yday=346, tm_isdst=0)
# >>> time.sleep(3)
# >>> time.strftime('%Y-%m-%d %H:%M:%S')
# '2018-12-12 15:29:35'

# >>> from datetime import datetime,timedelta
# >>> t1 = datetime.now(
# >>> t1
# datetime.datetime(2018, 12, 12, 15, 46, 25, 76779)
# >>> t1.year
# 2018
# >>> t1.month
# 12
# >>> t1.day
# 12
# >>> t1.hour
# 15
# >>> t1.minute
# 46
# >>> t1.second
# 25
# >>> t1.microsecond
# 76779
# >>> t2 = datetime(2018,10,10)
# >>> t2
# datetime.datetime(2018, 10, 10, 0, 0)
# >>> t1 = datetime.striptime('Dec 12 2018','%b %d %Y')
#
# >>> t1 = datetime.strptime('Dec 12 2018','%b %d %Y')
# >>> t1
# datetime.datetime(2018, 12, 12, 0, 0)
# >>> t = datetime(2018,12,10)
# >>> t1 > t
# True
# >>> t = datetime.now()
# >>> days = timedelta(days=100)
# >>> t1 = t -days
# >>> t2 = t + days
# >>> t1
# datetime.datetime(2018, 9, 3, 15, 54, 39, 562108)
# >>> t2
# datetime.datetime(2019, 3, 22, 15, 54, 39, 562108)
# >>>
# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('无效输入,必须为非0的数字')
# except (KeyboardInterrupt,EOFError):
#     print('\nbye-bye')
#
# else:
#     print(result)
# finally:
#     print('DOME')
# >>> import os
# >>> os.getcwd()
# '/root/nsd_2018/nsd1807/python1/day05'
# >>> os.mkdir('/tmp/demo')
# >>> os.chdir('/tmp/demo')
#
# >>> os.listdir('/home')
# ['lisi', 'Student', 'userb', 'abc', 'userd', 'usera', 'zabbix', 'bob', 'tomcat']
# >>> os.mknod('mytest.txt')
# >>> os.symlink('/etc/hosts','zhuji')
# >>> os.chmod('mytest.txt',0o644)
# >>> os.rename('mytest.txt','test.doc')
# >>> od.listdir()
# >>> os.listdir()
# ['stack.py', 'day05.txt', 'test.doc', 'zhuji', 'mydiv.py', 'trigger.py', 'railway.py', 'diff.py', 'userdb.py']
# >>> os.remove('zhuji')
# >>> os.path.split('/etc/sysconfig/network')
# ('/etc/sysconfig', 'network')
# >>> os.path.basename('/etc/sysconfig/network')
# 'network'
# >>> os.path.dirname('/etc/sysconfig/network')
# '/etc/sysconfig'
# >>> os.path.join('/etc/sysconfig','network')
# '/etc/sysconfig/network'
# >>> os.path.isfile('/etc/hosts')
# True
# >>> os.path.isdir('/etc/hosts')
# False
# >>> os.path.exists('/etc/hosts')
# True
# >>> os.path.islink('/etc/hosts')

# >>> import pickle as p
# >>> f = open('/tmp/data' ,'wb')
# >>> adict = {'name':'bob','age':20}
# >>> p.dump(adict,f)
# >>> f.close(0
# ...
# ...
# ...
# KeyboardInterrupt
# >>>
# >>> f.close()
# >>> import pickle as p
# >>> f = open('/tmp/data','rb')
# >>> mydict = p.load(f)

# >>> mydict
# {'name': 'bob', 'age': 20}
# >>> mydict['age']
#
# stack = []
#
#
# def push_it():
#     itm = input('数据: ').strip()
#     if itm:
#         stack.append(itm)
#
#
# def pop_it():
#     if stack:
#         print('弹出了%s' % stack.pop())
#     else:
#         print('\033[31;1m空\033[0m')
#
#
# def view_it():
#     print('\033[32;1m%s\033[0m' % stack)
#
#
# def show_menu():
#     cmds = {'0': push_it, '1': pop_it, '2': view_it}
#     prompt = """(0) 压桟
# (1) 出桟
# (2) 查询
# (3) 退出
# 请选择(0/1/2/3): """
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('无效输入')
#             continue
#         if choice == '3':
#             print('bye')
#             break
#         cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_menu()
# !/user/bin/env python3
# import getpass
#
# userdb = {}
#
#
# def register():
#     username = input('username: ')
#     if username not in userdb:
#         password = input('password: ')
#         userdb[username] = password
#     else:
#         print('用户名已存在')
#
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass("password: ")
#     if userdb.get(username) != password:
#         print('登录失败')
#     else:
#         print('登陆成功')
#
#
# def show_menu():
#     cmds = {'0': register, '1': login, '2': show_menu}
#     prompt = """ (0) 注册
# (1) 登陆
# (2) 退出
# 请选择(0/1/2): """
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '012':
#             print('无效输入')
#         if choice == '2':
#             print('bye')
#             break
#         cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_menu()

# import time
# import sys
#
# n = 0
# print('#' * 20, end='')
#
# while True:
#     print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')
#     sys.stdout.flush()
#     n += 1
#     time.sleep(0.2)
#     if n == 20:
#         n = 0
# def set_age(name, age):
#     if not 0 < age < 150:
#         raise ValueError('年龄超出范围了(1-150)')
#     print('%s现在是%s岁了' % (name, age))
#
#
# def set_age2(name, age):
#     assert 0 < age < 150, '年龄超过范围了(1-150)'
#     print('%s现在是%s岁了' % (name, age))
#
#
# if __name__ == '__main__':
#     set_age('li', 22)
#     set_age2('li', 222)
# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('无效输入,必须为非0的数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nbye-bye')
#
# else:
#     print(result)
# finally:
#     print('DONE')
# >>> adict
# {'name': 'bob', 'age': 20}
# >>> adict['email'] = 'bob@tedu.cn'
# >>> adict
# {'name': 'bob', 'age': 20, 'email': 'bob@tedu.cn'}
# >>> adict['age']= 22
# >>> adict
# {'name': 'bob', 'age': 22, 'email': 'bob@tedu.cn'}
# >>> adict.keys()
# dict_keys(['name', 'age', 'email'])
# >>> adict.keys()
# dict_keys(['name', 'age', 'email'])
# >>> adict.get('phone','110')
# '110'
# >>> adict.popitem()
# ('email', 'bob@tedu.cn')
# >>> adict.pop('name')
# 'bob'
# >>> adict
# {'age': 22}
# >>> adict.update({'aaa':10,'bb':22})
# >>> adict
# {'age': 22, 'aaa': 10, 'bb': 22}
