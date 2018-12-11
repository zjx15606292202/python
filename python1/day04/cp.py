scr_fname = '/bin/ls'
dst_fname = '/tmp/ls'


src1 = open(scr_fname,'rb')
dst1 = open(dst_fname,'wb') 


while True:
    data = src1.read(4097) 
    if data == b'':   
        break
    dst1.write(data)
src1.close()
dst1.close()
