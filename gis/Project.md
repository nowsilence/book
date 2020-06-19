**将WGS84坐标投影到以地心为原点的直角坐标系中**


*代码提取自cesium*

````
const toRad = Math.PI / 180;

const scratchN = new Point();
const scratchK = new Point();

const radii = new Point(
    6378137.0 * 6378137.0, 
    6378137.0 * 6378137.0, 
    6356752.3142451793 * 6356752.3142451793
);

const EPSILON1 = 0.1;
const wgs84OneOverRadii = new Point(1.0 / 6378137.0, 1.0 / 6378137.0, 1.0 / 6356752.3142451793);
const wgs84OneOverRadiiSquared = new Point(1.0 / (6378137.0 * 6378137.0), 1.0 / (6378137.0 * 6378137.0), 1.0 / (6356752.3142451793 * 6356752.3142451793));
const wgs84CenterToleranceSquared = EPSILON1;

const sign = Math.sign || function sign(x) {
    x = +x ;// convert to a number
    if (x === 0 || isNaN(x))
        return x;
    return x > 0 ? 1 : -1;
};

/**
 * 以地心为原点直角坐标系
 */
class GeocentricProjector extends Projector {

    project(coordinate) {
        let [lng, lat, altitude = 0] = coordinate;

        lng = toRad * lng;
        lat = toRad * lat;

        const cosLatitude = Math.cos(lat);
        scratchN.x = cosLatitude * Math.cos(lng);
        scratchN.y = cosLatitude * Math.sin(lng);
        scratchN.z = Math.sin(lat);

        scratchN._unit();

        radii._mult(scratchN, scratchK);
        
        const gamma = Math.sqrt(scratchN.dot(scratchK));

        scratchK._divScalar(gamma);

        scratchN._multScalar(altitude);

        return scratchK.add(scratchN);;
    }
    
    unproject(point) {
        var oneOverRadii =  wgs84OneOverRadii;
        var oneOverRadiiSquared =  wgs84OneOverRadiiSquared;
        var centerToleranceSquared = wgs84CenterToleranceSquared;

        //`cartesian is required.` is thrown from scaleToGeodeticSurface
        var p = scaleToGeodeticSurface(point, oneOverRadii, oneOverRadiiSquared, centerToleranceSquared);

        if (p == undefined) {
            return undefined;
        }
        
        var n = p.mult(oneOverRadiiSquared);;
        n = n._unit();

        var h = point.sub(p);
        
        var longitude = Math.atan2(n.y, n.x);
        var latitude = Math.asin(n.z);
        var height = sign(h.dot(point)) * h.mag();

        return [longitude, latitude, height];
    }
}


/**
 * Point类，代表一个坐标点.
 */
class Point {
    /**
     * 初始化Point对象x,y为坐标点,如果为undefined,则会使用默认值0.
     * @param {Number}[x=0] - 点符号x坐标位置
     * @param {Number}[y=0] - 点符号y坐标位置
     */
    constructor(x, y, z) {
        this.type = 'Point';
        this.z = 0;
        if (Array.isArray(x)) {
            if (x.length >= 2) {
                this.x = x[0] || 0;
                this.y = x[1] || 0;
            }

            if (x.length == 3) {
                this.z = x[2];
            }
        } else if (x != null && typeof x == 'object') {
            this.x = x.x || 0;
            this.y = x.y || 0;
            this.z = x.z || 0;
        } else {
            this.x = x || 0;
            this.y = y || 0;
            this.z = z || 0;
        }
    }

    /**
     * 克隆点符号对象,返回新对象.
     * @return {object} Point 克隆的对象
     */
    clone() {
        const clonePt = new Point();
        clonePt.x = this.x;
        clonePt.y = this.y;
        clonePt.z = this.z;

        return clonePt;
    }

    /**
     * 计算当前点与目标点之间的距离.
     * @param {object} p - 目标点位
     * @return {Number} - 当前点与目标点之间的距离
     */
    distance(p) {
        return this.sub(p).mag();
        // return Math.sqrt((this.x - p.x) * (this.x - p.x) + (this.y - p.y) * (this.y - p.y));
    }

    distanceSqured(p) {
        return this.sub(p).magSqured();
        // return Math.sqrt((this.x - p.x) * (this.x - p.x) + (this.y - p.y) * (this.y - p.y));
    }

    dist(p) {
        return this.distance(p);
    }

    add(p) {
        return this.clone()._add(p);
    }

    _add(p, result) {
        const ret = result || this;
        ret.x = this.x + p.x;
        ret.y = this.y + p.y;
        ret.z = this.z + p.z;
        return ret;
    }

    sub(p) {
        return this.clone()._sub(p);
    }

    _sub(p, result) {
        const ret = result || this;
        ret.x = this.x - p.x;
        ret.y = this.y - p.y;
        ret.z = this.z - p.z;
        return ret;
    }

    subScalar(k) {
        return this.clone()._subScalar(k);
    }

    _subScalar(k, result) {
        const ret = result || this;

        ret.x = this.x - k;
        ret.y = this.y - k;
        ret.z = this.z - k;
        return this;
    }

    _multScalar(k, result) {
        const p = result || this;
        p.x = this.x * k;
        p.y = this.y * k;
        p.z = this.z * k;
        return p;
    }

    multScalar(k) {
        return this.clone()._multScalar(k);
    }

    _mult(p, result) {
        const ret = result || this;

        ret.x = this.x * p.x;
        ret.y = this.y * p.y;
        ret.z = this.z * p.z;
        return ret;
    }

    mult(p) {
        return this.clone()._mult(p);
    }

    _div(p, result) {
        const ret = result || this;

        ret.x = this.x / p.x;
        ret.y = this.y / p.y;
        ret.z = this.z / p.z;
        return ret;
    }

    div(p) {
        return this.clone()._div(p);
    }

    divScalar(k) {
        return this.clone()._divScalar(k);
    }

    _divScalar(k, result) {
        const p = result || this;
        p.x = this.x / k;
        p.y = this.y / k;
        p.z = this.z / k;
        return p;
    }

    dot(p) {
        return this.x * p.x + this.y * p.y + this.z * p.z;
    }

    cross(v) {

        return this.x * v.y - this.y * v.x;

    }

    unit() {
        return this.clone()._unit();
    }

    _unit() {
        this._divScalar(this.mag());
        return this;
    }

    mag() {
        return Math.sqrt(this.magSqured());
    }

    magSqured() {
        return this.x * this.x + this.y * this.y + this.z * this.z;
    }

    _perp() {
        const y = this.y;
        this.y = this.x;
        this.x = -y;
        return this;
    }

    /**
     * perpendicular 获取垂直向量，在xy平面上的垂直向量
     */
    perp() {
        return this.clone()._perp();
    }

    round() {
        return this.clone()._round();
    }

    _round() {
        this.x = Math.round(this.x);
        this.y = Math.round(this.y);
        this.z = Math.round(this.z);
        return this;
    }

    angleWith(b) {
        return this.angleWithSep(b.x, b.y);
    }

    angleWithSep(x, y) {
        return Math.atan2(
            this.x * y - this.y * x,
            this.x * x + this.y * y
        );
    }

    /**
     * 判断两个点坐标是否相等.
     * @param {object} p - 传入的点位
     * @return {boolean} - 返回boolean值表示点坐标是否相等
     */
    equals(p) {
        if (this.x !== p.x || this.y !== p.y || this.z !== p.z) {
            return false;
        }

        return true;
    }

    // encode() {
    //     return [
    //         double2Floats(this.x),
    //         double2Floats(this.y),
    //         double2Floats(this.z)
    //     ];
    // }

    encode() {
        const x = double2Floats(this.x);
        const y = double2Floats(this.y);
        const z = double2Floats(this.z);
        return [
            [x[0], y[0], z[0]],
            [x[1], y[1], z[1]],
        ];
    }

    toArray() {
        return [this.x, this.y, this.z];
    }

    static convert(a) {
        if (a instanceof Point) {
            return a;
        }
        if (Array.isArray(a)) {
            return new Point(a);
        }
        return a;
    }

    static toArray(a) {
        if (a instanceof Point) {
            return a.toArray();
        }
        if (Array.isArray(a)) {
            return a;
        }

        return a;
    }
}


var scaleToGeodeticSurfaceIntersection = new Point();
var scaleToGeodeticSurfaceGradient = new Point();

const EPSILON12 = 0.000000000001;

function scaleToGeodeticSurface(point, oneOverRadii, oneOverRadiiSquared, centerToleranceSquared) {
    

    var positionX = point.x;
    var positionY = point.y;
    var positionZ = point.z;

    var oneOverRadiiX = oneOverRadii.x;
    var oneOverRadiiY = oneOverRadii.y;
    var oneOverRadiiZ = oneOverRadii.z;

    var x2 = positionX * positionX * oneOverRadiiX * oneOverRadiiX;
    var y2 = positionY * positionY * oneOverRadiiY * oneOverRadiiY;
    var z2 = positionZ * positionZ * oneOverRadiiZ * oneOverRadiiZ;

    // Compute the squared ellipsoid norm.
    var squaredNorm = x2 + y2 + z2;
    var ratio = Math.sqrt(1.0 / squaredNorm);

    // As an initial approximation, assume that the radial intersection is the projection point.
    var intersection = point._multScalar(ratio, scaleToGeodeticSurfaceIntersection);// Cartesian3.multiplyByScalar(point, ratio, scaleToGeodeticSurfaceIntersection);

    // If the position is near the center, the iteration will not converge.
    if (squaredNorm < centerToleranceSquared) {
        return !isFinite(ratio) ? undefined : intersection.clone();
    }

    var oneOverRadiiSquaredX = oneOverRadiiSquared.x;
    var oneOverRadiiSquaredY = oneOverRadiiSquared.y;
    var oneOverRadiiSquaredZ = oneOverRadiiSquared.z;

    // Use the gradient at the intersection point in place of the true unit normal.
    // The difference in magnitude will be absorbed in the multiplier.
    var gradient = scaleToGeodeticSurfaceGradient;
    gradient.x = intersection.x * oneOverRadiiSquaredX * 2.0;
    gradient.y = intersection.y * oneOverRadiiSquaredY * 2.0;
    gradient.z = intersection.z * oneOverRadiiSquaredZ * 2.0;

    // Compute the initial guess at the normal vector multiplier, lambda.
    var lambda = (1.0 - ratio) * point.mag() / (0.5 * gradient.mag());
    var correction = 0.0;

    var func;
    var denominator;
    var xMultiplier;
    var yMultiplier;
    var zMultiplier;
    var xMultiplier2;
    var yMultiplier2;
    var zMultiplier2;
    var xMultiplier3;
    var yMultiplier3;
    var zMultiplier3;

    do {
        lambda -= correction;

        xMultiplier = 1.0 / (1.0 + lambda * oneOverRadiiSquaredX);
        yMultiplier = 1.0 / (1.0 + lambda * oneOverRadiiSquaredY);
        zMultiplier = 1.0 / (1.0 + lambda * oneOverRadiiSquaredZ);

        xMultiplier2 = xMultiplier * xMultiplier;
        yMultiplier2 = yMultiplier * yMultiplier;
        zMultiplier2 = zMultiplier * zMultiplier;

        xMultiplier3 = xMultiplier2 * xMultiplier;
        yMultiplier3 = yMultiplier2 * yMultiplier;
        zMultiplier3 = zMultiplier2 * zMultiplier;

        func = x2 * xMultiplier2 + y2 * yMultiplier2 + z2 * zMultiplier2 - 1.0;

        // "denominator" here refers to the use of this expression in the velocity and acceleration
        // computations in the sections to follow.
        denominator = x2 * xMultiplier3 * oneOverRadiiSquaredX + y2 * yMultiplier3 * oneOverRadiiSquaredY + z2 * zMultiplier3 * oneOverRadiiSquaredZ;

        var derivative = -2.0 * denominator;

        correction = func / derivative;
    } while (Math.abs(func) > EPSILON12);

    return new Point(
        positionX * xMultiplier,
        positionY * yMultiplier,
        positionZ * zMultiplier
    );
}
```