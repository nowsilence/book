当你通过 16进制 或 CSS 字符串（如 "red"）设置 THREE.Color 时，Three.js 会默认认为这些颜色值处于 sRGB 颜色空间（即经过伽马校正的非线性空间）。

但：THREE.Color 对象内部存储的是 线性化的 sRGB 值（即自动转换到 LinearSRGBColorSpace）。

javascript
const color = new THREE.Color(0xff0000); // 红色（sRGB 空间的输入）
console.log(color.r, color.g, color.b); // 输出的是线性化后的 RGB 值（约 0.2126, 0, 0）
自动转换：Three.js 在构造 Color 对象时，会自动将 sRGB 输入值转换为线性值（通过近似 RGB^2.2 的反伽马操作）。

setHSL/setRGB只有这两个方法，如果不传颜色空间，默认设置的颜色是线性空间的，
setHex/setStyle 会认为设置的是srgb空间的，内部会自动转换为线性空间，
three.js默认的shader会讲线性空间再转回srgb空间，线性空间颜色主要用于计算