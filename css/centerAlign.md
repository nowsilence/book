## box-sizing ##
```css
box-sizing: border-box; // content-box（默认值）
```
当使用 box-sizing: border-box; 时，元素的总宽度和总高度包括了元素的 border（边框）和 padding（内边距），而不是仅仅包括 content（内容）区域。这意味着即使加上了边框和内边距，元素的总宽度和总高度也不会改变。

## content居中显示 ##
```html
<div class="container">
    <div class="content"> </div>
</div>
```
```css
.container{
    flex-direction: column;
    height: 100%;
    display: flex;
}

.content {
    width: 100%;
    max-width: 800px;
    box-sizing: border-box;
    flex-grow: 1;
    margin: auto; // 居中的关键
}
```