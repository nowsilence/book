** 格林公式求多边形面积 **

```
function polygonArray(points) {
    points.push(points[0]);
    let s = 0;
    for (let i = 0; i < points.length - 1; i++) {
        s += (points[i][0] + points[i + 1][0]) * (points[i + 1][1] - points[i][1]);   
    }
    return 0.5 * Math.abs(s);
}
```