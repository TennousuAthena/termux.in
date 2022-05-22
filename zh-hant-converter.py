#!/usr/bin/python3
import os, opencc

def convert_file(filename):
    converter = opencc.OpenCC('s2t.json')
    with open(filename,'r+') as f:
        s=f.read()
        f.seek(0,0)
        f.write(converter.convert(s))
        f.close()


paths = os.walk(r'./docs')


for path, dir_lst, file_lst in paths:
    for file_name in file_lst:
        if ".md" in file_name:
            convert_file(os.path.join(path, file_name))

