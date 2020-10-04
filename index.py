def main_index():
    import os
    try:
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/mian_index.tar")
        os.system("tar xvf mian_index.tar ")
        os.system("rm -rf mian_index.tar")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/index.html")
        os.system("clear")
        return True
    except:
        return False