def head_name(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    tittle = "\t<title>" + str + "</title>\n"
    cur_log.execute('''update Html1 set statement='{}' where id=9'''.format(tittle))
    cur_log.execute('''update Page1 set statement='{}' where id=9'''.format(tittle))
    conn_log.commit()
    # =====================
    file = open("index.html", "w")
    cur_log.execute('select * from Html1')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html2')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html3')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    conn_log.close()
    return True

def main_name(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    mainame = '''\t\t\t\t\t<div class="nav-mobile-capital"><a href="index.html">'''+str+'''</a>\n'''
    mainame1 = '''\t\t\t\t\t<a href="index.html">'''+str+'''</a>\n'''
    cur_log.execute('''update Html1 set statement='{}' where id=33'''.format(mainame))
    cur_log.execute('''update Html1 set statement='{}' where id=42'''.format(mainame1))
    mainame = '''\t\t\t\t\t<div class="nav-mobile-capital"><a href="index.html">''' + str + '''</a>\n'''
    mainame1 = '''\t\t\t\t\t<a href="index.html">''' + str + '''</a>\n'''
    cur_log.execute('''update Page1 set statement='{}' where id=33'''.format(mainame))
    cur_log.execute('''update Page1 set statement='{}' where id=42'''.format(mainame1))
    conn_log.commit()
    # =====================
    file = open("index.html", "w")
    cur_log.execute('select * from Html1')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html2')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html3')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    conn_log.close()
    return True

def big_name(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    bigname='''\t\t\t\t\t\t<h1 class="banner-title">'''+str+'''</h1>\n'''
    cur_log.execute('''update Html2 set statement='{}' where id=36'''.format(bigname))
    conn_log.commit()
    # =====================
    file = open("index.html", "w")
    cur_log.execute('select * from Html1')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html2')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html3')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    conn_log.close()
    return True

def vice_name(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    vicename='''\t\t\t\t\t\t<p>'''+str+'''</p>\n'''
    cur_log.execute('''update Html2 set statement='{}' where id=37'''.format(vicename))
    conn_log.commit()
    # =====================
    file = open("index.html", "w")
    cur_log.execute('select * from Html1')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html2')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html3')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    conn_log.close()
    return True

def head_ico(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    ico='''\t<link rel="icon" href="'''+str+'''">\n'''
    cur_log.execute('''update Html1 set statement='{}' where id=11'''.format(ico))
    cur_log.execute('''update Page1 set statement='{}' where id=11'''.format(ico))
    conn_log.commit()
    # =====================
    file = open("index.html", "w")
    cur_log.execute('select * from Html1')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html2')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html3')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    conn_log.close()
    return True

def main_img(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    img='''\t\t\t<img src="'''+str+'''" class="banner-img">\n'''
    cur_log.execute('''update Html2 set statement='{}' where id=32'''.format(img))
    conn_log.commit()
    # =====================
    file = open("index.html", "w")
    cur_log.execute('select * from Html1')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html2')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    file = open("index.html", "a")
    cur_log.execute('select * from Html3')
    for write_out in cur_log.fetchall():
        file.write(write_out[1])
    file.close()
    # ====================
    conn_log.close()
    return True