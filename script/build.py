#! python3
# build.py
# 1. 更新 cls 和手册的版本并编译手册
# 2. 将文件传输到 release 目录并压缩

import os
import shutil
import subprocess
import sys
from pathlib import Path
import datetime
import re
import zipfile
import send2trash
import pyinputplus as pyip

# 几个目录常量
originPath = Path("/Users/xiakangwei/Nutstore/Github/repository/whuthesis")
docPath = Path("/Users/xiakangwei/Nutstore/Github/repository/whuthesis/doc")
releasePath = Path("/Users/xiakangwei/Nutstore/Github/repository/whuthesis/release")

# 版本
try:
    version = str(sys.argv[1])
    # 让用户确认版本的输入
    while True:
        print('New version will be: v' + version + '. Are you sure?')
        answer = pyip.inputYesNo()
        if answer == 'no':
            version = input('Please type the new version: ')
            continue
        else:
            break
except IndexError:
    version = input('Please type the new version: ')
    # 让用户确认版本的输入
    while True:
        print('New version will be: v' + version + '. Are you sure?')
        answer = pyip.inputYesNo()
        if answer == 'no':
            print('Please type the new version: ')
            version = input()
            continue
        else:
            break

# 时间
dateNow = datetime.datetime.now()
# 将月份和日期都变成两位数，否则编译会报错
month = dateNow.month
month = f"{month:02d}"
day = dateNow.day
day = f"{day:02d}"
date = str(dateNow.year) + '/' + str(month) + '/' + str(day)

# 压缩包名称
releaseZipName = 'whuthesis-v' + version + '.zip'

# 更新 cls 和 main.tex 的版本

# 正则表达式
clsDateRegex = re.compile(r'\\ProvidesExplClass\s\{.*\}\s\{(\d{4}/\d{1,2}/\d{1,2})\}\s\{v(\d+\.\d+\.?\d*)\}')
# texDateRegex = re.compile(r'% update date: \d{4}-\d{1,2}-\d{1,2}')
# texVersionRegex = re.compile(r'% version: v\d{1}\.\d{1,2}\.\d{1,2}')
# docDateRegex = re.compile(r'\\newcommand\{\\DocDate\}\{(\d{4}-\d{1,2}-\d{1,2})\}')
docVersionRegex = re.compile(r'\\newcommand\{\\whu@version\}\{(\d+\.\d+\.?\d*)\}')


clsFile = 'whuthesis.cls'
docFile = 'whuthesis-doc.pdf'
# exampleFiles = ['ccnu-setup.tex', 'main.tex', 'main.pdf', 'whuthesis-main.bib', 'gb7714-CCNU.cbx', 'gb7714-CCNU.bbx', 'gb7714-CCNUay.bbx']
# helpFiles = ['CHANGELOG.md', 'README.md', 'LICENSE', 'latexmkrc', 'lguide-ch1.pdf']
# subFiles = ['back', 'body', 'copyright', 'figures', 'front', 'logo']


# 替换 cls 中的时间和版本
with open(originPath / clsFile, 'r') as file:
    content = file.read()
    content = clsDateRegex.sub(r'\\def\\whu@date{%s}' % (date), content)
    with open(originPath / clsFile, 'w') as newFile:
        newFile.write(content)

# # 替换 main.tex 的时间和版本
# with open(originPath / exampleFiles[1], 'r') as file:
#     content = file.read()
#     content = texDateRegex.sub(f'% update date: {date}', content)
#     content = texVersionRegex.sub(f'% version: v{version}', content)
#     with open(originPath / exampleFiles[1], 'w') as newFile:
#         newFile.write(content)


# # 更新手册版本并编译
# with open(docPath / 'whuthesis-doc.tex', 'r') as file:
#     content = file.read()
#     content = docDateRegex.sub(r'\\newcommand{\\DocDate}{%s}' % (date), content)
#     content = docVersionRegex.sub(r'\\newcommand{\\DocVersion}{v%s}' % (version), content)
#     with open(docPath / 'whuthesis-doc.tex', 'w') as newFile:
#         newFile.write(content)


# # 编译

# # 先将 working directory 改到 doc 再编译，这样可以使得一些相对路径不依赖 py 的位置
# # （其实就是相对路径要相对 tex 文件，所以要到那个目录下）

# # 编译示例文件
# os.chdir(originPath)
# LaTeXcompile = subprocess.run(['latexmk', '-xelatex', exampleFiles[1]], capture_output=True)  

# out = LaTeXcompile.stdout

# if out != '':
#     os.chdir(docPath)
#     LaTeXcompile = subprocess.run(['latexmk', '-xelatex', 'whuthesis-doc.tex'], capture_output=True)
#     out = LaTeXcompile.stdout

# # 复制文件到 release 并压缩

# if out != '':  # 表示编译已经结束
#     # 手册
#     shutil.copy(docPath / docFile, releasePath)
#     # 辅助文件
#     for helpFile in helpFiles:
#         shutil.copy(originPath / helpFile, releasePath)
#     # 主文件
#     shutil.copy(originPath / clsFile, releasePath)
#     for exampleFile in exampleFiles:
#         shutil.copy(originPath / exampleFile, releasePath)
#     # 分文件
#     for subFile in subFiles:
#         shutil.copytree(originPath / subFile, releasePath / subFile, dirs_exist_ok=True)
#     # 去掉 aux 文件
#     os.chdir(releasePath)
#     for foldName, subfolders, filenames in os.walk(releasePath):
#         for filename in filenames:
#             if filename.endswith('aux'):
#                 send2trash.send2trash(os.path.join(foldName, filename))
#     # 删除之前的压缩包
#     # 删除 release 目录的压缩包
#     if list(releasePath.glob('*.zip')):
#         send2trash.send2trash(list(releasePath.glob('*.zip'))[0])

#     # 压缩

#     os.chdir(releasePath)
#     with zipfile.ZipFile(releasePath / releaseZipName, 'w') as releaseZip:
#         # # 放入 release 目录中的文件
#         # for file in os.listdir(releasePath):
#         #     # 不把 zip 去掉的话会循环压缩
#         #     if not file.endswith('zip') and not file.endswith('DS_Store') and not file.startswith('__MACOSX/'):
#         #         releaseZip.write(file)
#         for path, dirnames, filenames in os.walk(releasePath):
#             relativePath = path.replace(str(releasePath), '')  # 把父目录路径去掉，剩下相对路径
#             # print(path)
#             # print(relativePath)
#             # print()
#             for filename in filenames:
#                 if not filename.endswith('zip') and not filename.endswith('DS_Store') and not filename.startswith('__MACOSX/'):
#                     # #1 表示原位置， #2 表示目标位置
#                     releaseZip.write(os.path.join(path, filename), os.path.join(relativePath, filename))
