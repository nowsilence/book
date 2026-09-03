在ES6中，全局对象的属性和全局变量脱钩，但是为了保持兼容性，旧的不变，所以var、function声明的全局变量依然可以在window对象上看到，而let、const声明的全局变量在window对象上看不到
```js
import.meta
// 是 ES 模块的标准语法——每个模块都能拿到一个 import.meta 对象，里面是关于这个模块自身的元信息
// 最常用的是 import.meta.url（当前模块的 URL 路径）
```

Nuxt/Vite 在这个对象上额外注入了一些布尔标志：

标志	            含义
import.meta.client	当前代码在「客户端构建产物」里 = true
import.meta.server	在「服务端构建产物」里 = true
import.meta.dev	dev 模式 = true
import.meta.prod	生产构建 = true

它是「编译期替换」，不是运行时读取