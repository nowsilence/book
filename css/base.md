```css

overflow-y: auto; /* 内容超出才显示滚动条 */

will-change: transform; /* 把这个元素放到独立图层, 交给 GPU 显卡 加速渲染, 滚动 / 动画时 超级丝滑，图层是要占 显存 + 内存 的，故添加的多了反而卡*/

box-sizing: content-box; // 默认 最终的宽度= width + 2 * padding + 2 * border
box-sizing: border-box； // 最终的宽度= width;

/* 只对 img、video、svg 有效 */
object-fit: fill; /*  默认值 拉伸填满盒子 */
object-fit: contain; /*  等比例缩放 可能会有留白 */
object-fit: cover; /*  等比例缩放 超出部分自动裁剪（居中裁剪） */
object-fit: none; /* 不缩放，原图大小, 超出盒子直接隐藏 */
object-position: center; /* 默认：居中裁剪 */
object-position: top;    /* 顶部对齐 */
object-position: left top;/* 左上角 */

display: flex;
flex-direction: row;        /* 默认 → 横向 */
flex-direction: column;     /* 纵向 */
align-items: stretch; /* 默认 子元素，如果没有设置高度，会自动拉伸，和父元素一样高！若要保持子元素高度：设置align-items: center; 或 子元素设置height值； 或子元素设置 align-self: center;*/
align-items: center; /* 交叉轴（垂直于主轴的方向）对齐方式，垂直居中， */
justify-content: center;        /* 主轴对齐对齐方式，flex-direction指向的轴，水平居中 */
justify-content: space-between; /* 两端对齐 */
justify-content: space-around;  /* 环绕间距 */
gap: 12px; /* 子元素之间自动加间距，超级好用 */

```