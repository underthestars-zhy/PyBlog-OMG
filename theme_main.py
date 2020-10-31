def theme_main ():
    import os
    try:
        os.system("rm main_txt.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/main_txt.py")
        os.system("rm main_com.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/main_com.py")
        os.system("rm index.py")
        os.system("wget https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/index.py")
        os.system("clear")
        return True
    except:
        return False
def theme_tf ():
    return "OMG"

def version():
    return "Beat5"

def least_version_url():
    return 'https://github.com/underthestars-zhy/PyBlog-OMG/raw/main/version_theme.txt'