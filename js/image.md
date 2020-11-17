ImageBitmap/ImageData

ImageBitmap GPU可以直接使用绘制
ImageData 存储的是像素二进制数据，是一组非预乘的RGBA颜色值，用于CPU，绘制前，经过alpha预乘后传入GPU。

如果是简单的绘制图像，那么使用ImageBitmap；如果需要操作像素，则使用ImageData

```
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
```