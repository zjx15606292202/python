stack = []
def push_it():
    itm = input('数据: ').strip()
    if itm:
           stack.append(itm)


def pop_it():
    if stack:
           print('弹出了%s' % stack.pop())
    else:
           print('\033[31;1m空\033[0m')




def view_it():
      print('\033[32;1m%s\033[0m' % stack)




def show_menu():
    cmds = {'0':push_it,'1':pop_it,'2':view_it} 
    prompt = """(0) 压桟
(1) 出桟
(2) 查询
(3) 退出 
请选择(0/1/2/3): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
           print('无效输入')
           continue
        if choice == '3':
           print('bye') 
           break   
        cmds[choice]()




if __name__ == '__main__':
    show_menu()
