#!/user/bin/env python3
import random
all_choices = ['石头','剪刀','布']
win_list = [['石头,剪刀'],['剪刀,布'],['布,石头']]
info = '''(0)石头 (1)剪刀 (2)布 请选择0/1/2:  '''

pwin = 0
cwin = 0
while pwin< 2 and cwin < 2:
        pc = random.choice(all_choices)
        ind = int(input(info))
        player = all_choices[ind]

        print('计算机的选择:%s ,你的选择:%s ' % (pc, player)) 

        if player == pc:
           print('\033[32;1m平局\033[0m') 
        elif [player,pc] in win_list:
           pwin += 1
           print('\033[32;1m你赢了\033[0m')  
        else:
           cwin += 1 
           print('\033[31;1m你输了\033[0m')
        
