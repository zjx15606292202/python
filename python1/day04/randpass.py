import string
import random

all_chs = string.digits + string.ascii_letters


def suji(b):
   result = ''
 
   for i in range(b):
       ch = random.choice(all_chs) 
       result += ch

   return result

if __name__ == '__main__':
    b = int(input('请输入长度: '))
    suji(b)
    print(suji(b))
    #a = suji()
    #print(a)

