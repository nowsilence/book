stencilMask(mask)
设置模板缓冲区的写入掩码 如：0xFF（默认允许写入所有位）0xF（允许写入低四位）
stencilMaskSeparate(face, mask)
参数face：
gl.FRONT
gl.BACK
gl.FRONT_AND_BACK

stencilFunc（Glenum func ,GLint ref ,GLuint mask） :用来控制stencil的测试方式，得出测试结果
第一个参数func 指定模板测试比较函数(gl.NEVER 总是不通过)
func 用来指定参考值与模板缓冲区的比较方式，可以有以下值：
gl.NEVER
gl.LESS
gl.EQUAL
gl.LEQUAL
gl.GREATER
gl.NOTEQUAL
gl.GEQUAL
gl.ALWAYS

第二个参数ref 用来和模板缓冲区进行对比的参考值，取值范围是0-2^n - 1,n为模板缓冲区位深度，可以通过gl.getParameter(gl.STENCIL_BITS)查询
第三个参数mask 指定操作掩码（采用16进制或8进制），在测试时将ref mask 进行与运算，再将mask与模板缓冲中的值进行与运算，最后根据比较函数得出结果
             位掩码值，用来指定参考值与模板缓冲区中的值在比较的时候使用哪些位。它是一个16进制的数，其取值范围是 0x00 - 0xFF,换算为二进制正好为 00000000 - 11111111。假设我们设置掩码值为0x0F,其二进制为00001111，也就是说参考值与模板缓冲区比较的时候，将参考值与目标值都转化为二进制，只有后四位参与比较，前四位忽略。
stencilFuncSeparate(face, func, ref, mask)
参数face：
gl.FRONT
gl.BACK
gl.FRONT_AND_BACK
其他参数同stencilFunc

stencilOp(fail, zfail, zpass)
stencilFunc通过或者失败以后，如何操作模板缓存区，同样接收3个参数：

fail 当模板测试失败的时候执行的操作
zfail 当深度测试失败的时候执行的操作
zpass 当模板测试和深度测试都成功的时候执行的操作
这三个参数的取值都一样，如下：

gl.KEEP -Keeps the current value.
gl.ZERO -Sets the stencil buffer value to 0.
gl.REPLACE -Sets the stencil buffer value to the reference value as specified by WebGLRenderingContext.stencilFunc().
gl.INCR -ncrements the current stencil buffer value. Clamps to the maximum representable unsigned value.
gl.INCR_WRAP -Increments the current stencil buffer value. Wraps stencil buffer value to zero when incrementing the maximum representable unsigned value.
gl.DECR -Decrements the current stencil buffer value. Clamps to 0.
gl.DECR_WRAP 
gl.INVERT Inverts the current stencil buffer value bitwise.

stencilOpSeparate(face, fail, zfail, zpass)
参数face：
gl.FRONT
gl.BACK
gl.FRONT_AND_BACK
其他参数同stencilOp

stencilWrite: 是否写入模板缓冲，默认 false
stencilWriteMask: 模板写入的掩码，默认为 0xff
stencilFunc: 模板比较使用的函数，默认是 AlwaysStencilFunc。stencilRef & stencilFuncMask 的值与缓冲区已存在的模板值按照stencilFunc比较，如果符合函数关系，则返回 true，片元会通过渲染流水线；否则，返回false，渲染流水线会中断，不会再往下执行，深度和颜色不会被写入深度缓冲及颜色缓冲
stencilRef: 模板参考值
stencilFuncMask: 模板测试的掩码，默认 0xff
stencilFail: 模板测试的话，如何操作
stencilZFail: 模板测试通过，深度测试不通过的操作
stencilZPass: 模板测试和深度测试都通过的操作

先进行模板测试，再进行深度测试，个人理解是先进行模板测试，再进行深度测试，然后更新模板缓冲区值，因为stencilOp要根据深度测试结果来更新模板缓冲区

片段着色器处理完一个片段之后，模板测试开始执行，它是根据模板缓冲来进行的。通过比较像素的模板值与模板缓冲中的值，根据设置的比较函数和掩码等，决定是否通过测试，若不通过测试则直接丢弃该片段，不会进入后续的深度测试和渲染流程。

在模板测试通过之后，保留的片段才会进入深度测试。深度测试会比较当前像素的深度值与深度缓冲中存储的值，以确定是否应该进行渲染，如果启用深度测试，而且当前像素在深度上小于深度缓冲中的值，那么该像素将被渲染，否则被丢弃。