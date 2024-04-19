```javascript
最新版已经移除THREE.RGB格式
如果想设置RGB代码如下：

texture.format = 'RGB';
texture.internalFormat = 'RGB8';

class RenderPass extends THREE.Pass {
        /*
            writeBuffer 如果renderToScreen为false，渲染一般要渲染到这个buffer里，
            readBuffer 当前pass一般会使用readBuffer的纹理，一般是上个pass处理的结果存到这里面，如果上个pass的处理结果已经写入到了writeBuffer，一般需要sapeBuffer
        */
		render( renderer, writeBuffer, readBuffer /*, deltaTime, maskActive */ ) {
```