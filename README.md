# Pyinstaller_Template
> 有关Pyinstaller的打包模板

## 虚拟环境迁移

- 在 `vene\pyvenv.cfg` 记事本修改路径
  - `home` 全局 Python 路径
  - `executable` 全局 Python 路径
  - `command` 全局 Python 路径 + 项目路径
- 在 `venv\Scripts\activate.bat` 记事本修改 `set VIRTUAL_ENV=...` 更改路径为要迁移的路径
- 在 `venv\Scripts\activate` 记事本修改 `VIRTUAL_ENV=...` 更改路径为要迁移的路径
- 迁移后无法直接使用 pip, 需要 cmd 激活虚拟环境后输入 
	- `python -m pip install --upgrade pip` 重新激活 pip
- 因迁移而无法使用的第三方库, 可以先卸载再安装

## ⭐编译打包

- 编译前请先配置 build.spec 文件
- 打包前建议先删除 `build` `dist` 两个文件夹
- 终端输入 `Pyinstaller build.spec` 进行打包
