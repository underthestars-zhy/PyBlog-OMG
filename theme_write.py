def page_write(name, path_, time_, txt, pic_url):
    if name == 'About' or name == 'about' or name == 'ABOUT':
        try:
            import time
            import sqlite3
            conn_log = sqlite3.connect("index.db")
            cur_log = conn_log.cursor()
            maintime = "\t\t\t\t\t\t\t\t\t\t\t\t<i></i>Time: "+str(time_)+"\n"
            cur_log.execute('''update Page1 set statement='{}' where id=86'''.format(maintime))
            conn_log.commit()
            pic = f"\t\t<img src=\"{pic_url}\" class=\"banner-img\">"
            cur_log.execute('''update Page1 set statement='{}' where id=80'''.format(pic))
            conn_log.commit()
            time.sleep(1)
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
            file.close()
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
    else:
        try:
            import time
            import sqlite3
            conn_log = sqlite3.connect("index.db")
            cur_log = conn_log.cursor()
            maintime = "\t\t\t\t\t\t\t\t\t\t\t\t<i></i>Time: " + str(time_) + "\n"
            cur_log.execute('''update Page1 set statement='{}' where id=86'''.format(maintime))
            conn_log.commit()
            pic = f"\t\t<img src=\"{pic_url}\" class=\"banner-img\">"
            cur_log.execute('''update Page1 set statement='{}' where id=80'''.format(pic))
            conn_log.commit()
            tittle = "\t\t\t\t\t<h1 class=\"banner-title archive-title\">"+name+"</h1>"
            cur_log.execute('''update Page1 set statement='{}' where id=84'''.format(tittle))
            conn_log.commit()
            time.sleep(1)
            # =====================
            file = open(path_+".html", "w")
            cur_log.execute('select * from Page1')
            for write_out in cur_log.fetchall():
                file.write(str(write_out[1]))
            file.close()
            # =====================
            file = open(path_+".html", "a")
            import markdown
            file.write(str(markdown.markdown(txt)))
            file.close()
            # ====================
            file = open(path_+".html", "a")
            cur_log.execute('select * from Page2')
            for write_out in cur_log.fetchall():
                file.write(str(write_out[1]))
            file.close()
            conn_log.close()
            return True
        except:
            return False