# ImageBitmap/ImageData

ImageBitmap GPU可以直接使用绘制
ImageData 存储的是像素二进制数据，是一组非预乘的RGBA颜色值，用于CPU，绘制前，经过alpha预乘后传入GPU。

如果是简单的绘制图像，那么使用ImageBitmap；如果需要操作像素，则使用ImageData

```javascript
const image = new Image();

image.onload = function(img) {
    createImageBitmap(this, 0, 0, 32, 32).then(imageBitmap => {
        console.log(imageBitmap);
    })
}

image.src = './resource/texture/kerb/WPS0000001.jpg';


Render.Ajax.get('./resource/texture/kerb/WPS0000001.jpg', {
    responseType: 'blob',
    // timeout: 10000,
    success: function (response) {
        createImageBitmap(response).then(imageBitmap => {
        console.log(imageBitmap);
    })
    }
});

// 图片跨域问题, 参考[https://juejin.cn/post/6844903795726483463]

```

向服务器请求图片,使用ajax请求失败报403, 可能是服务限制了请求的Accept 头包含 image/*。
可以尝试设置accept

```javascript
xhr.setRequestHeader('Accept', 'image/webp,image/*,*/*;q=0.8');

```

图像的三种对象：

## Image: <img> 元素本质上就是HTMLImageElement对象，HTMLImageElement对象继承自Image的接口，二者行为一致
```javascript
// 获取页面上的图片元素
const imgElement = document.querySelector('#my-image');

// 等待图片加载完成（重要！）
if (imgElement.complete) {
    // 已经加载完成，直接创建
    const bitmap = await createImageBitmap(imgElement);
    ctx.drawImage(bitmap, 0, 0);
    bitmap.close();
} else {
    // 还没加载完，监听 load 事件
    imgElement.addEventListener('load', async () => {
        ctx.drawImage(imgElement, 0, 0);
    });
}

// 创建一个Image对象
const img = new Image();
// 监听加载完成事件
img.onload = () => {
    console.log('图片加载成功');
    // 将图片绘制到canvas上，会在主线程上自动解码
    ctx.drawImage(img, 0, 0);
};
// 监听加载失败事件
img.onerror = (err) => {
    console.error('图片加载失败', err);
};
// 开始加载图片
img.src = 'https://example.com/my-image.jpg';
```

## ImageData: 代表了Canvas区域背后那一块原始的像素数据, data属性为Uint8ClampedArray（类型化数组），按顺序存储每个像素的红(R)、绿(G)、蓝(B)、透明通道(A) 值，每个值的范围是0-255

```javascript
// 获取canvas上 (0,0) 到 (100,100) 区域的像素数据
const imageData = ctx.getImageData(0, 0, 100, 100);
const data = imageData.data; // 获取像素数组

// 一个将图片变为灰度的简单例子
for (let i = 0; i < data.length; i += 4) {
    const avg = (data[i] + data[i+1] + data[i+2]) / 3;
    data[i] = avg;     // 红通道
    data[i+1] = avg;   // 绿通道
    data[i+2] = avg;   // 蓝通道
}

// 将处理后的数据画回canvas
ctx.putImageData(imageData, 0, 0);
```
## ImageBitmap
解码后并存储在GPU（或内存中）的位图图像，一般刚解码后存放在内存，第一次使用会上层GPU，放到显存，具体要看厂商优化
```javascript
// 高性能方式：直接从网络获取并解码
fetch('https://example.com/large-image.jpg')
    .then(response => response.blob())   // 获取文件二进制数据
    .then(blob => createImageBitmap(blob)) // 创建位图（解码过程不阻塞主线程）
    .then(bitmap => {
        // 直接绘制，非常快
        ctx.drawImage(bitmap, 0, 0);
        // 使用完后可以释放内存
        bitmap.close();
    });
```