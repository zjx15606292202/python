#!/usr/bin/env python3

try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('无效输入,必须为非0的数字')
except (KeyboardInterrupt,EOFError):
    print('\nbye-bye') 

else:
    print(result)
finally:
    print('DONE')
