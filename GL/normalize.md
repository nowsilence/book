normalize 是 WebGL/OpenGL 顶点属性配置中的一个关键参数，用于控制整数类型的顶点数据在传递给着色器（shader）时是否进行归一化处理。当 normalize: true 时，整数会被映射到浮点数范围，具体映射规则取决于数据类型的符号性（有符号 / 无符号）和位数。
核心作用
当 normalize: true 时，整数类型的顶点数据会被转换为 [-1.0, 1.0] 或 [0.0, 1.0] 范围的浮点数，转换过程由 GPU 硬件自动完成，无性能损耗。若 normalize: false，整数会被直接作为整数传递（此时 shader 中需用整数类型变量接收，如 int 或 uint）。
不同数据类型的归一化规则
以下是 WebGL 中常见的整数类型（componentDatatype）在 normalize: true 时的映射规则：
1. 无符号整数类型（Unsigned）
类型：UNSIGNED_BYTE（8 位）、UNSIGNED_SHORT（16 位）
取值范围：[0, max]（max 为该类型的最大值，如 UNSIGNED_BYTE 的 max=255）
归一化结果：映射到 [0.0, 1.0] 浮点数范围，公式为：浮点数 = 整数 / max
示例：
UNSIGNED_BYTE：0 → 0.0，255 → 1.0，128 → 128/255 ≈ 0.50196
UNSIGNED_SHORT：0 → 0.0，65535 → 1.0，32768 → 32768/65535 ≈ 0.5000076

2. 有符号整数类型（Signed）
类型：BYTE（8 位）、SHORT（16 位）
取值范围：[min, max]（包含负数，如 BYTE 的范围是 -128 ~ 127）
归一化结果：映射到 [-1.0, 1.0] 浮点数范围，公式为：
浮点数 = 整数 / max_abs
其中 max_abs 是该类型能表示的最大绝对值（如 BYTE 的 max_abs=127，SHORT 的 max_abs=32767）。
示例：
BYTE：-128 → -128/127 ≈ -1.00787（接近 -1.0），0 → 0.0，127 → 1.0
SHORT：-32768 → -32768/32767 ≈ -1.00003，32767 → 1.0

3. 注意：浮点数类型不生效
如果 componentDatatype 是浮点数类型（如 FLOAT），normalize 参数会被忽略（因为浮点数本身无需归一化，直接传递原始值）。