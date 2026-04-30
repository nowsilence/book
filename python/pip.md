pip 在安装Python时自带

```shell
# 安装依赖
pip install tushare
pip freeze > requirements.txt # 导出当前所有安装的库
pip install -r requirements.txt # 安装指定的依赖 -r 即 --requirement

```
直接使用可能报：pip: command not found
原因是我在安装python的时候使用的是
```shell
brew install python@3.12
```
Homebrew安装的 Python 3.12，pip 不叫 pip，叫 pip3.12
可以使用下面命令：
```shell
pip3.12 install tushare # 或者
pip3 install tushare # 或者
python3 -m pip install tushare # -m = module（模块）python3 -m pip 运行一个自带的模块
```