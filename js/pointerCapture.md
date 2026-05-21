elem.setPointerCapture(pointerId) – binds events with the given pointerId to elem. After the call all pointer events with the same pointerId will have elem as the target (as if happened on elem), no matter where in document they really happened.
In other words, elem.setPointerCapture(pointerId) retargets all subsequent events with the given pointerId to elem.

event.pointerId

会把所有的事件重定向到这个元素
解决问题例如：拖动元素移动，若拖动的快速则鼠标会离开元素，造成拖动中断，

[参考](https://javascript.info/pointer-events)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <title>setPointerCapture 解决快速拖拽断触</title>
  <style>
    body {
      margin: 0;
      height: 100vh;
      background: #f0f2f5;
    }
    #drag {
      width: 150px;
      height: 150px;
      background: #1677ff;
      border-radius: 8px;
      position: absolute;
      left: 100px;
      top: 100px;
      /* 禁止浏览器默认触摸行为、文字选中 */
      touch-action: none;
      user-select: none;
      cursor: grab;
    }
    #drag:active {
      cursor: grabbing;
    }
  </style>
</head>
<body>
  <div id="drag"></div>

  <script>
    const drag = document.getElementById("drag");
    let isDragging = false;
    let offsetX = 0, offsetY = 0;

    // 按下：捕获指针，关键！
    drag.addEventListener("pointerdown", (e) => {
      isDragging = true;
      // 强制捕获当前指针，鼠标移出div也能收到move事件
      drag.setPointerCapture(e.pointerId);

      // 计算鼠标相对于盒子内部的偏移
      offsetX = e.clientX - drag.offsetLeft;
      offsetY = e.clientY - drag.offsetTop;
    });

    // 移动：快速拖动、鼠标移出div依然有效
    drag.addEventListener("pointermove", (e) => {
      if (!isDragging) return;
      // 实时更新位置
      drag.style.left = `${e.clientX - offsetX}px`;
      drag.style.top = `${e.clientY - offsetY}px`;
    });

    // 松开鼠标
    drag.addEventListener("pointerup", (e) => {
      isDragging = false;
      // 抬起后浏览器会自动释放捕获，这里可手动释放（可选）
      drag.releasePointerCapture(e.pointerId);
    });

    // 异常中断（滚动、弹窗等）
    drag.addEventListener("pointercancel", (e) => {
      isDragging = false;
      drag.releasePointerCapture(e.pointerId);
    });
  </script>
</body>
</html>

```