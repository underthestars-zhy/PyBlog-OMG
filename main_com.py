def theme_main_com(num):
    num = int(num)
    if num == 2:
        return "+++++OMG-名称设置+++++\n==========================================\n0: Back, 1: 设置站点名称, 2: 设置主标题, 3: 设置站点大标题, 4: 设置副标题"
    elif num == 3:
        return "+++++OMG-图标/片设置+++++\n==========================================\n0: Back, 1: 设置网站图标"
def int_com(lst):
    if lst[0] == 2 :
        if lst[1] == 1:
            return "+++++OMG-设置站点名称+++++\n=========================================="
        elif lst[1] == 2:
            return "+++++OMG-设置站点主标题+++++\n=========================================="
        elif lst[1] == 3:
            return "+++++OMG-设置站点大标题+++++\n=========================================="
        elif lst[1] == 4:
            return "+++++OMG-设置站点副标题+++++\n=========================================="
    elif lst[0] == 3:
        if lst[1] == 1:
            return "+++++OMG-设置站点图标+++++\n=========================================="
def com_input(lst):
    if lst[0] == 2 :
        if lst[1] == 1:
            return "str"
        elif lst[1] == 2:
            return "str"
        elif lst[1] == 3:
            return "str"
        elif lst[1] == 4:
            return "str"
    if lst[0] == 3:
        if lst[1] == 1:
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
        elif lst[1] == 3:
            if index_com.big_name(lst[2]):
                return True
            else:
                return False
        elif lst[1] == 4:
            if index_com.vice_name(lst[2]):
                return True
            else:
                return False
    if lst[0] == 3:
        if lst[1] == 1:
            if index_com.head_ico(lst[2]):
                return True
            else:
                return False