with open('/tmp/mima')as f:
    aset = set(f)
with open('/etc/passwd')as f:
    bset = set(f)
with open('/tmp/xkk.txt','w')as f:
   f.writelines(aset - bset)
