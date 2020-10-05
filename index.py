def index_sql():
    try:
        import os
        import sqlite3
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/html1.txt")
        os.system("rm html1.txt")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/html2.txt")
        os.system("rm html2.txt")
        conn_log = sqlite3.connect("index.db")
        cur_log = conn_log.cursor()
        cur_log.execute('''Create table Html1(id int,statement text)''')
        cur_log.execute('''Create table Html2(id int,statement text)''')
        # ==============
        file = open("html1.txt", "r")
        i = 1
        while i <= 99:
            read_ = str(file.readline())
            cur_log.execute('''insert into Html1 Values('{}','{}')'''.format(i, read_))
            conn_log.commit()
            i += 1
        file.close()
        # ====================
        file = open("html2.txt", "r")
        i = 1
        while i <= 33:
            read_ = str(file.readline())
            cur_log.execute('''insert into Html2 Values('{}','{}')'''.format(i, read_))
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
        conn_log.close()
        return True
    except:
        return False
def main_index():
    import os
    try:
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/css.tar")
        os.system("tar xvf css.tar ")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/js.tar")
        os.system("tar xvf js.tar ")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/images.tar")
        os.system("tar xvf images.tar ")
        os.system("wget https://gitdown.uts.ski/https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/fonts.tar")
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
