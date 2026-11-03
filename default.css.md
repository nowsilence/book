```css
/* 全局默认样式重置 */
/* 基础重置 */
/* 通配选择器：清除所有元素及伪元素的内外边距，并统一盒模型为 border-box */
*,
*::before,
*::after {
  margin: 0;              /* 清除默认外边距 */
  padding: 0;             /* 清除默认内边距 */
  box-sizing: border-box; /* 盒模型以边框为基准，padding/border 计入宽高 */
  -moz-user-select: none; /* Firefox私有属性 */
  /* 用于控制元素是否可被用户选中（鼠标拖拽高亮文本） */
  -webkit-user-select: none; /* WebKit内核私有属性 */
  -ms-user-select: none; /* IE私有属性(IE10及以后) */
  -khtml-user-select: none; /* KHTML内核私有属性 */
  -o-user-select: none; /* Opera私有属性 */
  user-select: none; CSS3属性
}

/* 根元素（HTML）基础排版设置 */
html {
  line-height: 1.5;       /* 行高为字体大小的 1.5 倍 */
  tab-size: 4;            /* 制表符（Tab）显示为 4 个空格宽度 */
  font-size: 16px;        /* 设置根字号，作为 rem 单位计算基准 */
}

/* 页面主体样式 */
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; /* 优先使用系统字体 */
  color: #222;            /* 默认文字颜色（深灰） */
  background: #ffffff;    /* 页面背景色（白） */
  min-height: 100vh;      /* 至少占满整个视口高度 */
}

/* 水平分隔线基础样式 */
hr {
  height: 0;              /* 不占高度，仅靠边框显示 */
  border-width: 1px 0 0 0;/* 仅保留上边框，形成一条横线 */
  border-color: #eee;     /* 边框颜色（浅灰） */
}

/* 加粗文字 */
b, strong {
  font-weight: 700;       /* 加粗字重 */
}

/* 等宽字体相关元素（代码、按键、预格式化文本等） */
code, kbd, pre, samp {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; /* 使用等宽字体 */
}

/* 小号文字 */
small {
  font-size: 0.875em;     /* 相对父级缩小为 87.5% */
}

/* 上标与下标基础定位 */
sub, sup {
  font-size: 0.75em;      /* 相对父级缩小为 75% */
  line-height: 0;         /* 不占行高，避免影响布局 */
  position: relative;     /* 相对自身定位，配合 bottom/top 偏移 */
  vertical-align: baseline;/* 默认基线对齐 */
}
sub { bottom: -0.25em; }  /* 下标：向下偏移 */
sup { top: -0.5em; }      /* 上标：向上偏移 */

/* 列表去除默认项目符号 */
ul, ol {
  list-style: none;       /* 去掉圆点/数字等列表标记 */
}

/* 链接样式重置 */
a {
  color: inherit;         /* 链接颜色继承父级 */
  text-decoration: none;  /* 去掉下划线 */
}

/* 媒体元素自适应与块级显示 */
img, picture, svg, video, canvas {
  display: block;         /* 块级显示，避免行内空隙 */
  max-width: 100%;        /* 最大不超过容器宽度，防止溢出 */
}

/* 表单控件统一继承字体与颜色 */
button, input, optgroup, select, textarea {
  font-family: inherit;   /* 字体继承父级 */
  font-size: 100%;        /* 字号保持与父级一致 */
  line-height: inherit;   /* 行高继承父级 */
  color: inherit;         /* 颜色继承父级 */
}

/* 按钮交互状态 */
button {
  cursor: pointer;        /* 鼠标悬停显示为手型 */
}

/* 多行文本框仅允许垂直拉伸 */
textarea {
  resize: vertical;       /* 限制只能上下调整大小 */
}

/* 表格边框合并（消除单元格间缝隙） */
table {
  border-collapse: collapse;
}

/* 去掉默认聚焦框（需要自己加focus样式） */
:focus {
  outline: none;          /* 移除浏览器默认聚焦轮廓 */
}

/* 禁止文本选中（可选，不需要就删掉） */
/* .no-select {
  user-select: none;
} */

```
