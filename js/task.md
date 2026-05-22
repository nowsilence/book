# 微任务、宏任务、事件循环

## 微任务

* Promise 回调函数
* async/await await后续代码，本质上会封装为微任务回调
* queueMicrotask(callback) 传入的回调函数
* MutationObserver 监听触发的回调

被async修饰的函数会返回一个Promise，若不主动返回，会默认封装一个Promise。
await 后面的函数fn必须返回一个Promise，若没有明确返回，fn需要async修饰

MutationObserver 监听DOM发生修改时，自动触发回调，元素属性、文本、子节点变化

```js
// 1. 创建观察器
const observer = new MutationObserver(callback)

// 2. 指定监听谁、监听哪些变化
observer.observe(目标DOM, 配置项)

// 3. 停止监听
observer.disconnect()
// 常用配置
// {
//   childList: true,    // 子节点增删
//   attributes: true,  // 属性修改
//   characterData: true,// 文本内容修改
//   subtree: true      // 监听后代所有节点
// }
```

## 宏任务

* setTimeout / setInterval
* setImmediate（node）
* Ajax 请求
* DOM 渲染事件
* I/O 读写

## 事件循环

1、执行完所有主线程同步代码
2、彻底清空当前所有微任务（包含执行中新增的微任务）
3、**取出队列头部 1 个宏任务执行** ***重点是只取出一个，即使有很多个***
4、本轮结束，开启下一轮循环，重复 1→2→3

执行一个node脚本有没有事件循环？有的。
当一个脚本执行到代码尾部，如果这个时候还有异步任务没执行完，程序就不会退出，它会一直等着异步任务，等所有任务都清空了程序才会结束，

process.nextTick执行时机比微任务要早：
同步代码 → nextTick → 微任务 → 事件循环（宏任务）
同步代码执行完 → 立刻执行的插队任务，假如正在执行清空微任务的时候插入了一个nextTick，那么立刻暂停微任务，去清空nextTick队列，然后再执行剩下的微任务
