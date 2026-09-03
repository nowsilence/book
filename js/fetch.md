
```js
async function downloadToIndexedDB(url, db) {
    // resp为 Response对象
    // resp.body // ReadableStream | null
    // 只要不去调用 `.blob()` / `.arrayBuffer()` / `.json()` / `.text()`，**整个响应体不会读进内存**。
    // 一旦调用任意一个，流就被消耗掉，只能调用一次！
    const resp = await fetch(url);
    // 流读取，不一次性全部入内存
    const reader = resp.body.getReader();
    while(true) {
        const {done, value} = await reader.read(); // value 是Uint8Array小块，不是完整文件
        if(done) break;
        // 把小块Uint8Array直接写入IndexedDB，不拼接全部
        await db.put("chunks", { data: value });
    }
}

```


1. FileSystem Access API 只支持 Chromium（Chrome/Edge），Safari 写能力残缺，移动端大多不支持。
```js
/**
 * 流式下载，边下载边写入本地磁盘，不加载全部到内存
 * @param {string} url 下载地址
 * @param {FileSystemFileHandle} fileHandle 已经授权的本地文件句柄
 */
async function streamDownloadToDisk(url, fileHandle) {
  const resp = await fetch(url);
  if (!resp.body) throw new Error("浏览器不支持ReadableStream");

  // 创建可写文件流，直接指向本地文件
  const writable = await fileHandle.createWritable();
  // 响应流直接管道输出到本地文件，数据一块一块落盘，内存只存小块chunk
  await resp.body.pipeTo(writable);
  console.log("下载完成，数据已经落盘，此时内存没有完整文件");
}

// 使用示例
async function demo() {
  // 弹出保存对话框，让用户选择保存位置，得到文件句柄
  const fileHandle = await window.showSaveFilePicker({
    suggestedName: "bigfile.zip"
  });
  
  await streamDownloadToDisk("/api/bigfile", fileHandle);

  // ----过一段时间之后，再读取这个本地文件，不需要一直放在内存----
  const file = await fileHandle.getFile();
  const reader = new FileReader();
  reader.readAsArrayBuffer(file);
}
```



OPFS 优点：

1. **零弹窗，不需要用户点击选择保存位置**
2. 支持 ReadableStream `pipeTo`，**流式边下边落盘，不把完整文件放内存**
3. 页面刷新仍然保留文件，浏览器重启也还在
4. 支持 Web Worker，性能好，大文件友好

OPFS 缺点：

1. **普通文件管理器看不到这个文件**，是浏览器沙盒私有存储；用户不能直接打开这个 zip。只能 JS 代码内部读取。
2. 有存储配额，存储空间不足浏览器会清理；清除站点数据文件直接消失。
3. 如果最终要让用户拿到这个文件到电脑文件夹：后续需要再把 OPFS 里的文件导出（触发一次 a 标签下载或者调用一次`showSaveFilePicker`导出到真实磁盘）。

```js

// OPFS：浏览器沙盒内部磁盘，完全不弹窗，不需要用户选择
// 文件存在硬盘，但用户的资源管理器看不到；属于该网站私有存储，受浏览器存储配额管控，清除网站数据就会删掉
const rootDir = await navigator.storage.getDirectory();
// 创建/打开沙盒内文件，不需要任何弹窗
const fileHandle = await rootDir.getFileHandle("bigfile.zip", {create:true});

// 直接流式fetch pipe写入，不加载全部进内存
const resp = await fetch(url);
const writable = await fileHandle.createWritable();
await resp.body.pipeTo(writable);

// 隔一段时间之后读取磁盘（沙盒里的文件）
const file = await fileHandle.getFile();
```