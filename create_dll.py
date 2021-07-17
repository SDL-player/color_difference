import os

dir_ = "."

file = "functions"

os.system("gcc -m64 --share {0}\{1}.c -o {0}\{1}.dll".format(dir_, file))
