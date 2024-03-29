# 更新日志

## [v0.0.1] - 2024-03-29

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