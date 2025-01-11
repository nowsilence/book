**求点到线段上的垂足点（不一定在线段上）**

```
function pedalPoint(p, p0, p1) {

    var retVal;

    var dx = p0.x - p1.x;
    var dy = p0.y - p1.y;

    if(Math.abs(dx) < 0.00000001 && Math.abs(dy) < 0.00000001 ) {
        return p0;
    }

   
    // 点乘
    var u = (p.x - p0.x) * (p0.x - p1.x) + (p.y - p0.y) * (p0.y - p1.y);

    u = u / (dx * dx + dy * dy);

    var x = p0.x + u * dx;

    var y = p0.y + u * dy;

    return { x: x, y: y }
}



function pedalPoint(p, p0, p1) {

    var retVal;

    var dx = p0.x - p1.x;
    var dy = p0.y - p1.y;
    var dz = p0.z - p1.z;

    if(Math.abs(dx) < 0.00000001 && Math.abs(dy) < 0.00000001 && Math.abs(dz) < 0.00000001) {
        return p0;
    }

   
    // 点乘
    var u = (p.x - p0.x) * (p0.x - p1.x) + (p.y - p0.y) * (p0.y - p1.y) + (p.z - p0.z)*(p0.z - p1.z);;

    u = u / (dx * dx + dy * dy + dz * dz);

    var x = p0.x + u * dx; 

    var y = p0.y + u * dy;

    var z = p0.z + u * dz;
    return { x: x, y: y, z: z }
}

```

[参考](https://www.cnblogs.com/star91/articles/4770453.html)