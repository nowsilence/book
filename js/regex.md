```
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

// 匹配属性
const attrReg = /\s*(.+?)\s*=\s*"\s*(.+?)\s*"/g;
attrReg.exec(attr);
```