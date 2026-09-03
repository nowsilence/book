** 快捷键 **
```
# 导入Java类
shift+alt+O
```

** Javascript自动导入文件引号 **
```
在Preference->Setting搜索Quote Style
```

# 快捷键

功能	            Windows             Linux/Mac
格式化整个文档	    Shift + Alt + F	    Shift + Option + F
只格式化选中代码	Ctrl + K Ctrl + F	Cmd + K Cmd + F

vue开发默认的tab缩进是2个空格，可以通过设置修改为4个空格
.prettierrc放到根目录下，根package.json同级
```json
{
  "tabWidth": 4,
  "useTabs": false
}
```

settings.json 放到.vscode目录下
```json
{
  "editor.tabSize": 4,
//   "editor.detectIndentation": false, // 关闭自动检测，不被旧文件干扰
  "[vue]": {
    "editor.tabSize": 4, // vue文件单独强制4空格
    "editor.defaultFormatter": "Vue.volar"
  }
}
```