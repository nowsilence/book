** 安装gitbook(需要node环境) **
``` 
sudo npm install gitbook-cli -g
```

** GitBook 常用命令 **
```
# 初始化
gitbook init

# 全量加载插件
gitbook install
或者单独
npm install gitbook-plugin-插件名 (只替换插件名部分)

# 编译
gitbook build

# 编译+开启本地服务
gitbook serve
```
** fontsettings  **
```
{
    "pluginsConfig": {
        "fontsettings": {
            "theme": 'white', // 'sepia', 'night' or 'white',
            "family": 'sans', // 'serif' or 'sans',
            "size": 2         // 1 - 4
        }
    }
}
```

