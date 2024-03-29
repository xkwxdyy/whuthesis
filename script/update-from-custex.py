"""
update-from-custex.py
Author: 夏大鱼羊
Date: 2024/03/29
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
    - [✔]`whu.module.xxx_cus.tex` 或 `whu.library.xxx_cus.tex` 中若有 `\WHUDependency{}`，且 `{}` 中包含 `module={xxx,yyy}` 或者 `library={zzz,www}`，则将 `...` 改为 `..._cus`
    - [✔]修改 `whu.sty`
        - [✔]将 `Chinese User Scheme (WHU) basic file` 修改为 `Basic file of thesis template for Wuhan university`
        - [✔]将 `\WHULoadModule { xxx }` 命令修改为 `\WHULoadModule { xxx_cus }`
        - [✔]将 `pgf_cus` 和 `tcb_cus` 加入 \c__whu_library_delayed_prop 
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


"""
`whu.module.xxx_cus.tex` 或 `whu.library.xxx_cus.tex` 中若有 `\WHUDependency{}`，且 `{}` 中包含 `module={xxx,yyy}` 或者 `library={zzz,www}`，则将 `...` 改为 `..._cus`
"""
# 定义替换函数
def replace_dependency(input_str):
    # 查找匹配 module 和 library 的正则表达式
    module_pattern = r'module={([^}]*)}'
    library_pattern = r'library={([^}]*)}'

    # 查找 module 和 library 中的所有项
    module_match = re.search(module_pattern, input_str)
    library_match = re.search(library_pattern, input_str)

    if module_match:
        # 将 module 中的项替换为带有 _cus 后缀的项
        old_module_items = module_match.group(1).split(',')
        new_module_items = [item.strip() + '_cus' for item in old_module_items]
        # 替换原始字符串中的 module 部分
        input_str = re.sub(module_pattern, 'module={' + ','.join(new_module_items) + '}', input_str)

    if library_match:
        # 将 library 中的项替换为带有 _cus 后缀的项
        old_library_items = library_match.group(1).split(',')
        new_library_items = [item.strip() + '_cus' for item in old_library_items]
        # 替换原始字符串中的 library 部分
        input_str = re.sub(library_pattern, 'library={' + ','.join(new_library_items) + '}', input_str)

    return input_str

for file in os.listdir(whu_directory):
    file_path = os.path.join(whu_directory, file)
    # 文件夹不处理
    if os.path.isfile(file_path):
        # 处理 module 文件
        if file.startswith('whu.module') and file.endswith('_cus.tex'):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                # 修改文件中的字符串
                if "WHUDependency" in file_content:
                    file_content = replace_dependency(file_content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
        # 处理 library 文件
        if file.startswith('whu.library') and file.endswith('_cus.tex'):
            with open(file_path , 'r', encoding='utf-8') as f:
                file_content = f.read()
                # 修改文件中的字符串
                if "WHUDependency" in file_content:
                    file_content = replace_dependency(file_content)
            with open(file_path , 'w', encoding='utf-8') as f:
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



"""
将 `pgf_cus` 和 `tcb_cus` 加入 \c__whu_library_delayed_prop

ref: https://github.com/Sophanatprime/cus/issues/7
"""
old_latex_code_WHULoadLibrary = r'''
\NewDocumentCommand \WHULoadLibrary { m O{} O{0000/00/00} }
  {
    \prop_if_in:NnTF \c__whu_library_delayed_prop {#1}
      {
        \hook_gput_code:nnn 
          { package/ \prop_item:Nn \c__whu_library_delayed_prop {#1} / after }
          { whu/load }
          { \__whu_load_library_real:nnn {#1} {#2} {#3} }
      }
      { \__whu_load_library_real:nnn {#1} {#2} {#3} }
  }
'''

new_latex_code_WHULoadLibrary = r'''
\NewDocumentCommand \WHULoadLibrary { m O{} O{0000/00/00} }
  {
    \prop_set_from_keyval:Nn \c__whu_library_delayed_prop 
      {
        pgf     = tikz,
        tcb     = tcolorbox,
        pgf_cus = tikz,
        tcb_cus = tcolorbox
      }
    \prop_if_in:NnTF \c__whu_library_delayed_prop {#1}
      {
        \hook_gput_code:nnn 
          { package/ \prop_item:Nn \c__whu_library_delayed_prop {#1} / after }
          { whu/load }
          { \__whu_load_library_real:nnn {#1} {#2} {#3} }
      }
      { \__whu_load_library_real:nnn {#1} {#2} {#3} }
  }
'''
whu_sty_path = os.path.join(whu_directory, 'whu.sty')
with open(whu_sty_path, 'r', encoding='utf-8') as f:
    file_content = f.read()
    file_content = file_content.replace(old_latex_code_WHULoadLibrary, new_latex_code_WHULoadLibrary)
with open(whu_sty_path, 'w', encoding='utf-8') as f:
    f.write(file_content)