def theme_main_com(num):
    num = int(num)
    if num==2:
        return "+++++OMG-名称设置+++++\n==========================================\n0: Back, 1: 设置站点名称, 2: 设置主标题"
def int_com(lst):
    if lst[0] == 1 :
        if lst[1] == 1:
            return "+++++OMG-设置站点名称+++++\n=========================================="
def com_input(lst):
    if lst[0] == 2 :
        if lst[1] == 1:
            return "str"
        elif lst[1] == 2:
            return "str"
def com_str(lst):
    import index_com
    if lst[0] == 2 :
        if lst[1] == 1:
            if index_com.head_name(lst[2]):
                return True
            else:
                return False
        elif lst[1] == 2:
            if index_com.main_name(lst[2]):
                return True
            else:
                return False