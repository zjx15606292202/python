# def get_age(name, age):
#     print('%s is %s years old.' % (name, age))
#
#
# get_age('bob', 24)
# get_age(name="bob", age=23)
# get_age(bob, age=23)
# import os
# import pickle
# import time
#
#
# def cost(record):
#     amount = int(input('金额: '))
#     comment = input('备注: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(record, 'rb') as fobj:
#         data = pickle.load(fobj)
#     balance = data[-1][-2] - amount
#     data.append([date, 0, amount, balance, comment])
#     with open(record, 'wb') as fobj:
#         pickle.dump(data, fobj)
#
#
# def save(record):
#     amount = int(input('金额: '))
#     comment = input('备注: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(record, 'rb') as fobj:
#         data = pickle.load(fobj)
#     balance = data[-1][-2] + amount
#     data.append([date, 0, amount, balance, comment])
#     with open(record, 'wb') as fobj:
#         pickle.dump(data, fobj)
#
#
# def query(record):
#     print('%-12s%-10s%-10s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
#     with open(record, 'rb') as fobj:
#         data = pickle.load(fobj)
#     for item in data:
#         print('%-12s%-10s%-10s%-10s%-20s' % tuple(item))
#
#
# def show_menu():
#     record = 'record.txt'  # 记账
#     if not os.path.exists(record):
#         init_data = [
#             [time.strftime('%Y-%m-%d'), 0, 0, 10000, '开始记账'],
#         ]
#         with open(record, 'wb') as fobj:
#             pickle.dump(init_data, fobj)
#     cmds = {'0': cost, '1': save, '2': query}
#     prompt = """(0) 记录开销
# (1) 记录收入
# (2) 查询收支记录
# (3) 退出
# 请选择(0/1/2/3): """
#     while True:
#         try:
#             choice = input(prompt).strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt, EOFError):
#             choice = '3'
#
#         if choice not in '0123':
#             print('无效输入,请重试')
#             continue
#         if choice == '3':
#             print('\nbye')
#             break
#         cmds[choice](record)
#
#     if __name__ == '__main__':
#         show_menu()

#def my(*args):  *表示args是个元祖
#    print(args)
#
#
#def my1(**kwargs): **kwargs表示是个字典
#    print(kwargs)
#
#
#
#if __name__ == '__main__':
#    my()
#    my(10)
#    my(10,20,309)
#    my(10,20,309,'bob','tom')
#    my1(name='bob',age=23)

# def add(a, b):
#     print(a + b)
#
#
# if __name__ == '__main__':
#     alist = [10, 20]
#     add(*alist)
#     add(*'xk')

# import random
#
#
# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# def exam():
#     cmds = {'+': add, '-': sub}
#     nums = [random.randint(1, 100) for i in range(2)]
#     nums.sort(reverse=True)
#     op = random.choice('+ -')
#     prompt = '%s%s%s=' % (nums[0], op, nums[1])
#     result = cmds[op](*nums)
#     # if op == '+':
#     #    result = nums[0] + nums[1]
#     # else:
#     #    result = nums[0] - nums[1]
#     tries = 0
#     while tries < 3:
#         try:
#             answer = int(input(prompt))
#         except:
#             print()
#             continue
#         if answer == result:
#             print('答对了')
#             break
#         else:
#             print('答错了')
#         tries += 1
#     else:
#         print('%s%s' % (prompt, result))
#
#
# if __name__ == '__main__':
#     while True:
#         exam()
#         try:
#             yn = input('Continue:(y/n)? ').strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt, EOFError):
#             yn = 'n'
#
#         if yn in 'Nn':
#             print('\nbye')
#             break


# from random import randint
#
#
# def func1(n):
#     return n % 2
#
# if __name__ == '__main__':
#     nums = [randint(1,100)for i in range(10)]
#     print(nums)
#     print(list(filter(func1,nums)))
#     print(list(filter(lambda n: n % 2,nums)))
# print('#' * 20)
# print(list(map(func2, nums)))
# print(list(map(lambda n: n + 1, nums)))


# x = 10
#
#
# def foo():
#     print(x)
#
#
# print(foo())
#
#
# def bar():
#     x = 'hello,world'
#     print(x)
#
#
# print(bar())
# print(x)
#
#
# def test1():
#     y = 100
#     print(y)
#
#
# print(test1())
#
# print(y)

# import tkinter
# from functools import partial
#
# root = tkinter.Tk()
# lb = tkinter.Label(root,text="Hello World!", font="Arial 20")
# b1 = tkinter.Button(root,bg='blue',fg='white',text='Button 1')
# MyButton = partial(tkinter.Button,root,bg='blue',fg='white')
# b2 = MyButton(text='Button 2')
# b3 = MyButton(text='Button 3')
# b4 = MyButton(text='QUIT',command=root.quit)
# for item in [lb,b1,b2,b3,b4]:
#     item.pack()
#
# root.mainloop()

# def func1(n):
#     if n ==1:
#         return 1
#     return n * func1(n-1)
# if __name__ == '__main__':
#     print(func1(5))

# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n-1)
# if __name__ == '__main__':
#     print(func(5))

# from random import randint
#
# def quick_sort(seq):
#     if len(seq) < 2:
#         return seq
#
#     middle = seq[0]
#     smaller = []
#     larger = []
#
#     for item in seq[1:]:
#         if item < middle:
#             smaller.append(item)
#         else:
#             larger.append(item)
#
#     return quick_sort(smaller) + [middle] + quick_sort(larger)
#
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     print(quick_sort(nums))

# def mygen():
#     yield 100
#     print('---------')
#     yield 200
#     print('#########')
#     yield 300
# a = mygen()
# a.__next__()
# a.__next__()
# x = a.__next__()
# x
# a.__next__()
# b = mygen()
# for item in b:
#     print(item)
#
# def file_block(fobj):
#     content = []
#     for line in fobj:
#         content.append(line)
#         if len(content) ==10:
#             yield content
#             content.clear()
#     if content:
#         yield content
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     fname = '/etc/passwd'
#     fobj = open(fname)
#     for block in file_block(fobj):
#         print(block)
#
#     fobj.close()

# from random import randint
#
# def quick_sort(seq):
#     if len(seq) < 2:
#         return seq
#
#     middle = seq[0]
#     smaller = []
#     larger = []
#
#     for item in seq[1:]:
#         if item < middle:
#             smaller.append(item)
#         else:
#             larger.append(item)
#     return quick_sort(smaller) + [middle] + quick_sort(larger)
#
#
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     print(quick_sort(nums))

def foo():
    print('in foo')
    bar()

def bar():
    print('in bar')
foo()

def myfunc():
    >>

    def foo():
        ...
        print('in foo')

    ...
    bar()
    ...
    >> >

    # def bar():
    #     ...
    #     print('in bar')
    #
    # ...
    # >> > foo()
    # in foo
    # in bar
    # >> >
    #
    # def myfunc(*args):
    #     ...
    #     print(args)



    # def myfunc2(**kw):
    #     ...
    #     print(kw)
    #
    # ...
    # >> > if __name__ == '__main__':
    #     ...
    #     myfunc()
    # ...
    # myfunc(10)
    # ...
    # myfunc(10, 20, 30)
    # ...
    # myfunc(10, 20, 30, 'bob')
    # ...
    # ...
    # ()
    # (10,)
    # (10, 20, 30)
    # (10, 20, 30, 'bob')
    # >> > if __name__ == '__main__':
    #     ...
    #     myfunc2(name='bob')
    # ...
    # myfunc2(name='bob', age=23)
    # ...
    # {'name': 'bob'}
    # {'name': 'bob', 'age': 23}
    # >> >
    #
    # def add(x, y)
    #     File
    #     "<stdin>", line
    #     1
    #
    #     def add(x, y)
    #         ^
    #
    #     SyntaxError: invalid
    #     syntax
    #     >> >
    #
    #     def add(x, y):
    #         ...
    #         print(x + y)
    #
    #     ...
    #     >> > if __name__ == '__main__':
    #         ...
    #         alist = [10, 20]
    #     ...
    #     add(*alist)
    #     ...
    #     add(*'ab')
    #     ...
    #     30
    #     ab

    # def func1(n):
    #     if n == 1:
    #         return 1
    #     return n * func1(n - 1)
    #
    # if __name__ == '__main__':
    #     print(func1(5))

# from random  import randint
#
# def fun1(n):
#     return n % 2
#
#
# def func2(n):
#      return n + 1
#
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     print(list(filter(func1,nums)))
#     print(list(filter(lambda n: n % 2,nums)))
#     print(list(map(func2,nums)))
#     print(list(map(lambda n: n+1,nums)))

# def file_block(fobj):
#     content = []
#     for line in fobj:
#         content.append(line)
#         if len(content) == 10:
#             yield content
#             content.clear()
#     if content:
#         yield content
#
# if __name__ == '__main__':
#     fname = '/etc/passwd'
#     fobj = open('/etc/passwd')
#     for item in file_block(fobj):
#         print(item)
#
#     fobj.close()


# import random
#
# def exam():
#     cmds = {'+':lambda x,y: x+y,'-':lambda x,y:x-y}
#     nums = [random.randint(1,100)for i in range(2)]
#     nums.sort(reverse=True)
#     op = random.choice('+-')
#     prompt = '%s%s%s=' % (num[0],op,num[1])
#     result = cmds[op](*nums)
#     tries = 0
#     while tries < 3:
#         try:
#             answer = int(input(prompt))
#         except:
#             print()
#             continue
#         if answer == result:
#             print('答对了')
#             break
#         else:
#             print('答错了')
#         tries +=1
#     else:
#         print('%s%s' %(prompt,result))
#
#
#
#
#
#
#
# # if __name__ == '__main__':
# #     while True:
# #         exam()
# #         try:
# #             yn = input('继续(y/n)? ').strip()[0]
# #         except IndexError:
# #             continue
# #         except (KeyboardInterrupt,EOFError):
# #             yn = 'n'
# #         if yn in 'Nn':
# #             print('\nbye')
# #             break
# import os
# import time
# import pickle
#
# def cost(record):
#     amount = int(input('金额: '))
#     comment = input('备注: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(record,'rb') as fobj:
#         data = pickle.load(fobj)
#     balance = data[-1][-2] - amount
#     data.append([date,0,amount,balance,comment])
#     with open(record,'wb') as fobj:
#         pickle.dump(data,fobj)
#
#
# def save(record):
#     amount = int(input('金额: '))
#     comment = input('备注: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(record, 'rb') as fobj:
#         data = pickle.load(fobj)
#     balance = data[-1][-2] + amount
#     data.append([date, 0, amount, balance, comment])
#     with open(record, 'wb') as fobj:
#         pickle.dump(data, fobj)
#
# def query(record):
#     print('%-12s%-10s%-10s%-10s%-20s' % ('date','save','cost','balance','comment'))
#     with open(record,'rb') as fobj:
#         data = pickle.load(fobj)
#     for item in data:
#         print('%-12s%-10s%-10s%-10s%-20s' % tuple(item))
#
#
# def show_menu():
#         record = 'record.txt'
#         cmds = {'0':cost,'1':save,'2':query}
#         if not os.path.exists(record):
#             init_data = [
#                 [time.strftime('%Y-%m-%d'),0,0,10000,'开始记账'],
#             ]
#             with open(record,'wb') as fobj:
#                 pickle.dump(init_data,fobj)
#         prompt = """ (0) 记录开销
# (1) 记录收入
# (2) 查询收支
# (3) 退出
# 请选择(0/1/2/3):  """
#         while True:
#             try:
#                 choice = input(prompt).strip()[0]
#             except IndexError:
#                 continue
#             except (KeyboardInterrupt,EOFError):
#                 choice == '3'
#             if choice == '3':
#                 print('\nbye')
#                 break
#             if choice not in '0123':
#                 print('无效输入, 请重试')
#                 continue
#             cmds[choice](record)
#
#
#
# if __name__ == '__main__':
#     show_menu()





























