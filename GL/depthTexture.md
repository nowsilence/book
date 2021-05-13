实例化WebGLRenderTarget,调用一次render:

let renderTarget = new WebGLRenderTarget(width, height, {
  depthTexture: new DepthTexture()
})
render.setRenderTarget(renderTarget)
renderer.render(scene, camera)
如此就生成了深度纹理， 可以将深度纹理赋给其他材质使用。

在shader中，采样深度纹理，有些特殊。
深度纹理以前好像需要转解码float类型到RGBA四个通道，现在似乎是不用了，系统
通常支持DepthFormat, 对应的ext为 webgl_depth_texture?
深度纹理的类型，在THREEJS中有两种：

DepthFormat(默认)
DepthStencilFormat
对于DepthFormat, 在shader中的采样方式（参考Unity的宏:SAMPLE_DEPTH_TEXTURE)：
uniform sampler2D depthTexture;
float depth = texture2D(depthTexture, uv).r;
这里的depth即是深度缓冲区的值，近截面深度值为0， 远截面深度值为1， 非线性，为了表现，
靠近近截面会占用更多的精度。

TODO 深度转换函数
Unity 中LinearEyeDepth 负责把深度纹理的采样结果转换到视角空间下的深度值，也 就是我们上面得到的Z(visw)。而 Linear01Depth 则会返回一个范围在[0, 1]的线性深度值
