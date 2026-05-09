#在mousemove之后不想触发click事件#

```javascript
// Suppress the next click, but only if it's immediate.
/**
 * e.preventDefault()阻止元素默认行为
 * 表单不会自动提交
 * 点击<a>不会跳转
 * [ˌprɒpə'ɡeɪʃ(ə)n]
 * e.stopPropagation(); 默认是在冒泡阶段阻止子元素向父元素冒泡，如果在捕获阶段，会阻止事件传递到子元素
 * 总之，不能里把stopPropagation理解为阻止冒泡，而是阻止其在相应事件阶段传播
 * 事件传播三阶段
 * 捕获阶段 (Capture Phase)：从 window → 父元素 → 子元素（向下）
 * 目标阶段 (Target Phase)：到达触发事件的元素
 * 冒泡阶段 (Bubbling Phase)：从子元素 → 父元素 → window（向上）
 * 
 * el.addEventListener('click', e => {
 *  // 默认情况下，事件监听器注册在冒泡阶段，所以执行顺序是：子元素先执行 → 然后是父元素 → 最后是祖先元素
 *
 * });
 * el.addEventListener('click', e => {
 *  // 在捕获阶段监听事件(第二个参数为true)
 *  
 * }, true);
 * 
 * e.currentTarget 绑定的对象：el
 * e.target 实际触发的对象，如在父元素上绑定监听，点击子元素，e.target为子元素，e.currentTarget为父元素
 */
const _suppressClick = (e) => {
    e.preventDefault(); 
    e.stopPropagation();
    window.removeEventListener('click', _suppressClick, true);
};

const suppressClick = () => {
    window.addEventListener('click', _suppressClick, true);
    window.setTimeout(() => {
        window.removeEventListener('click', _suppressClick, true);
    }, 0);
};
```