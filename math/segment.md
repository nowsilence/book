```javascript

const _point0 = new Vector2();
const _point1 = new Vector2();
const _point2 = new Vector2();
const _point3 = new Vector2();

const _v0 = new Vector2();
const _v1 = new Vector2();

/**
 * 线段相交
 */
function intersectSegment(p0, p1, q0, q1) {
    _point0.fromArray(p0);
    _point1.fromArray(p1);

    _point2.fromArray(q0);
    _point3.fromArray(q1);

    _v1.subVectors(_point3, _point2);
    _v0.subVectors(_point1, _point0);

    const result = {};

    if (_v0.lengthSq() == 0 || _v1.lengthSq() == 0) {
        return result;
    }

    const denominator = _v0.cross(_v1);
    result.denominator = denominator;

    _v0.subVectors(_point0, _point2);
    let ua = _v.cross(_v0);

    _v1.subVectors(_point1, _point0);
    let ub = _v1.cross(_v0);

    if (denominator === 0 && ua === 0 && ub === 0) {
        result.isCollinear = true;
        return result;
    }

    if (denominator === 0) {
        result.isParallel = true;
        return result;
    }

    ua /= denominator;
    ub /= denominator;

    result.t = ua;
    result.s = ub;

    if (ua < 0 || ua > 1 || ub < 0 || ub > 1) {
        // 交点不在线段上
        return result;
    }

    _point0.add(_point1.sub(_pointer0).multiplyScalar(ua));

    result.intersection = _point0.toArray();

    return result;
}
```