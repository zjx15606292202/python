
import time
import sys

n = 0
print('#'* 20,end='')


while True:
    print('\r%s@%s' % ('#' * n, '#' * (19 -n)), end='')
    sys.stdout.flush()
    n += 1
    time.sleep(0.2)
    if n == 20:
       n = 0
