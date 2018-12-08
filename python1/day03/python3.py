# import random
# all_choices = ['石头', '剪刀', '布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# prompt = """(0) 石头
# (1) 剪刀
# (2) 布
# 请选择(0/1/2): """
# cwin = 0
# pwin = 0
# while cwin < 2 and pwin < 2:
#     computer = random.choice(all_choices)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1m平局\033[0m')
#     elif [player, computer] in win_list:
#         pwin += 1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou LOSE!!!\033[0m')
# py_str = 'python'
# alist = ['xkk','lmk','zjx']
# atuple = ('zhl','mx')
# adict = {'zx':'南京','bw':'北京'}
#
#
# for ch in py_str:
#    print(ch)
# for name in alist:
#    print(name)
# for name in atuple:
#    print(name)
# for key in adict:
#    print(key,adict[key])
# range(10)
# range(0, 10)
# range(0,10)
# range(0, 10)
# list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  range(0,10000)
# range(0, 10000)
#  range(20000)
# range(0, 20000)
# list(range(6,11))
# [6, 7, 8, 9, 10]
# list(range(4,9,2))
# [4, 6, 8]
# list(range(10,0,-1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#  sum=0
#  for i in range(1,101):
# ... sum += i

# fib = [0,1]
# for i in range(8):
#    fib.append(fib[-1]+fib[-2])
# print(fib)

# for i in range(1,10):   # [1,2,3,4,5,6,7,8,9]
#    for j in range(1,i+1):   #[1],[1,2],[1,2,3]
#         print('%sX%s=%s' % (j,i,i*j),end=' ')
#    print()
# [10]
# [10]
# >>> [10+5]
# [15]
# >>> [10+5 for i in range(1,11)]
# [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# >>> [10+i for i in range(1,11)]
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# >>> [10+i for i in range(1,11) if i%2==1]
# [11, 13, 15, 17, 19]
# >>> ['192.168.1.'+ str(i) for i in range(1,30)]
# ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10', '192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15', '192.168.1.16', '192.168.1.17', '192.168.1.18', '192.168.1.19', '192.168.1.20', '192.168.1.21', '192.168.1.22', '192.168.1.23', '192.168.1.24', '192.168.1.25', '192.168.1.26', '192.168.1.27', '192.168.1.28', '192.168.1.29']

# >>> f = open('/tmp/zhu')
# >>> data = f.read()
# >>> f.close()
# >>> print(data)
# 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
# ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
# 172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com
# 172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com
# 172.25.254.254  classroom  content  classroom.example.com  content.example.com
# 172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com
# 192.168.2.100 www.a.com www.b.com
#
# >>> data
# '127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com\n172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com\n172.25.254.254  classroom  content  classroom.example.com  content.example.com\n172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com\n192.168.2.100 www.a.com www.b.com\n'
# >>>

# >>> f = open('/tmp/zhu')
# >>> f.read()
# '127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com\n172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com\n172.25.254.254  classroom  content  classroom.example.com  content.example.com\n172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com\n192.168.2.100 www.a.com www.b.com\n'
# >>> f.read(10)
# ''
# >>> f.close()
# >>> f = open('/tmp/zhu')
# >>> f.read(10)
# '127.0.0.1 '
# >>> f.readline()
# '  localhost localhost.localdomain localhost4 localhost4.localdomain4\n'
# >>> f.readlines()
# ['::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n', '172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com\n', '172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com\n', '172.25.254.254  classroom  content  classroom.example.com  content.example.com\n', '172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com\n', '192.168.2.100 www.a.com www.b.com\n']
# >>> f.close()
# >>> f.close()
# >>> f = open('/bin/ls', 'rb')
# >>> f.read(10)
# b'\x7fELF\x02\x01\x01\x00\x00\x00'
# >>> f = open('/tmp/zhu','w')
# >>> f.write('hello,world!\n')
# 13
# >>> f.flush
# <built-in method flush of _io.TextIOWrapper object at 0x7fbfd5318c18>
# >>> f.flush()
# >>> f.writelines(['2nd line.\n','3rd line.\n'])
# >>> f.close()

# >>> f = open('/tmp/zhu','a')
# >>> f.write('4th.\n')
# 5
# >>> f.close()
# >>> [10]
# [10]
# >>> [10 + 5]
# [15]
# >>> [10 + 5 for i in range(1, 11)]
# [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# >>> [10 + i for i in range(1, 11)]
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# >>> [10 + i for i in range(1, 11) if i % 2 == 1]
# [11, 13, 15, 17, 19]
# >>> ['192.168.1.' + str(i) for i in range(1, 255)]
# >>> range(10)
# range(0, 10)
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> f =open('/tmp/zhu' ,'r+')
# >>> f.write('abcde')
# 5
# >>> f.flush
# <built-in method flush of _io.TextIOWrapper object at 0x7f32c4d97c18>
# >>> f.flush()
# >>> f.tell()
# 5
# >>> f.read(8)
# 'o.\n2nd l'
# >>> f.seek(3,0)
# 3
# >>> f.read(2)
# 'de'
# >>> f.seek(0,2)
# 39
# >>> f.write('my test.\n')
# 9
# >>> f.flush()
# >>> f.read()
# ''
# >>> f.seek(0.0)
# 0.0
# >>> f.readline()
# 'abcdeo.\n'
# >>> with open('/tmp/zhu')as f:
#     ...
#     line = f.readline()
#     >> > line
# with open('/tmp/zhu') as f:
#  for line in f:
#   print(line,end= ' ')
# f1 = open('/bin/ls','rb')
# f2 = open('/root/ls','wb')
#
# data = f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()
# src_fname= '/bin/ls'
# dst_fname= '/tmp/list'
#
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while True:
#     data = src_fobj.read(4096)
#     if not data:
#         break
#     dst_fobj.write(data)
#
# scr_fobj.close()
# dst_fobj.close()
# src_fname= '/bin/ls'
# dst_fname= '/tmp/list'

# with open(src_fname,'rb') as src_fobj:
#   with open(dst_fname,'wb') as dst_fobj:
#
#      while True:
#          data = src_fobj.read(4096)
#          if not data:
#             break
#          dst_fobj.write(data)
#
# #scr_fobj.close()
# #dst_fobj.close()
# def generate_fib():
#     fib = [0,1]
#     for i in range(8):
#       fib.append(fib[-1]+fib[-2])
#     print(fib)
#
# generate_fib()
# generate_fib()

# def generate_fib():
#   fib = [0,1]
#   for i in range(8):
#     fib.append(fib[-1]+fib[-2])
#     return fib
#
# alist= generate_fib()
# print(alist)
# blist= [i*2 for i in alist]
# print(blist)
# def generate_fib(n):
#   fib = [0,1]
#   for i in range(n - 2):
#     fib.append(fib[-1]+fib[-2])
#   return fib
#
# #alist= generate_fib()
# #print(alist)
# #blist= [i*2 for i in alist]
# #print(blist)
#
# a = generate_fib(10)
# print(a)
# b = generate_fib(5)
# print(b)
# x = int(input('length: '))
# c = generate_fib(x)
# print(c)

# import sys
#
# def copy(src_fname,dst_fname):
#     with open(src_fname,'rb') as src_fobj:
#         with open(dst_fname,'wb') as dst_fobj:
#             while True:
#                 data = src_fobj.read(4096)
#                 if not data:
#                     break
#                 dst_fobj.write(data)
#
# copy(sys.argv[1],sys.argv[2])
# hi = 'hello world'
#
#
# def pstar(n=30):
#     print('*' * n)
#
#
# pstar()
# pstar(50)
#
#
# import star
#
# print(star.hi)
# star.pstar()

# import random
# all_choices = ['石头', '剪刀', '布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# prompt = """(0) 石头
# (1) 剪刀
# (2) 布
# 请选择(0/1/2): """
# cwin = 0
# pwin = 0
# while cwin < 2 and pwin < 2:
#     computer = random.choice(all_choices)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1m平局\033[0m')
#     elif [player, computer] in win_list:
#         pwin += 1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou LOSE!!!\033[0m')
# py_str = 'python'
# alist = ['xkk','lmk','zjx']
# atuple = ('zhl','mx')
# adict = {'zx':'南京','bw':'北京'}
#
#
# for ch in py_str:
#    print(ch)
# for name in alist:
#    print(name)
# for name in atuple:
#    print(name)
# for key in adict:
#    print(key,adict[key])
# range(10)
# range(0, 10)
# range(0,10)
# range(0, 10)
# list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  range(0,10000)
# range(0, 10000)
#  range(20000)
# range(0, 20000)
# list(range(6,11))
# [6, 7, 8, 9, 10]
# list(range(4,9,2))
# [4, 6, 8]
# list(range(10,0,-1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#  sum=0
#  for i in range(1,101):
# ... sum += i

# fib = [0,1]
# for i in range(8):
#    fib.append(fib[-1]+fib[-2])
# print(fib)

# for i in range(1,10):   # [1,2,3,4,5,6,7,8,9]
#    for j in range(1,i+1):   #[1],[1,2],[1,2,3]
#         print('%sX%s=%s' % (j,i,i*j),end=' ')
#    print()
# [10]
# [10]
# >>> [10+5]
# [15]
# >>> [10+5 for i in range(1,11)]
# [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# >>> [10+i for i in range(1,11)]
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# >>> [10+i for i in range(1,11) if i%2==1]
# [11, 13, 15, 17, 19]
# >>> ['192.168.1.'+ str(i) for i in range(1,30)]
# ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10', '192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15', '192.168.1.16', '192.168.1.17', '192.168.1.18', '192.168.1.19', '192.168.1.20', '192.168.1.21', '192.168.1.22', '192.168.1.23', '192.168.1.24', '192.168.1.25', '192.168.1.26', '192.168.1.27', '192.168.1.28', '192.168.1.29']

# >>> f = open('/tmp/zhu')
# >>> data = f.read()
# >>> f.close()
# >>> print(data)
# 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
# ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
# 172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com
# 172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com
# 172.25.254.254  classroom  content  classroom.example.com  content.example.com
# 172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com
# 192.168.2.100 www.a.com www.b.com
#
# >>> data
# '127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com\n172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com\n172.25.254.254  classroom  content  classroom.example.com  content.example.com\n172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com\n192.168.2.100 www.a.com www.b.com\n'
# >>>

# >>> f = open('/tmp/zhu')
# >>> f.read()
# '127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com\n172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com\n172.25.254.254  classroom  content  classroom.example.com  content.example.com\n172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com\n192.168.2.100 www.a.com www.b.com\n'
# >>> f.read(10)
# ''
# >>> f.close()
# >>> f = open('/tmp/zhu')
# >>> f.read(10)
# '127.0.0.1 '
# >>> f.readline()
# '  localhost localhost.localdomain localhost4 localhost4.localdomain4\n'
# >>> f.readlines()
# ['::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n', '172.25.0.11  server0  server server0.example.com  webapp0.example.com  www0.example.com\n', '172.25.0.10  desktop0  desktop  desktop0.example.com  smtp0.example.com\n', '172.25.254.254  classroom  content  classroom.example.com  content.example.com\n', '172.25.254.250  foundation0 foundation0.example.com rhgls.domain254.example.com\n', '192.168.2.100 www.a.com www.b.com\n']
# >>> f.close()
# >>> f.close()
# >>> f = open('/bin/ls', 'rb')
# >>> f.read(10)
# b'\x7fELF\x02\x01\x01\x00\x00\x00'
# >>> f = open('/tmp/zhu','w')
# >>> f.write('hello,world!\n')
# 13
# >>> f.flush
# <built-in method flush of _io.TextIOWrapper object at 0x7fbfd5318c18>
# >>> f.flush()
# >>> f.writelines(['2nd line.\n','3rd line.\n'])
# >>> f.close()

# >>> f = open('/tmp/zhu','a')
# >>> f.write('4th.\n')
# 5
# >>> f.close()
# >>> [10]
# [10]
# >>> [10 + 5]
# [15]
# >>> [10 + 5 for i in range(1, 11)]
# [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# >>> [10 + i for i in range(1, 11)]
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# >>> [10 + i for i in range(1, 11) if i % 2 == 1]
# [11, 13, 15, 17, 19]
# >>> ['192.168.1.' + str(i) for i in range(1, 255)]
# >>> range(10)
# range(0, 10)
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> f =open('/tmp/zhu' ,'r+')
# >>> f.write('abcde')
# 5
# >>> f.flush
# <built-in method flush of _io.TextIOWrapper object at 0x7f32c4d97c18>
# >>> f.flush()
# >>> f.tell()
# 5
# >>> f.read(8)
# 'o.\n2nd l'
# >>> f.seek(3,0)
# 3
# >>> f.read(2)
# 'de'
# >>> f.seek(0,2)
# 39
# >>> f.write('my test.\n')
# 9
# >>> f.flush()
# >>> f.read()
# ''
# >>> f.seek(0.0)
# 0.0
# >>> f.readline()
# 'abcdeo.\n'
# >>> with open('/tmp/zhu')as f:
#     ...
#     line = f.readline()
#     >> > line
# with open('/tmp/zhu') as f:
#  for line in f:
#   print(line,end= ' ')
# f1 = open('/bin/ls','rb')
# f2 = open('/root/ls','wb')
#
# data = f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()
# src_fname= '/bin/ls'
# dst_fname= '/tmp/list'
#
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while True:
#     data = src_fobj.read(4096)
#     if not data:
#         break
#     dst_fobj.write(data)
#
# scr_fobj.close()
# dst_fobj.close()
# src_fname= '/bin/ls'
# dst_fname= '/tmp/list'

# with open(src_fname,'rb') as src_fobj:
#   with open(dst_fname,'wb') as dst_fobj:
#
#      while True:
#          data = src_fobj.read(4096)
#          if not data:
#             break
#          dst_fobj.write(data)
#
# #scr_fobj.close()
# #dst_fobj.close()
# def generate_fib():
#     fib = [0,1]
#     for i in range(8):
#       fib.append(fib[-1]+fib[-2])
#     print(fib)
#
# generate_fib()
# generate_fib()

# def generate_fib():
#   fib = [0,1]
#   for i in range(8):
#     fib.append(fib[-1]+fib[-2])
#     return fib
#
# alist= generate_fib()
# print(alist)
# blist= [i*2 for i in alist]
# print(blist)
# def generate_fib(n):
#   fib = [0,1]
#   for i in range(n - 2):
#     fib.append(fib[-1]+fib[-2])
#   return fib
#
# #alist= generate_fib()
# #print(alist)
# #blist= [i*2 for i in alist]
# #print(blist)
#
# a = generate_fib(10)
# print(a)
# b = generate_fib(5)
# print(b)
# x = int(input('length: '))
# c = generate_fib(x)
# print(c)

# import sys
#
# def copy(src_fname,dst_fname):
#     with open(src_fname,'rb') as src_fobj:
#         with open(dst_fname,'wb') as dst_fobj:
#             while True:
#                 data = src_fobj.read(4096)
#                 if not data:
#                     break
#                 dst_fobj.write(data)
#
# copy(sys.argv[1],sys.argv[2])
# hi = 'hello world'
#
#
# def pstar(n=30):
#     print('*' * n)
#
#
# pstar()
# pstar(50)
#
#
# import star
#
# print(star.hi)
# star.pstar()



