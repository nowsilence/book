```javascript
const func = (x, y, width, height, zmin = 0, zmax = 1) => {
    const hwidth = width * 0.5;
    const hheight = height * 0.5;
    const hdepth = (zmax - zmin) * 0.5;

    const mat = new THREE.Matrix4();
    // 左上角为原点使用hheight，左下角为原点使用-hheight
    mat.set(
        hwidth, 0, 0, x + hwidth,
        0, -hheight, 0, y + hheight,
        0, 0, hdepth, zmin + hdepth,
        0, 0, 0, 1
    );
    // set设置的时候是按行设置的，比如前4个是第一行，接下来4个是二行
    // mat里面存储的elements，是按列存储的，比如前4个是第一列，接下来是第二列

    return mat;
}
```