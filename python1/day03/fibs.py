def generate_fib(n):
  fib = [0,1]	 		
  for i in range(n - 2):
    fib.append(fib[-1]+fib[-2])
  return fib
       
#alist= generate_fib()
#print(alist)
#blist= [i*2 for i in alist]
#print(blist)

a = generate_fib(10)
print(a)
b = generate_fib(5)
print(b)
x = int(input('length: '))
c = generate_fib(x)
print(c)



