def theme_main ():
    import os
    import sqlite3
    try:
        conn_log = sqlite3.connect("index.db")
        cur_log = conn_log.cursor()
        cur_log.execute('select * from ThemeDown')
        for down_in in cur_log.fetchall():
            if down_in[0] == 1:
                return True
        conn_log.close()
    except:
        pass
    try:
        os.system("rm main_txt.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/main_txt.py")
        os.system("rm main_com.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/main_com.py")
        os.system("rm index.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/index.py")
        os.system("clear")
        conn_log = sqlite3.connect("index.db")
        cur_log = conn_log.cursor()
        cur_log.execute('''Create table ThemeDown(tf int)''')
        conn_log.commit()
        cur_log.execute('''insert into ThemeDown Values(1)''')
        conn_log.commit()
        conn_log.close()
        return True
    except:
        return False
def theme_tf ():
    return "OMG"

def version():
    return "Beat5"

def least_version_url():
    return 'https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/version_theme.txt'