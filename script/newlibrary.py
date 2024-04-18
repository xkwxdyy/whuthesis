"""
newlibrary.py
Author: 夏大鱼羊
Date: 2024/04/05
Description: 新建一个库
"""

import sys
import pyinputplus as pyip

library_directory = "/Users/xiakangwei/Nutstore/Github/repository/whuthesis/library"


try:
    library_name = str(sys.argv[1])
    # 确认库的名称的输入
    while True:
        print('The name of the new library will be: ' + library_name + '. Are you sure?')
        answer = pyip.inputYesNo()
        if answer == 'no':
            library_name = input('Please type the name the new library: ')
            continue
        else:
            break
except IndexError:
    library_name = input('Please type the name the new library: ')
    # 确认库的名称的输入
    while True:
        print('The name of the new library will be: ' + library_name + '. Are you sure?')
        answer = pyip.inputYesNo()
        if answer == 'no':
            print('Please type the name the new library: ')
            library_name = input()
            continue
        else:
            break


# 新建一个文件，`whu.library.library_name.tex`
library_file = open(library_directory + '/whu.library.' + library_name + '.tex', 'w')
    # 然后写入 "\WHUProvideExplLibrary{library_name}{\whu@date}{\whu@version}{}"
library_file.write("\\WHUProvideExplLibrary{" + library_name + "}{\\whu@date}{\\whu@version}{}")
library_file.close()