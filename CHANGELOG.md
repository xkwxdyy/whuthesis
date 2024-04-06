# 更新日志

## [v0.0.3] - 2024-04-06

### Added

- 增加 `newlibrary.py` 脚本用于新建库
- 增加 2024 年本科生 word 模板
- 增加两个测试文件
- 基本完成黄正华老师硕士模板的兼容

### Changed

- 增加和完善一些库
- 更新了一些 `TODO` 的内容
- 将 `declaration` 和 `authorization` 改成 `chapter` 处理
- 优化 `for-library` 的 `cleardoublepage` 的处理为局部处理
- Readme: 改为以库为核心
- 优化 master 的 degree-type 键值

### Fixed

- 修复 `for-library` 的空白页问题
- 修复 `information` 和 `constant`不能二次 `set` 的问题

### Removed

- 移除 `whuclass.cls`


## [v0.0.2] - 2024-04-04

### Added

- 增加 `武汉大学学位论文使用授权协议书`
- 增加关键词的格式调整
- `type` 库增加字符串处理


### Changed

- `update-from-custex.py` 适配 `cus` 的模板和库的路径移动
- `constant` 库中的变量改为 `g`类型




## [v0.0.1] - 2024-04-02

### Added

- 增加 `gb7714-WHU.cbx`
- `whuthesis.cls`
  - 增加版权说明
  - 增加 `library` 的文档类选项
- 增加未完成的 `build.py` 脚本
- 增加两个 logo
- 增加一些 TODO
- 增加 `math` 的相关库（未完成）
- 增加本硕博库（未开始）
- 增加 `math` 库的参考资料


### Changed

- 文件名采用 `pgf` 规范（https://github.com/Sophanatprime/cus/issues/13#issuecomment-2029553021）
- 自定义内容全部改为以 `library` 形式
- `whuthesis.cls` 改为 `\LoadClass` 前载入 `whu` 宏包（https://github.com/Sophanatprime/cus/commit/f0d8c9c042f5c72a29c1bd012517aee74b235f4a）
- `update-from-custex.py` 脚本将 `_cus` 的处理改为 `.cus`
- 修改模块和库的路径（https://github.com/Sophanatprime/cus/issues/19）
- `update-from-custex.py` 适配模板和库的路径移动




## [v0.0.1] - 2024-03-29

### Added

- 增加 `update-from-custex.py` 脚本功能：增加文件版权说明


### Fixed

- `cus` 修复 对 `pgf` 和 `tcb` 的处理（[cus/issues/#7](https://github.com/Sophanatprime/cus/issues/7)
- `cus` 修复与 `biblatex` 宏包的冲突（[cus/issues/#8](https://github.com/Sophanatprime/cus/issues/8)



## [v0.0.1] - 2024-03-28

### Added

- 增加用户手册，完成简介部分


### Changed

- 将 `whuthesis` 的日期和版本号与 `CusTeX` 的分开


### Fixed

- 重写 `update-from-custex.py` 脚本，完善功能，处理文件后缀，防止模块和库名称和 `CusTeX` 的冲突
- `update-from-custex.py` 脚本处理 `\WHUDependency` 里的模块后缀和库后缀
 

## [v0.0.1] - 2024-03-27

### Added

- 增加脚本 `update-from-custex.py`
  - 复制 `cus` 项目的主要文件并替换文件名和文件内容的 `cus` 为 `whu`
  - 替换 `whu.sty` 的日期和版本为 `whuthesis.cls` 中日期和版本
  - 替换 `whu.sty` 的文件描述