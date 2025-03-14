[webgl文档](https://www.khronos.org/registry/webgl/specs/latest/1.0/)

※如果纹理边缘地方有边线问题，考虑下把minFilter设置为LinearFilter试试

THREE.RGBFormat is slow. Not all devices natively support RGB texture formats which requires an emulation in software. 
Several resources in the WebGL space recommend to always use RGBA.
all devices using Metal support no 3 channel formats（RGB8）.

纹理： 
internalformat
    A GLenum specifying the color components in the texture.
    每个纹理单元存储多少颜色成分，并在可能的情况下说明这些成分的存储大小，以及是否希望对纹理进行压缩
format
    A GLenum specifying the format of the texel data. 
    In WebGL 1, this must be the same as internalformat (see above). in WebGL 2, the combinations are listed in this table(https://registry.khronos.org/webgl/specs/latest/2.0/#TEXTURE_TYPES_FORMATS_FROM_DOM_ELEMENTS_TABLE)
    指向数据元素的颜色布局

type 告诉webgl使用缓存区中的什么数据类型来存储颜色分量

多个internalformat对应的fommat可能相同，即布局相同成分的存储大小不同

WebGL 在执行draw命令时需要依赖当前的渲染状态，如顶点缓冲区绑定、着色器程序激活、纹理绑定等。如果draw命令不是串行执行，可能会导致渲染状态在不同命令之间发生混乱，从而产生错误的渲染结果。为了保证渲染状态的一致性和正确性，WebGL 会按照顺序依次执行draw命令，在每个命令执行前确保渲染状态已经正确设置。
不过，虽然draw命令本身是串行执行的，但现代 GPU 具有高度并行性，在执行单个draw命令时，GPU 会并行处理图形数据的各个部分，如顶点处理、光栅化、片段处理等阶段，以提高渲染效率。
