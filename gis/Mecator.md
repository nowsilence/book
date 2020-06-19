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