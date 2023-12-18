/* ① 创建绑定组的布局对象 */
const bindGroupLayout = device.createBindGroupLayout({
  entries: [
    {
      /* use for sampler */
      binding: 0,
      visibility: GPUShaderStage.VERTEX | GPUShaderStage.FRAGMENT,,
      sampler: {
        type: 'filtering',
      },
    },
    {
      /* use for texture view */
      binding: 1,
      visibility: GPUShaderStage.FRAGMENT,
      texture: {
        sampleType: 'float'
      }
    },
    {
        binding: GPUIndex32
        visibility: GPUShaderStage { VERTEX, FRAGMENT, COMPUTE }
        buffer: GPUBufferBindingLayout {
            type: GPUBufferBindingType-> { 'uniform', 'storage', 'read-only-storage' }, default: 'uniform'
            hasDynamicOffset: boolean -> 默认false
            GPUSize64 minBindSize: 0
        } 
    },
    {
        binding: GPUIndex32
        sampler: GPUSamplerBindingLayout -> { type: -> GPUSamplerBindingType { 'filering', 'non-filtering', 'comparison}}
    },
    {
        binding: GPUIndex32, // 对应GPUTextureView
        texutre: GPUTextureBindingLayout {
            sampleType: GPUTextureSamppleType { 'float', 'unfilterable-float', 'depth', 'sint', 'uint' },
            viewDimension: GUPTextureViewDimension { '1d', '2d', '2d-array', 'cube', 'cube-array', '3d' }
            multisample: boolean false
        }
    },
    {
        binding: GPUIndex32, // 对应GPUTextureView
        storageTexture: GPUStorageTextureBindingLayeout -> { access: GPUStorageTextureAccess { 'write-only'}, format: GPUTextureFormat {'r8unorm', 'r8uint'……}, viewDimension: GUPTextureViewDimension }
    },
    {
        binding: GPUIndex32,
        externalTexture:  GPUExternalTextureBindingLayout 
    }
  ]
})
/* ② 创建 Pipeline 的布局对象 */
const pipelineLayout = device.createPipelineLayout({
  bindGroupLayouts: [bindGroupLayout],
})

/* ③ 创建 pipeline 时，传递 Pipeline 的布局对象 */
const pipeline = device.createRenderPipeline({
  layout: pipelineLayou, // <- 传递布局对象
  <!-- layout: auto, // 若使用auto，则不需要步骤①②，程序会从shader里提取，使用auto的话，如果着色器中有uniform变量确没使用，在createGroup里不能配置，否则报错 -->
    vertex: {
        module: shaderModule,
        entryPoint: 'vertexMain'，
        buffers: [
           {
                arrayStride: 8,
                attributes: [
                    {
                        format: 'float32',
                        offset:0,
                        shaderLocation: 0,
                    },
                    {
                        format: 'float32',
                        offset:4,
                        shaderLocation: 1,
                    }
                ]
           },
           {
                arrayStride: 16,
                attributes: [
                    {
                        format: 'float32x2',
                        offset:0,
                        shaderLocation: 2,
                    }, 
                    {
                        format: 'float32',
                        offset:8,
                        shaderLocation: 3,
                    }
                ]
           }
        ]
    },
    fragment: {
        module: shaderModule,
        entryPoint: 'fragmentMain',
        targets: [{
            format: 'bgra8unorm',
        }],
    },
    depthStencil:
    primitive: {
      topology: 'triangle-list',
    },
    multisample = {};
  // ... 其他
})

/* ④ 创建绑定组：GPUBindGroup，一组资源 */
const uniformBindGroup = device.createBindGroup({
  layout: pipeline.getBindGroupLayout(0), // <- 指定绑定组的布局对象
  entries: [
    {
      binding: 0,
      resource: sampler, // <- 传入采样器对象
    },
    {
      binding: 1,
      resource: texture.createView() // <- 传入纹理对象的视图
    }, {
        binding: GPUIndex32,
        resource: GPUBindingResource (
            GPUSampler,
            GPUTextureView,
            GPUExternalTexture,
            GPUBufferBinding->{
                GPUBuffer buffer,
                GPUSize 64 offset, 
                GPUSize size // must be a multiple of 4 bytes.
                }
        )
    }
  ]
})


A GPUCommandBuffer containing the commands recorded by the GPUCommandEncoder can be created by calling finish(). Once finish() has been called the command encoder can no longer be used.

submit(commandBuffers)
Schedules the execution of the command buffers by the GPU on this queue.

Submitted command buffers cannot be used again.

texture/storageTexture对应的资源类型都是GPUTextureView

texture对应的wgsl类型为：
texture_1d<T>
texture_2d<T>
texture_2d_array<T>
texture_3d<T>
texture_cube<T>
texture_cube_array<T>

若sampleType为'deepth',则对应的类型为：
texture_depth_2d
texture_depth_2d_array
texture_depth_cube	Cube
texture_depth_cube_array

若multisample为true，则对应的wgsl类型为：

texture_multisampled_2d<T>
texture_depth_multisampled_2d

storageTexture对应的wgsl类型为：
texture_storage_1d<Format, Access>
texture_storage_2d<Format, Access>
texture_storage_2d_array<Format, Access>
texture_storage_3d<Format, Access>

externalTexture对应的wgsl数据类型为texture_external



buffer: enum GPUBufferBindingType {
    "uniform",
    "storage", // 值为数组的情况下使用，即值长度不固定的时候
    "read-only-storage",
};
var<uniform> | var<storage>


Address space	Sharing among invocations	Default access mode	Notes
function	Same invocation only	read_write	
private	Same invocation only	read_write	
workgroup	Invocations in the same compute shader workgroup	read_write	The element count of an outermost array may be a pipeline-overridable constant.
uniform	Invocations in the same shader stage	read	For uniform buffer variables
storage	Invocations in the same shader stage	read	For storage buffer variables
handle	Invocations in the same shader stage	read	For sampler and texture variables.
WGSL predeclares an enumerant for each address space, except for the handle address space.

Variables in the workgroup address space must only be statically accessed in a compute shader stage.

Variables in the storage address space (storage buffers) can only be statically accessed by a vertex shader stage if the access mode is read. Variables whose store type is a storage texture cannot be statically accessed by a vertex shader stage. See WebGPU createBindGroupLayout().

NOTE: Each address space may have different performance characteristics.

When writing a variable declaration or a pointer type in WGSL source:

For the storage address space, the access mode is optional, and defaults to read.

For other address spaces, the access mode must not be written.

For each GPUBindGroupLayoutEntry entry in descriptor.entries:

Exactly one of entry.buffer, entry.sampler, entry.texture, and entry.storageTexture is provided.

entry.visibility contains only bits defined in GPUShaderStage.

If entry.visibility includes VERTEX:
entry.buffer?.type must not be "storage". Note that "read-only-storage" is allowed.

entry.storageTexture?.access must not be "write-only".

If entry.texture?.multisampled is true:

entry.texture.viewDimension is "2d".

entry.texture.sampleType is not "float".

If entry.storageTexture is provided:

entry.storageTexture.viewDimension is not "cube" or "cube-array".

entry.storageTexture.format must be a format which can support storage usage.

storage buffer的内存布局和uniform一样，struct的动态数组必须放到最后

bindLayout中设置的资源在wgsl中必须有对应的设置。
wgsl定的资源，bindLayout可不提供但是不可访问

swap chain是一个缓冲结构，webgpu会先将内容渲染到swap chain的buffer中，然后再将其显示到屏幕上；
swap chain本质上是等待呈现在屏幕上的一个图片队列。