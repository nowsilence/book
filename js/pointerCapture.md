elem.setPointerCapture(pointerId) – binds events with the given pointerId to elem. After the call all pointer events with the same pointerId will have elem as the target (as if happened on elem), no matter where in document they really happened.
In other words, elem.setPointerCapture(pointerId) retargets all subsequent events with the given pointerId to elem.

会把所有的事件重定向到这个元素
解决问题例如：拖动元素移动，若拖动的快速则鼠标会离开元素，造成拖动中断，

[参考](https://javascript.info/pointer-events)