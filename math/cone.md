[参考](https://www.geometrictools.com/Documentation/IntersectionLineCone.pdf)

```javascript
const INTERSECTION_TYPE = {
    EMPTY: 0,
    POINT: 1,
    RAY_POSITIVE: 2,
    RAY_NEGATIVE: 3,
    SEGMENT: 4,
};
Object.freeze(INTERSECTION_TYPE);

class Cone {
    constructor(ray, angle, minHeight = 0, maxHeight = -1) {
        this.ray = ray;
        this.minHeight = minHeight;
        this.maxHeight = maxHeight;
        this.angle = angle;

        const cosAngle = Math.cos(angle);
        this.cosAngleSqr = cosAngle * cosAngle;
    }

    heightInRange(h) {
        return this.minHeight <= h && (this.maxHeight != -1 ? h <= this.maxHeight : true);
    }

    get isFinite() {
        return this.maxHeight != -1;
    }
}

function setEmpty(result) {
    result.t[0] = Infinity;
    result.t[1] = Infinity;
    result.type = INTERSECTION_TYPE.EMPTY;
}

function setPoint(t0, result) {
    result.type = INTERSECTION_TYPE.POINT;
    result.t[0] = t0;
    result.t[1] = Infinity;
}

function setSegment(t0, t1, result) {
    result.type = INTERSECTION_TYPE.SEGMENT;
    result.t[0] = t0;
    result.t[1] = t1;
}

function setRayPositive(t0, result) {
    result.type = INTERSECTION_TYPE.RAY_POSITIVE;
    result.t[0] = t0;
    result.t[1] = Infinity;
}

function setRayNegative(t1, result) {
    result.type = INTERSECTION_TYPE.RAY_NEGATIVE;
    result.t[0] = Infinity;
    result.t[1] = t1;
}

function findIntersection(u0, u1, v0, v1, overlap) {
    let numValid;

    if (u1 < v0 || v1 < u0) {
        numValid = 0;
    } else if (v0 < u1) {
        if (u0 < v1) {
            overlap[0] = (u0 < v0 ? v0 : u0);
            overlap[1] = (u1 > v1 ? v1: u1);

            if (overlap[0] < overlap[1]) {
                numValid = 2;
            } else {
                numValid = 1;
            }
        } else {
            overlap[0] = u0;
            overlap[1] = u0;
            numValid = 1;
        }
    } else {
        overlap[0] = v0;
        overlap[1] = v0;
        numValid = 1;
    }

    return numValid;
}

function findIntersection1(u0, u1, v, overlap) {
    let numValid;

    if (u1 > v) {
        numValid = 2;
        overlap[0] = Math.max(u0, v);
        overlap[1] = u1;
    } else if (u1 == v) {
        numValid = 1;
        overlap[0] = v;
    } else {
        numValid = 0;
    }

    return numValid;
}

function setPointClamp(t0, h0, cone, result) {
    if (cone.heightInRange(h0)) {
        setPoint(t0, result);
    } else {
        setEmpty(result);
    }
}

function setSegmentClamp(t0, t1, h0, h1, DdU, DdPmV, cone, result) {
    if (h1 > h0) {
        let numValid;
        const ovelap = [];
        if (cone.isFinite) {
            numValid = findIntersection(h0, h1, cone.minHeight, cone.maxHeight, ovelap);
        } else {
            numValid = findIntersection1(h0, h1, cone.minHeight, ovelap);
        }

        if (numValid == 2) {
            const t0 = (ovelap[0] - DdPmV) / DdU;
            const t1 = (ovelap[1] - DdPmV) / DdU;
            return setSegment(t0, t1, result);
        } else if (numValid == 1) {
            const t0 = (ovelap[0] - DdPmV) / DdU;
            return setPoint(t0, result);
        } else {
            return setEmpty(result);
        }
    } else {
        if (cone.heightInRange(h0)) {
            return setSegment(t0, t1, result);
        } else {
            return setEmpty(result);
        }
    }
}

function setRayClamp(h, DdU, DdPmV, cone, result) {
    if (cone.isFinite) {
        const overlap = [];
        const numValid = findIntersection1(cone.minHeight, cone.maxHeight, h, overlap);
        if (numValid == 2) {
            return setSegment((overlap[0] - DdPmV) / DdU, (overlap[1] - DdPmV) / DdU, result);
        } else if (numValid == 1) {
            return setPoint((overlap[0] - DdPmV) / DdU, result);
        } else {
            return setEmpty(result);
        }
    } else {
        return setRayPositive((Math.max(cone.minHeight, h) - DdPmV) / DdU, result);
    }
}

function intersection(ray, cone, result) {
    const PmV = ray.origin.clone().sub(cone.ray.origin);
    const UdU = ray.direction.dot(ray.direction);
    const DdU = cone.ray.direction.dot(ray.direction);
    const DdPmV = cone.ray.direction.dot(PmV);
    const UdPmV = ray.direction.dot(PmV);
    const PmVdPmV = PmV.dot(PmV);
    const c2 = DdU * DdU - cone.cosAngleSqr * UdU;
    const c1 = DdU * DdPmV - cone.cosAngleSqr * UdPmV;
    const c0 = DdPmV * DdPmV - cone.cosAngleSqr * PmVdPmV;

    if (c2 != 0) {
        const discr = c1 * c1 - c0 * c2;

        if (discr < 0) {
            c2NotZeroDiscrNeg(result);
        } else if (discr > 0) {
            c2NotZeroDiscrPos(c1, c2, discr, DdU, DdPmV, cone, result);
        } else {
            c2NotZeroDiscrZero(c1, c2, UdU, UdPmV, DdU, DdPmV, cone, result);
        }
    } else if (c1 != 0) {
        c2ZeroC1NotZero(c0, c1, DdU, DdPmV, cone, result);
    } else {
        c2ZeroC1Zero(c0, UdU)
    }
}

function c2NotZeroDiscrNeg(result) {
    return setEmpty(result);
}

function c2NotZeroDiscrPos(c1, c2, discr, DdU, DdPmV, cone, result) {
    const x = -c1 / c2;
    const y = (c2 > 0 ? 1 / c2 : -1 / c2);
    
    const t0 = x - y * Math.sqrt(discr);
    const t1 = x + y * Math.sqrt(discr);
    const h0 = t0 * DdU + DdPmV;
    const h1 = t1 * DdU + DdPmV;

    if (h0 >= 0) {
        return setSegmentClamp(t0, t1, h0, h1, DdU, DdPmV, cone, result)
    } else if (h1 <= 0) {
        return setEmpty(result);
    } else {
        return setRayClamp(h1, DdU, DdPmV, cone, result);
    }
}

function c2NotZeroDiscrZero(c1, c2, UdU, UdPmV, DdU, DdPmV, cone, result) {
    const t = -c1 / c2;
    if (t * UdU + UdPmV == 0) {
        if (c2 < 0) {
            return setPointClamp(t, 0, cone, result)
        } else {
            return setRayClamp(0, DdU, DdPmV, cone, result);
        }
    } else {
        const h = t * DdU + DdPmV;
        if (h >= 0) {
            return setPointClamp(t, h, cone, result);
        } else {
            return setEmpty(result);
        }
    }
}

function c2ZeroC1NotZero(c0, c1, DdU, DdPmV, cone, result) {
    const t = -c0 / (2 * c1);
    const h = t * DdU + DdPmV;
    if (h > 0) {
        return setRayClamp(h, DdU, DdPmV, cone, result);
    } else {
        return setEmpty(result);
    }
}

function c2ZeroC1Zero(c0, UdU, UdPmV, DdU, DdPmV, cone, result) {
    if (c0 != 0) {
        return setEmpty(result);
    } else {
        const t = -UdPmV / UdU;
        const h = t * UdU + DdPmV;
        return setRayClamp(h, DdU, DdPmV, cone, result);
    }
}


function lineIntersectsCone(ray, cone, result) {
    if (ray.direction.dot(cone.ray.direction) >= 0) {
        intersection(ray, cone, result);
    } else {
        ray.direction.negate();
        intersection(ray, cone, result);
        result.t[0] = -result.t[0];
        result.t[1] = -result.t[1];

        const tmp = result.t[0];
        result.t[0] = result.t[1];
        result.t[1] = tmp;
        if (result.type == 2) {
            result.type = 3;
        }
    }
}

function computePoints(intersectionType, origin, direction, result) {
    switch (intersectionType)
    {
        case INTERSECTION_TYPE.POINT:
        case INTERSECTION_TYPE.RAY_POSITIVE:
            return [direction.clone().multiplyScalar(result.t[0]).add(origin)];
        case INTERSECTION_TYPE.RAY_NEGATIVE:
            return [direction.clone().multiplyScalar(result.t[1]).add(origin)]; 
        case INTERSECTION_TYPE.SEGMENT:
            return [
                direction.clone().multiplyScalar(result.t[0]).add(origin),
                direction.clone().multiplyScalar(result.t[1]).add(origin)
            ];
    }

    return null;
}

function rayIntersectsCone(ray, cone) {
    const result = {
        t: [Infinity, Infinity],
        type: INTERSECTION_TYPE.EMPTY
    };

    lineIntersectsCone(ray, cone, result);

    if (result.type != INTERSECTION_TYPE.EMPTY) {

        if (result.type == INTERSECTION_TYPE.POINT) {
            if (result.t[0] < 0) {
                setEmpty(result);
            }
        } else if (result.type == INTERSECTION_TYPE.SEGMENT) {
            if (result.t[1] > 0) {
                setSegment(Math.max(result.t[0], 0), result.t[1], result);
            } else if (result.t[1] < 0) {
                setEmpty(result);
            } else {
                setPoint(0, result);
            }
        } else if (result.type == INTERSECTION_TYPE.RAY_POSITIVE) {
            setRayPositive(Math.max(result.t[0], 0), result);
        } else {
            if (result.t[1] > 0) {
                setSegment(0, result.t[1], result);
            } else if (result.t[1] < 0) {
                setEmpty(result);
            } else {
                setPoint(0, result);
            }
        }
    }

    return computePoints(result.type, ray.origin, ray.direction);
}

```