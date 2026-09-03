# MySQL #

## 字符编码 ##

MySQL 里的 **`utf8` ≠ 标准 UTF-8**

**`utf8`（MySQL 旧实现）**：仅支持**最多 3 字节 UTF-8**；不能存储：emoji 表情、部分生僻汉字、冷门符号（😀、𠮷等）
**`utf8mb4`**：**真正完整 UTF-8**，支持**1～4 字节字符**；支持所有 Unicode，包含全部 emoji、扩展汉字
mb4 = most bytes 4