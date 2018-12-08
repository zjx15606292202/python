for i in range(1,10):   # [1,2,3,4,5,6,7,8,9]
   for j in range(1,i+1):   #[1],[1,2],[1,2,3]
        print('%sX%s=%s' % (j,i,i*j),end=' ')
   print()    
