adict = {'name':'bob','age':20}
for key in adict.keys():
   print(key)

for key in adict:
   print(key)
   print(list(adict.values()))

for key,val in adict.items():
   print('%s: %s' % (key,val))
