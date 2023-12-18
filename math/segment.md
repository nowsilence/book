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
function pointDistSegment(point, start, end) {
    const v0 = point.clone().sub(start);
    const v1 = end.clone().sub(start);

    const v1sqrLength = v1.dot(v1);
    const v1_v0 = v1.dot(v0);

    let t = v1_v0 / v1sqrLength;

    if (clampToLine) {
        t = Math.max(0, Math.min(1, t));
    }

    v1.multiplyScalar(t).add(start);

    return {
        t,
        distance: v1.distanceTo(point),
        point: v1
    };
}

function douglasPeucker3(points, epsilon) {
    const stack = [
        {
            start: 0,
            end: points.length - 1
        }
    ];

    const result = [];
    while(stack.length > 0) {
        const tmp = stack.pop();
        let dMax = 0;
        let index = 0;

        for (let g = tmp.start + 1; g < tmp.end; g++) {
            const { distance } = pointDistSegment(points[g], points[tmp.start], points[tmp.end]);
            if (distance > dMax) {
                index = g;
                dMax = distance;
            }
        }

        if (dMax > epsilon) {
            stack.push({ start: tmp.start, end: index });
            stack.push({ start: index, end: tmp.end });
        } else {
            if (result.length) {
                result.pop();
            }

            result.push(points[tmp.end]);
            result.push(points[tmp.start]);
        }
    }

    return result.reverse();
}
```