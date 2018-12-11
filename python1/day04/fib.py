#!/usr/bin/env python3

fib = [0,1]
a = int(input('数列的长度: '))
for i in range(a - 2):

   fib.append(fib[-1]+ fib[-2])
print(fib)
