def head_name(str):
    import sqlite3
    conn_log = sqlite3.connect("index.db")
    cur_log = conn_log.cursor()
    cur_log.execute("delete from Html1 where id=9")
    conn_log.commit()
    tittle="<title>"+str+"</title>"
    cur_log.execute('''insert into Html1 Values(9,'{}')'''.format(tittle))
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