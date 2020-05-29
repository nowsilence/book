** 将大小为0~1的两个浮点数，封装成一个整数 **

```
function compress(f0, f1) {
    const i0 = (f0 * 4095.0) | 0;
    const i1 = (f1 * 4095.0) | 0;
    return 4096.0 * i1 + i1;
}

```

** 将一个整数解压为两个0~1的浮点数 **

```
function decompress(encoded) {
    const temp = encoded / 4096.0;
    const xZeroTo4095 = Math.floor(temp);
    const stx = xZeroTo4095 / 4095.0;
    const sty = (encoded - xZeroTo4095 * 4096.0) / 4095.0;
    
    return [stx, sty];
}
```

** 将深度值(0~1)包装到rgba中, 主要用于shader 把深度值存储在纹理中 **

```
// shader代码
vec4 packDepth(float depth)
{
    // See Aras Pranckevičius' post Encoding Floats to RGBA
    // http://aras-p.info/blog/2009/07/30/encoding-floats-to-rgba-the-final/
    vec4 enc = vec4(1.0, 255.0, 65025.0, 16581375.0) * depth;
    enc = fract(enc);
    enc -= enc.yzww * vec4(1.0 / 255.0, 1.0 / 255.0, 1.0 / 255.0, 0.0);
    return enc;
}

float unpackDepth(vec4 packedDepth)
 {
    // See Aras Pranckevičius' post Encoding Floats to RGBA
    // http://aras-p.info/blog/2009/07/30/encoding-floats-to-rgba-the-final/
    return dot(packedDepth, vec4(1.0, 1.0 / 255.0, 1.0 / 65025.0, 1.0 / 16581375.0));
 }
```