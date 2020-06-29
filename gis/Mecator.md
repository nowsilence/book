**墨卡托投影**


```
const EquatorialRadius = 6378137.0; // 赤道半径
const PolarRadius = 6356752.0; // 极地半径

const PIR = Math.PI * EquatorialRadius;
const PI2 = Math.PI / 2;
const PIR180 = PIR / 180;

project(coordinate) {
    const [lng, lat, altitude = 0] = coordinate;
    
    const x = lng * PIR180;
    const y = Math.log(Math.tan((90 + lat) * Math.PI / 360)) / RAD * PIR180;
    if (isNaN(x)) {
        console.log('坐标错误！');
    }
    return [x, y, altitude];
}

unproject(point) {
    const [x, y, z = 0] = point;

    const lng =  x / PIR * 180;
    let lat = y / PIR * 180;
    lat =  180 / Math.PI * ( 2 * Math.atan(Math.exp(lat * RAD))- PI2);

    return [lng, lat, z];
}
```

**分辨率/墨卡托级别互换**

```

const degree2Rad = Math.PI / 180.0;
// 地球半径
const EarthRadius = 6378137;
// 瓦片大小
const tileSize = 256;
// 当前纬度的周长
const circumference = Math.cos(degree2Rad * lat) * PI2 * EarthRadius;

// 知道当前级别 level，求当前纬度的分辨率 单位 米/像素
const resolution = circumference / Math.pow(2, level) / tileSize;

// 已知分辨率 resolution ，求当前级别
const level = Math.floor(Math.log2(circumference / (tileSize * resolution)));

```