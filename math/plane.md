
** 射线与平面的交点 **

```
// 线的方向向量, 单位向量
var direction;
// 线上一点
var point;
// 面法向量 单位向量
var normal;
// 面常量
var constant;

var result;

var denominator = normal.dot( direction );

// 平行或共面
if ( denominator === 0 ) {

    // 点到面的距离
    var dis = normal.dot( point ) + constant;
    // 共面
    if ( dis === 0 ) {
        result = point;
    }

    // 平行
    result = undefined;
}

var t = - (point.dot(normal) + constant) / denominator;
/*
  t < 0 射线与平面没有交点
*/
if (t < 0) {

    result = undefined;

}

return target.copy( direction ).multiplyScalar( t ).add( line.start );
```

[参考](https://blog.csdn.net/csxiaoshui/article/details/78211866)