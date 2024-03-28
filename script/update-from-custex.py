"""
update-from-custex.py
Author: 夏大鱼羊
Date: 2024/03/28
Description:
    - [✔] 从 custex 仓库中复制 `.sty`, `.cls`, `cus.module.xxx.tex` 和 `cus.library.xxx.tex` 文件
        - [✔]`cus.module.xxx.tex` 和 `whu.library.xxx.tex` 文件改名为 `whu.module.xxx_cus.tex` 和 `cus.library.xxx_cus.tex` 文件
        - [✔]`cus.sty` 和 `cusclass.cls` 文件改名为 `whu.sty` 和 `whuclass.cls`
    - [✔]修改这些文件中的字符串:
        - [✔]`cus` 为 `whu`
        - [✔]`Cus` 为 `Whu`
        - [✔]`CUS` 为 `WHU`
    - [✔]修改 `whu.module.xxx_cus.tex` 中的 `\WHUProvideModule{xxx}` 或 `\WHUProvideExplModule{xxx}` 的 `xxx` 为 `xxx_cus`
    - [✔]修改 `whu.library.xxx_cus.tex` 中的 `\WHUProvideLibrary{xxx}` 或 `\WHUProvideExplLibrary{xxx}` 的 `xxx` 为 `xxx_cus`
    - 修改 `whu.sty`
        - [✔]将 `Chinese User Scheme (WHU) basic file` 修改为 `Basic file of thesis template for Wuhan university`
        - 将 `\WHULoadModule { xxx }` 命令修改为 `\WHULoadModule { xxx_cus }`
"""
import os
import shutil
import re



# 源目录和目标目录
cus_directory = "/Users/xiakangwei/Nutstore/Github/repository/custex"
whu_directory = "/Users/xiakangwei/Nutstore/Github/repository/whuthesis"


def modify_cus_to_whu(file_path: str):
    """
    修改文件中的字符串
    - `cus` 为 `whu`
    - `Cus` 为 `Whu`
    - `CUS` 为 `WHU`
    """
    with open(file_path , 'r', encoding='utf-8') as f:
        file_content = f.read()
    # 修改文件中的字符串
    file_content = file_content.replace('cus', 'whu').replace('Cus', 'Whu').replace('CUS', 'WHU')
    with open(file_path , 'w', encoding='utf-8') as f:
        f.write(file_content)



"""
从 custex 仓库中复制 `.sty`, `.cls`, `cus.module.xxx.tex` 和 `cus.library.xxx.tex` 文件

- `cus.module.xxx.tex` 和 `whu.library.xxx.tex` 文件改名为 `whu.module.xxx_cus.tex` 和 `cus.library.xxx_cus.tex` 文件

- `cus.sty` 和 `cusclass.cls` 文件改名为 `whu.sty` 和 `whuclass.cls`
"""
for file in os.listdir(cus_directory):
    # file_path 表示文件的绝对路径
    file_path = os.path.join(cus_directory, file)
    # 判断 file_path 是否是文件还是文件夹，只处理文件
    if os.path.isfile(file_path):
        # 如果文件是 'cus.sty' 或 'cusclass.cls'，则修改标题后复制到 whu 目录
        if file == 'cus.sty' or file == 'cusclass.cls':
            source_file_path = file_path
            target_file_path = os.path.join(whu_directory, file.replace('cus', 'whu'))
            shutil.copy(source_file_path, target_file_path)
            # 修改文件中的 cus 为 whu
            modify_cus_to_whu(target_file_path)
        # 其它的 '.sty' 文件直接复制到 whu 目录
        elif file.endswith('.sty') and 'cus' not in file:
            source_file_path = file_path
            target_file_path = os.path.join(whu_directory, file)
            shutil.copy(source_file_path, target_file_path)
        else:
            # 处理以 '.tex' 结尾并以 'cus' 开头的文件
            if file.endswith('.tex') and file.startswith('cus'):
                source_file_path = file_path
                # 如果是 module 或 library 文件，则还需要在 module 名后加上 '_cus'
                if 'module' in file or 'library' in file:
                    target_file_path = os.path.join(whu_directory, file.replace('cus', 'whu').replace('.tex', '_cus.tex'))
                else:
                    # 其余文件直接替换 cus 即可
                    target_file_path = os.path.join(whu_directory, file.replace('cus', 'whu'))
                # 复制文件
                shutil.copy(source_file_path, target_file_path)
                # 修改文件中的 cus 为 whu
                modify_cus_to_whu(target_file_path)



"""
修改 `whu.module.xxx_cus.tex` 中的 `\WHUProvideModule{xxx}` 或 `\WHUProvideExplModule{xxx}` 的 `xxx` 为 `xxx_cus`
"""
for file in os.listdir(whu_directory):
    file_path = os.path.join(whu_directory, file)
    # 文件夹不处理
    if os.path.isfile(file_path):
        # 处理 module 文件
        if file.startswith('whu.module') and file.endswith('_cus.tex'):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                # 修改文件中的字符串
                file_content = re.sub(r'\\WHUProvide(Module|ExplModule){(.*?)}', r'\\WHUProvide\1{\2_cus}', file_content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)



"""
修改 `whu.library.xxx_cus.tex` 中的 `\WHUProvideLibrary{xxx}` 或 `\WHUProvideExplLibrary{xxx}` 的 `xxx` 为 `xxx_cus`
"""
for file in os.listdir(whu_directory):
    file_path = os.path.join(whu_directory, file)
    # 文件夹不处理
    if os.path.isfile(file_path):
        # 处理 library 文件
        if file.startswith('whu.library') and file.endswith('_cus.tex'):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                # 修改文件中的字符串
                file_content = re.sub(r'\\WHUProvide(Library|ExplLibrary){(.*?)}', r'\\WHUProvide\1{\2_cus}', file_content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)


# 修改 `whu.sty`

"""
将 `Chinese User Scheme (WHU) basic file` 修改为 `Basic file of thesis template for Wuhan university`
"""
whu_sty_path = os.path.join(whu_directory, 'whu.sty')
with open(whu_sty_path, 'r', encoding='utf-8') as f:
    file_content = f.read()
    file_content = file_content.replace('Chinese User Scheme (WHU) basic file', 'Basic file of thesis template for Wuhan university')
with open(whu_sty_path, 'w', encoding='utf-8') as f:
    f.write(file_content)



"""
将 `\WHULoadModule { xxx }` 命令修改为 `\WHULoadModule { xxx_cus }`
"""
with open(whu_sty_path, 'r', encoding='utf-8') as whu_sty_file:
    lines = whu_sty_file.readlines()
    for idx, line in enumerate(lines):
        if line.startswith('\\WHULoadModule') and not line.startswith('\\NewDocumentCommand \\WHULoadModule'):
            lines[idx] = re.sub(r'\\WHULoadModule\s*{\s*(\S+)\s*}', r'\\WHULoadModule { \1_cus }', line)

with open(whu_sty_path, 'w', encoding='utf-8') as whu_sty_file:
    whu_sty_file.writelines(lines)