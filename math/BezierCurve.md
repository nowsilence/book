## 贝塞尔曲线函数，以及绘制曲线一部分算法

** 二次贝塞尔曲线函数 **
```
/**
 * 二次贝塞尔曲线方程
 * @param  p0 起点
 * @param  p1 曲度点
 * @param  p2 终点
 * @param  {number} 绘制进度(0-1)
 */
function quadraticBezier(p0, p1, p2, t) {
    const k = 1 - t;
    return k * k * p0 + 2 * (1 - t) * t * p1 + t * t * p2; 
}

/*
    绘制曲线一部分方法

    0 < t0 < t1，时间
    p00, p11, p22 新的起点，控制点，终点
*/

const p00 = quadraticBezier(p0, p1, p2, t0);
const p22 = quadraticBezier(p0, p1, p2, t1); 

var u0 = 1 - t0;
var u1 = 1 - t1;

const p11 = u0 * u1 * p0 + (u1 * t0 + u0 * t1) * p1 + t0 * t1 * p2;
```

** 三次贝赛尔曲线 **

```

function quadraticBezier(p1, p2, p3, p4, t) {
    cont k = 1 - t;
    return k * k * k * p1 + 3 * k * k * t * p2 + 3 * k * t * t * p3 + t * * t * t * p4;
}

## 绘制一部分算法

0 < t0 < t1 < 1

u0 = (1 − t0)
u1 = (1 − t1))

const p11 = quadraticBezier(p1, p2, p3, p4, t0);
const p44 = quadraticBezier(p1, p2, p3, p4, t1);

p22 = u0 * u0 * u1 * p1 + (t0* u0 * u1 + u0 * t0 * u1 + u0 * u0 * t1) * p2 + (t0 * t0 * u1 + u0 * t0 * t1 + t0 * u0 * t1) *p 3 + t0 * t0 * t1* p4;

p33 = u0 * u1 * u1 * p1 + (t0 * u1 * u1 + u0 * t1 * u1 + u0 * u1 * t1) * p2 + (t0 * t1 * u1 + u0 * t1 * t1 + t0 * u1 * t1) *p 3 + t0 * t1 * t1 * p4

```

[参考](https://stackoverflow.com/questions/878862/drawing-part-of-a-b%C3%A9zier-curve-by-reusing-a-basic-b%C3%A9zier-curve-function)