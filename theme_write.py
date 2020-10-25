def page_write(name, time, txt):
    if name == 'About' or name == 'about' or name == 'ABOUT':
        try:
            import sqlite3
            conn_log = sqlite3.connect("index.db")
            cur_log = conn_log.cursor()
            maintime = "\t\t\t\t\t\t\t\t\t\t\t\t<i></i>Time: "+time+"\n"
            cur_log.execute('''update Page1 set statement='{}' where id=86'''.format(maintime))
            conn_log.commit()
            # =====================
            file = open("about.html", "w")
            cur_log.execute('select * from Page1')
            for write_out in cur_log.fetchall():
                file.write(str(write_out[1]))
            file.close()
            # =====================
            file = open("about.html", "a")
            import markdown
            file.write(str(markdown.markdown(txt)))
            # ====================
            file = open("about.html", "a")
            cur_log.execute('select * from Page2')
            for write_out in cur_log.fetchall():
                file.write(str(write_out[1]))
            file.close()
            conn_log.close()
            return True
        except:
            return False