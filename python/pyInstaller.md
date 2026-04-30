# PyInstaller 

## 是什么？
把 Python 代码 + 所有依赖库 + Python 解释器
打包成 一个独立可执行文件。
Windows → .exe
Mac → .app/ 可执行文件
别人不用装 Python
别人不用 pip 安装任何库
双击直接运行

## 安装
```shell
pip install pyinstaller
```

## 命令
```shell
# -F 打包成一个单独文件
# -w 不弹出黑色命令行窗口（GUI 程序必用）
# -i logo.ico windows .ico mac .icns
pyinstaller -F -w 你的文件.py


pyinstaller -F -w -i logo.ico 你的文件.py #  带上图标

# 单个 exe = 运行前要先解压 → 慢
# 文件夹 = 直接运行 → 快
pyinstaller -w 你的文件.py # 打包成文件夹

pyinstaller 你的文件.py

```

