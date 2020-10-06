def head_name(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    tittle = "<title>" + str + "</title>"
    cur_log.execute('''update Html1 set statement='{}' where id=9'''.format(tittle))
    conn_log.commit()
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