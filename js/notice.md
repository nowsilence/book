```
在JavaScript标准中规定了二进制位运算时其操作数长度为32位，其最高位为符号位，因此能够表示的有效数字位数为31位。
对于浮点数会向下取整转成整数在为运算。

‌核心功能‌：x | 0 会将 x 转换为一个 32 位整数，去掉小数部分，且向零方向取整（即向下取整，对于负数则向上取整使其更接近零）

``` 