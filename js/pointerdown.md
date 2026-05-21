onpointerdown属性
该GlobalEventHandlers事件处理程序onpointerdown被用来指定pointerdown事件的事件处理程序，在初始按下指针设备时将触发该处理器。这个事件可以被发送到Window，Document和Element对象。
由于使用鼠标或鼠标兼容的设备而生成的用户活动，这在功能上等同于mousedown事件。如果pointerdown事件不是通过对preventDefault ()的调用而取消的，则大多数用户代理将触发一个mousedown事件，以便不使用指针事件的站点能够正常工作。


```javascript

document.addEventListener('pointerdown', e => {
  console.log('pointerdown')
  
  // e.preventDefault()       // 不阻止 mousedown
  e.stopImmediatePropagation() // 真正阻止 mousedown
})

document.addEventListener('mousedown', e => {
  console.log('mousedown') // 只有不加上面那行才会打印
})


// 事件触发顺序
// touchstart → pointerdown → mousedown → mouseup → pointerup → touchend

// 在 touchstart 里 preventDefault()，才会阻止浏览器派发模拟鼠标事件（mousedown/mousemove/mouseup）

// 浏览器的「触摸→模拟鼠标」是在 Touch 事件阶段决定的，Pointer 事件只是中间层，无权取消这套兼容逻辑，所以只有 touchstart.preventDefault() 能关掉模拟鼠标事件，pointerdown 不行。
```
