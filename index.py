def index_sql():
    try:
        import os
        import sqlite3
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/html1.txt")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/html2.txt")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/html3.txt")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/index_com.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/page1.txt")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/page2.txt")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/theme_write.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/page_update.py")
        conn_log = sqlite3.connect("index.db")
        cur_log = conn_log.cursor()
        cur_log.execute('''Create table ThemeSet(id int, set_cmd text)''')
        cur_log.execute('''Create table Html1(id int, statement text)''')
        cur_log.execute('''Create table Html2(id int, statement text)''')
        cur_log.execute('''Create table Html3(id int, statement text)''')
        cur_log.execute('''Create table Page1(id int, statement text)''')
        cur_log.execute('''Create table Page2(id int, statement text)''')
        cur_log.execute('''insert into ThemeSet Values(1,'PyBlog')''')  # 设置tittle标签
        cur_log.execute('''insert into ThemeSet Values(2,'Nothing')''')  # 设置导航栏标题
        cur_log.execute('''insert into ThemeSet Values(3,'Nothing')''')  # 设置背景图大标题
        cur_log.execute('''insert into ThemeSet Values(4,'Nothing')''')  # 设置小标题
        cur_log.execute('''insert into ThemeSet Values(5,'Nothing')''')  # 设置ico
        cur_log.execute('''insert into ThemeSet Values(6,'Nothing')''')  # 设置背景图片
        conn_log.commit()
        # ==============
        file = open("html1.txt", "r")
        i = 1
        while i <= 58:
            read_ = str(file.readline())
            cur_log.execute('''insert into Html1 Values('{}','{}')'''.format(i, read_))
            conn_log.commit()
            i += 1
        file.close()
        # ====================
        file = open("html2.txt", "r")
        i = 1
        while i <= 41:
            read_ = str(file.readline())
            cur_log.execute('''insert into Html2 Values('{}','{}')'''.format(i, read_))
            conn_log.commit()
            i += 1
        file.close()
        # ====================
        file = open("html3.txt", "r")
        i = 1
        while i <= 33:
            read_ = str(file.readline())
            cur_log.execute('''insert into Html3 Values('{}','{}')'''.format(i, read_))
            conn_log.commit()
            i += 1
        file.close()
        # ====================
        file = open("page1.txt", "r")
        i = 1
        while i <= 94:
            read_ = str(file.readline())
            cur_log.execute('''insert into Page1 Values('{}','{}')'''.format(i, read_))
            conn_log.commit()
            i += 1
        file.close()
        # ====================
        file = open("page2.txt", "r")
        i = 1
        while i <= 34:
            read_ = str(file.readline())
            cur_log.execute('''insert into Page2 Values('{}','{}')'''.format(i, read_))
            conn_log.commit()
            i += 1
        file.close()
        # =====================
        file = open("index.html", "w")
        cur_log.execute('select * from Html1')
        for write_out in cur_log.fetchall():
            file.write(str(write_out[1]))
        file.close()
        # ====================
        file = open("index.html", "a")
        cur_log.execute('select * from Html2')
        for write_out in cur_log.fetchall():
            file.write(str(write_out[1]))
        file.close()
        # ====================
        file = open("index.html", "a")
        cur_log.execute('select * from Html3')
        for write_out in cur_log.fetchall():
            file.write(str(write_out[1]))
        file.close()
        # =====================
        file = open("about.html", "w")
        cur_log.execute('select * from Page1')
        for write_out in cur_log.fetchall():
            file.write(str(write_out[1]))
        file.close()
        # ====================
        file = open("about.html", "a")
        cur_log.execute('select * from Page2')
        for write_out in cur_log.fetchall():
            file.write(str(write_out[1]))
        file.close()
        # ====================
        conn_log.close()
        return True
    except:
        return False
def main_index():
    import os
    try:
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/blob/main/css.tar")
        os.system("tar xvf css.tar ")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/blob/main/js.tar")
        os.system("tar xvf js.tar ")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/blob/main/images.tar")
        os.system("tar xvf images.tar ")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/blob/main/fonts.tar")
        os.system("tar xvf fonts.tar ")
        os.system("rm -rf css.tar")
        os.system("rm -rf js.tar")
        os.system("rm -rf images.tar")
        os.system("rm -rf fonts.tar")
        os.system("clear")
        if index_sql():
            return True
        else:
            return False
    except:
        return False
