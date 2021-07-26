**给定经纬度、距离、角度，求另外一点**
```
export const EquatorialRadius = 6378137.0; // 赤道半径
export const PolarRadius = 6356752.0; // 极地半径
export const EquatorialCircumference = 2 * Math.PI * EquatorialRadius;
export const RAD = Math.PI / 180.0;
/**
 * 参考https://www.cnblogs.com/softfair/p/lat_lon_distance_bearing_new_lat_lon.html
 * @param {*} lat 
 * @param {*} lon 
 * @param {number} distance 距离 单位米
 * @param {number} anesgle 角度 与正北方向夹角，顺时针
 */
export function getlatLon(lon, lat, distance, angle) {

    const dx = distance * Math.Sin(angle * RAD);

    const dy = distance * Math.Cos(angle * RAD);

    // 修正因为纬度不断变化的球半径长度，如果在lat=0，即在赤道上的时候，那ec就刚好是赤道半径；如果在极点lat=90，那ec 就刚好是极半径。
    const ec = PolarRadius + (EquatorialRadius - PolarRadius) * (90.0 - lat) / 90.0;
    // lat所在纬度的纬度圈的半径
    const ed = ec * Math.Cos(lat * RAD);

    const newLon = (dx / ed + lon * RAD) * 180.0 / Math.PI;

    const newLat = (dy / ec + lat * RAD) * 180.0 / Math.PI;

    return [newLon, newLat];

}
```
**球面距离**
```
/**
 * 球面距离
 * @param {*} lnglat1 
 * @param {*} lnglat2 
 */
export function sphericalDistance(lnglat1, lnglat2) {
    const radLat1 = RAD * lnglat1[1];
    const radLat2 = RAD * lnglat2[1];
    const a = radLat1 - radLat2;
    const b = RAD * lnglat2[0] - RAD * lnglat2[0];
    let s = 2 * Math.asin(Math.sqrt(Math.pow(Math.sin(a / 2), 2) +
        Math.cos(radLat1) * Math.cos(radLat2) * Math.pow(Math.sin(b / 2), 2)));
    s = s * EquatorialRadius * 1000;
    return s;
}
```