/* 获取来的TextMetrics对象 */
TextMetrics = {
    width: 123.7060546875, // 考虑当前文本的字的尺寸，字体之后的文本宽度,一般最常用的就只有这个width了。
    actualBoundingBoxLeft: -2, // 可能为负数 给出从 CanvasRenderingContext2D.textAlign 属性给定的对齐点到给定文本的边界矩形左侧的距离。该距离是平行于基线测量的。
    actualBoundingBoxRight: 118.96484375, // 属性给出的对齐点到给定文本边界矩形右侧的距离。该距离是平行于基线测量的。
    actualBoundingBoxAscent: 31, // 表示从 CanvasRenderingContext2D.textBaseline 属性指示的水平线到用于渲染文本的所需要的最高边界矩形的顶部的距离。
    actualBoundingBoxDescent: 10 , // 表示从 CanvasRenderingContext2D.textBaseline 属性指示的水平线到用于渲染文本的所需要的边界矩形的底部的距离。
}
比如字符p，

真实高度 = actualBoundingBoxAscent + actualBoundingBoxDescent
这是目前Canvas里最接近 “文字真实视觉高度”的值。
1：只包含当前文本实际字形，不含字体预留空白
   有些字体本身会在字形上下预留额外安全留白，actualBoundingBox 只裁到有像素的地方，裁掉了字体预留空边
2、不包含 CSS/Canvas 的 lineHeight 行间距
Canvas 绘制多行文字时，行高是独立设置的，
ascent + descent 只是字形本身高度，不包含行与行之间的间距。