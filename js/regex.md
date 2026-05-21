```js
const str = `
some text
<font size="3" color="red">This is some text!</font>
<font size="2" color="blue">This is some text!</font>
<font face="verdana" color="green">This is some text!</font>
some text
`;

// 匹配所有的font标签

const reg = /<\s*font\s+(.+?)>(.*?)<\s*\/\s*font\s*>/g;
reg.exec(str);

正则执行逻辑:
匹配到 <font ...>
开始走 (.*?)
每吃一个字符，就回头看一眼：后面是不是 </font>？
一旦发现后面是结束符 </font>，马上停止！

总结：.*? = 吃到结束标志就停，绝不往前多走一步！


// 匹配属性
const attrReg = /\s*(.+?)\s*=\s*"\s*(.+?)\s*"/g;
attrReg.exec(attr);

(.*?) // 非贪婪模式 例如：{(.*?)}，'{123}sdfsf}' 之后匹配到第一个},{(.*)}（贪婪模式）后匹配到最后一个}
正则默认是贪婪匹配（尽可能多拿字符），加?后变成非贪婪（尽可能少拿字符）。

// 以后面的字符串开始
^car
// 匹配除了0-9或者a-z之外的其他字符。
[^1-9a-z]

// 非捕获组
(?:pattern)
匹配 pattern 而不将其加入捕获组。
new RegExp('(?:a)(b)(c)').exec('abc')
//  ['abc', 'b', 'c', index: 0, input: 'abc', groups: undefined]

断言
https://blog.csdn.net/qq_18237141/article/details/132567686
```