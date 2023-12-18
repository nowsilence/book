stencilFunc（Glenum func ,GLint ref ,GLuint mask） :用来控制stencil的测试方式，得出测试结果
第一个参数指定模板测试比较函数(gl.NEVER 总是不通过)
第二个参数 用来做模板测试的参考值
第三个参数 指定操作掩码（采用16进制或8进制），在测试时将ref mask 进行与运算，再将mask与模板缓冲中的值进行与运算，最后根据比较函数得出结果


stencilWrite: 是否写入模板缓冲，默认 false
stencilWriteMask: 模板写入的掩码，默认为 0xff
stencilFunc: 模板比较使用的函数，默认是 AlwaysStencilFunc。stencilRef & stencilFuncMask 的值与缓冲区已存在的模板值按照stencilFunc比较，如果符合函数关系，则返回 true，片元会通过渲染流水线；否则，返回false，渲染流水线会中断，不会再往下执行，深度和颜色不会被写入深度缓冲及颜色缓冲
stencilRef: 模板参考值
stencilFuncMask: 模板测试的掩码，默认 0xff
stencilFail: 模板测试的话，如何操作
stencilZFail: 模板测试通过，深度测试不通过的操作
stencilZPass: 模板测试和深度测试都通过的操作