macOS Monterey（12.3）起彻底移除了系统自带Python 2.7，且不再预装 Python3
如果说你没手动安装python3，但是系统有，例如 /Users/nigel/Library/Python/3.9
这是来自Xcode 命令行工具（/usr/bin/python3），仅为兼容系统脚本，属于 “临时桥接”，并非完整开发环境。
删除/usr/bin/python3 可能破坏系统功能，只需忽略它
最好是不要使用他作为开发环境，原因：
    下次 macOS 系统更新 → 你安装的库全清空
    系统 Python 锁死版本，永远 3.9

/usr/bin/pip3 也是临时桥接

## 安装python3.12
```shell
# 安装前先看下pyenv，在下面
brew install python@3.12 # 会被安装到 /usr/local/Cellar/python@3.12
python3.12 -m pip install tushare # 会把依赖库安装到3.12目录里
```

## 创建虚拟环境
```shell
python3.12 -m venv myenv # myenv 虚拟环境名称，存放在当前目录，myenv文件夹名称，可以是个路径
source myenv/bin/activate # 进入虚拟环境，source就是一个mac终端命令，作用只有一个：运行一个文件里的命令
# 后面执行的pip安装、运行代码，都只在这个独立小环境里，完全不碰系统、不碰 Homebrew、不污染任何东西。

deactivate # 退出环境
```

## Python多版本管理：pyenv
```shell
# 必须使用pyenv install进行安装python，否则无法管理
brew install pyenv
pyenv install --list # 可安装版本列表
pyenv install 3.16.0 #  安装任意版本
pyenv versions # 查看 pyenv 管理的版本
pyenv global 3.16.0 # 把 3.16 设为全局默认

python --version # 查看当前用的哪个版本

pyenv uninstall 3.12.0 # 卸载
```

指定版本后，执行python --version，如果报错，执行以下代码
```shell
# 1 pyenv 装完后，必须加 3 行配置才能让 python 命令生效
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

# 2 
source ~/.bash_profile
```