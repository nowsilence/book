在WebGL2中，没有这个多采样纹理附件，在OPENGL才有，为什么提到这个多采样纹理附件，大部分时间，我们的离屏渲染都需要渲染到一个纹理对象上面，才能进一步使用。
在没有多采样纹理附件，只有多采样渲染缓冲对象的情况下，要实现MSAA，只能渲染到渲染缓冲对象上，但是渲染缓冲对象的内容不能直接传递给纹理对象。
那么应该怎么做呢？ 需要使用另外一个重要的函数：

gl.blitFramebuffer函数
通过gl.blitFramebuffer函数，可以把多采样渲染缓冲对象的内容传递给纹理对象。下面是该函数的签名：