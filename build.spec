# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from pprint import pprint


from os.path import join, basename, dirname, exists
from os import walk, makedirs, sep
from shutil import copyfile, rmtree
name_ = 'run'


# 初始化定义
binaries = [] # 添加二进制文件
datas = []
my_files = ['config.txt','de.py'] # 额外所需文件
my_folders = ['assets', 'util'] # 复制文件夹中所有文件
hiddenimports_ = ['util.pt'] # 导入动态模块 / 添加打包程序找不到的模块
excludes_ = [] # 不需要导入的包
icon_ = ['assets\\icon.ico'] # 图标路径
console_ = True # 是否显示命令行窗口
private_module = [ ] # 不需要打包的文件

# 额外复制 dll
modules = ['onnxruntime']
for module in modules: 
    tmp_ret = collect_all(module)
    binaries += tmp_ret[1]

a = Analysis(
    ['main.py'],
    pathex=[], 
    binaries=binaries,
    datas=datas, 
    hiddenimports=hiddenimports_,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['build_hook.py'],
    excludes=excludes_,
    noarchive=False,
    optimize=0,
)

# 排除不要打包的模块


pure = a.pure.copy()
a.pure.clear()
for name, src, type in pure:
    condition = [name == m or name.startswith(m + '.') for m in private_module]
    if condition and any(condition):
        ...
    else:
        a.pure.append((name, src, type))    # 把需要保留打包的 py 文件重新添加回 a.pure

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=name_,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=console_,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_,
    contents_directory='internal',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=name_,
)

# 复制额外所需的文件, 该文件可以在打包后继续修改

dest_root = join('dist', basename(coll.name))
for folder in my_folders:
    for dirpath, dirnames, filenames in walk(folder):
        for filename in filenames:
            my_files.append(join(dirpath, filename))
for file in my_files:
    if not exists(file):
        continue
    dest_file = join(dest_root, file)
    dest_folder = dirname(dest_file)
    makedirs(dest_folder, exist_ok=True)
    copyfile(file, dest_file)
