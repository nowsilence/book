# 异常处理返回值优先级
* finally 始终执行：无论 try 里正常 return、还是 catch 捕获异常，finally 都会在返回结果前执行。
* finally 有 return → 最终返回 finally 的值：直接覆盖 try/catch 的返回值。
* finally 无 return → 最终返回 try/catch 的值：finally 只执行代码，不修改返回值。
* finally 里修改变量，不影响已确定的返回值（JS 会先缓存返回值，再执行 finally）。
总之，finally返回值的优先级最高，最好是不要在finally添加返回值

## 只有 try + finally（无异常）
```javascript
function test() {
  try {
    console.log('执行 try');
    return 10; // 第一步：缓存返回值 10
  } finally {
    console.log('执行 finally');
    // 无 return
  }
}
console.log(test()); 
// 执行顺序：try → finally → 返回 10
// 最终输出：10
```
## 只有 try + finally（无异常）
```javascript
function test() {
  try {
    return 10; // 缓存 10，但会被覆盖
  } finally {
    return 20; // finally 优先级最高
  }
}
console.log(test()); // 输出：20

```
## catch 触发 + finally 无 return
```javascript

function test() {
  try {
    throw new Error('出错了'); // 抛出异常
    return 10; // 不会执行
  } catch (e) {
    console.log('执行 catch');
    return 50; // 缓存返回值 50
  } finally {
    console.log('执行 finally');
  }
}
console.log(test()); 
// 执行顺序：catch → finally → 返回 50
// 输出：50
```

## catch 触发 + finally 有 return

```javascript
function test() {
  try {
    throw new Error();
    return 10;
  } catch {
    return 50; // 缓存 50
  } finally {
    return 100; // 覆盖
  }
}
console.log(test()); // 输出：100
```