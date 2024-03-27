import os
import shutil

cus_directory = "/Users/xiakangwei/Nutstore/Github/repository/custex"
whu_directory = "/Users/xiakangwei/Nutstore/Github/repository/whuthesis"

# 寻找文件并复制
for root, _, files in os.walk(cus_directory):
    for file in files:
        if file.endswith('.tex') and file.startswith('cus'):
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(whu_directory, file.replace('cus', 'whu'))
            shutil.copy(source_file_path, target_file_path)
        elif file.endswith('.sty') and file != 'cus.sty':
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(whu_directory, file)
            shutil.copy(source_file_path, target_file_path)
        elif file == 'cus.sty' or file == 'cusclass.cls':
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(whu_directory, file.replace('cus', 'whu'))
            shutil.copy(source_file_path, target_file_path)

# 处理文本文件内容
for root, _, files in os.walk(whu_directory):
    for file in files:
        if file.endswith('.tex') or file.endswith('.sty') or file.endswith('.cls'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 替换文本内容中的字符串
            content = content.replace('cus', 'whu')
            content = content.replace('Cus', 'Whu')
            content = content.replace('CUS', 'WHU')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

# 打开 whuthesis.cls 文件，找到指定行并获取内容
whu_cls_path = os.path.join(whu_directory, 'whuthesis.cls')
whu_sty_path = os.path.join(whu_directory, 'whu.sty')

with open(whu_cls_path, 'r', encoding='utf-8') as whu_cls_file:
    lines = whu_cls_file.readlines()
    for line in lines:
        if '@d@te' in line:
            whu_date_line = line.strip()
        if '@versi@n' in line:
            whu_version_line = line.strip()

# 打开 whu.sty 文件，找到指定行并替换内容
whu_sty_path = os.path.join(whu_directory, 'whu.sty')

with open(whu_sty_path, 'r', encoding='utf-8') as whu_sty_file:
    lines = whu_sty_file.readlines()
    for idx, line in enumerate(lines):
        if '\\def\\whu@d@te' in line:
            lines[idx] = '\\def\\whu@d@te{2024/03/27}\n'
        if '\\def\\whu@versi@n' in line:
            lines[idx] = '\\def\\whu@versi@n{0.0.1}\n'

with open(whu_sty_path, 'w', encoding='utf-8') as whu_sty_file:
    whu_sty_file.writelines(lines)
    
    
# 替换 whu.sty 文件中的指定内容
whu_sty_path = os.path.join(whu_directory, 'whu.sty')

with open(whu_sty_path, 'r', encoding='utf-8') as whu_sty_file:
    whu_sty_content = whu_sty_file.read()

whu_sty_content = whu_sty_content.replace(
    'Chinese User Scheme (WHU) basic file',
    'Basic file of thesis template for Wuhan university')

with open(whu_sty_path, 'w', encoding='utf-8') as whu_sty_file:
    whu_sty_file.write(whu_sty_content)