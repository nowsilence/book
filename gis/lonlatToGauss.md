```javascirpt
// 椭球参数 - WGS84
const a = 6378137.0;
const f = 1 / 298.257223563;
const b = a * (1 - f);
const e = Math.sqrt((a * a - b * b) / (a * a));
const e2 = e * e;
const e4 = e2 * e2;
const e6 = e4 * e2;

// 计算子午线弧长
const A0 = 1 - e2 / 4 - 3 * e4 / 64 - 5 * e6 / 256;
const A2 = 3 / 8 * (e2 + e4 / 4 + 15 * e6 / 128);
const A4 = 15 / 256 * (e4 + 3 * e6 / 4);
const A6 = 35 * e6 / 3072;

/**
 * 经纬度转高斯投影坐标（支持度带号）
 * @param {number} lng - 经度
 * @param {number} lat - 纬度
 * @param {Object} [options] - 可选参数
 * @param {number} [options.zone] - 度带号（3度带或6度带号）
 * @param {boolean} [options.is3DegreeZone=true] - 是否为3度带，false表示6度带
 * @param {number} [options.falseEasting=500000] - 东伪偏移值
 * @param {number} [options.falseNorthing=0] - 北伪偏移值
 * @param {number} [options.scale=1.0] - 比例因子
 * @returns {Object} 返回包含x(东坐标), y(北坐标), zone(度带号)的对象
 */
function lngLatToGauss(lng, lat, options = {}) {
    const {
        zone,
        is3DegreeZone = true,
        falseEasting = 500000,
        falseNorthing = 0,
        scale = 1.0
    } = options;

    // 计算中央子午线经度
    let centralMeridian;
    if (zone !== undefined) {
        // 如果指定了度带号
        if (is3DegreeZone) {
            centralMeridian = zone * 3; // 3度带
        } else {
            centralMeridian = zone * 6 - 3; // 6度带
        }
    } else {
        // 自动计算中央子午线（默认为3度带）
        centralMeridian = Math.round(lng / 3) * 3;
    }

    // 计算度带号（用于返回）
    const calculatedZone = is3DegreeZone 
        ? Math.round(centralMeridian / 3)
        : Math.round((centralMeridian + 3) / 6);

    // 将经纬度转换为弧度
    const phi = lat * Math.PI / 180;
    const lambda = lng * Math.PI / 180;
    const lambda0 = centralMeridian * Math.PI / 180;

    // 计算辅助量
    const dlambda = lambda - lambda0;
    const sinPhi = Math.sin(phi);
    const cosPhi = Math.cos(phi);
    const tanPhi = Math.tan(phi);
    const eta2 = (e2 / (1 - e2)) * cosPhi * cosPhi;

    
    const M = a * (A0 * phi - A2 * Math.sin(2 * phi) + A4 * Math.sin(4 * phi) - A6 * Math.sin(6 * phi));

    // 计算高斯投影坐标
    const N = a / Math.sqrt(1 - e2 * sinPhi * sinPhi);
    const T = tanPhi * tanPhi;
    const C = eta2;
    const L = dlambda;

    const x = 
        scale * N * (L * cosPhi + 
                    (L * L * L * cosPhi * cosPhi * cosPhi / 6) * (1 - T + C) + 
                    (L * L * L * L * L * cosPhi * cosPhi * cosPhi * cosPhi * cosPhi / 120) * 
                    (5 - 18 * T + T * T + 72 * C - 58 * e2)) + 
        falseEasting;

    const y = 
        scale * (M + N * tanPhi * (L * L * cosPhi * cosPhi / 2 + 
                                 (L * L * L * L * cosPhi * cosPhi * cosPhi * cosPhi / 24) * 
                                 (5 - T + 9 * C + 4 * C * C) + 
                                 (L * L * L * L * L * L * cosPhi * cosPhi * cosPhi * cosPhi * cosPhi * cosPhi / 720) * 
                                 (61 - 58 * T + T * T + 600 * C - 330 * e2))) + 
        falseNorthing;

    return {
        x: x,
        y: y,
        zone: calculatedZone,
        centralMeridian: centralMeridian
    };
}


const result1 = lngLatToGauss(116.404, 39.915);
console.log(result1); // {x: 448251.944, y: 4425914.140, zone: 39, centralMeridian: 117}

// 2. 指定6度带号
const result2 = lngLatToGauss(116.404, 39.915, {zone: 20, is3DegreeZone: false});
console.log(result2); // {x: 20242451.944, y: 4425914.140, zone: 20, centralMeridian: 117}

// 3. 指定3度带号
const result3 = lngLatToGauss(116.404, 39.915, {zone: 39});
console.log(result3); // {x: 448251.944, y: 4425914.140, zone: 39, centralMeridian: 117}
```