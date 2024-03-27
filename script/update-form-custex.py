import os
import shutil
import re

cus_directory = "/Users/xiakangwei/Nutstore/Github/repository/custex"
whu_directory = "/Users/xiakangwei/Nutstore/Github/repository/whuthesis"

# 寻找文件并复制
for root, dirs, files in os.walk(cus_directory):
    for file in files:
        if file.endswith('.tex') and file.startswith('cus'):
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(whu_directory, file.replace('cus', 'whu'))
            shutil.copy(source_file_path, target_file_path)
        elif file.endswith('.sty') or file.endswith('.cls'):
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(whu_directory, file)
            shutil.copy(source_file_path, target_file_path)

# 处理文本文件内容
for root, _, files in os.walk(whu_directory):
    for file in files:
        if file.endswith('.tex') or file.endswith('.sty') or file.endswith('.cls'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 替换文本内容中的字符串
            content = re.sub(r'\bcus\b', 'whu', content)
            content = re.sub(r'\bCus\b', 'Whu', content)
            content = re.sub(r'\bCUS\b', 'WHU', content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)