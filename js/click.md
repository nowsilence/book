#在mousemove之后不想触发click事件#

```
// Suppress the next click, but only if it's immediate.
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