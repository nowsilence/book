LF（Line Feed）：表示换行符，ASCII 编码为 10（十六进制 0x0A）。最早源于 Unix 系统，目前被 Linux、macOS、FreeBSD 等类 Unix 操作系统采用。在这些系统中，仅需一个 LF 字符就能完成 “换行” 操作，即光标从当前行末尾直接移到下一行开头。

CRLF（Carriage Return + Line Feed）：表示回车 + 换行，由两个字符组成 ——CR（ASCII 编码 13，0x0D）负责 “回车”（光标回到当前行开头），LF 负责 “换行”（光标下移一行）。这种组合源于早期打字机的操作逻辑，目前被 Windows 操作系统采用，Windows 下的文本文件默认使用 CRLF 作为换行符。
起源于打字机时代：回车（将打印头移回行首）+ 换行（将纸张上移一行）Windows系统继承此传统，使用CRLF作为行结束符

Git 中的 core.autocrlf默认为true
‌core.autocrlf=true：
提交代码时：自动把本地 Windows 的 \r\n 转换成 \n 存入仓库
拉取代码时：自动把仓库里的 \n 转换成 Windows 本地 \r\n

core.autocrlf = input（Mac / Linux 推荐）
检出：保持 LF 不变
提交：自动把文件里的 CRLF 转成 LF
不会修改本地换行，只规范入库格式

项目根目录新建 .gitattributes，强制统一换行，彻底避免冲突：
plaintext
* text=auto eol=lf
*.sh text eol=lf
*.bat text eol=crlf


## 一、默认值区分平台

1. **Windows 版 Git（Git for Windows）**
安装向导默认勾选「Checkout Windows-style, commit Unix-style line endings」，等价自动配置 `core.autocrlf = true`；
2. **Mac / Linux 系统 Git**
默认 `core.autocrlf = false`，不会自动转换换行符。

