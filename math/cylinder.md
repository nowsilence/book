```javascript

class Cylinder {
    constructor(axis, radius, height) {
        this.axis = axis;
        this.radius = radius;
        this.height = height;
    }

    static create(aPos, anotherPos, radius) {
        const origin = anotherPos.clone().add(aPos).multiplyScalar(0.5);
        const direction = anotherPos.clone().sub(aPos);
        const height = direction.length();
        direction.normalize();

        return new Cylinder({ origin, direction }, radius, height);
    }
}

function computeOrthogonalComplement(v){

    const v1 = v.clone();

    if (v.x > v.y) {
        v1.set(-v.z, 0, v.x);
    } else {
        v1.set(0, v.z, -v.y);
    }

    v1.normalize();

    const v2 = v.clone().cross(v1);
    
    return [v, v1, v2];
}

function rayIntersectCylinder(ray, cylinder) {
    
    const result = { parameter: [], numIntersections: 0 };

    lineIntersectCylinder(ray.origin, ray.direction, cylinder, result);

    if (result.intersect) {
        const overlap = [];
        if (result.parameter[1] > 0) {

            overlap[0] = Math.max(result.parameter[0], 0);
            overlap[1] = result.parameter[1];
            if (overlap[0] < overlap[1]) {
                result.numIntersections = 2;
            } else {
                result.numIntersections = 1;
            }
        }
        else if (result.parameter[1] == 0) {

            result.numIntersections = 1;
            overlap[0] = 0;
        } else {

            result.numIntersections = 0;
            result.intersect = false;
        }

        result.parameter = overlap
    }

    if (result.intersect) {
        result.point = [];
        for (let i = 0; i < result.numIntersections; ++i) {
            result.point[i] = ray.direction.clone().multiplyScalar(result.parameter[i]).add(ray.origin);
        }
    }

    return result;
}

function lineIntersectCylinder(origin, direction, cylinder, result) {
    const basis = computeOrthogonalComplement(cylinder.axis.direction);

    const [W, U, V] = basis;
    
    const halfHeight = 0.5 * cylinder.height;
    const rSqr = cylinder.radius * cylinder.radius;

    const diff = origin.clone().sub(cylinder.axis.origin);
    const P = [U.dot(diff), V.dot(diff), W.dot(diff)];

    const zero = 0;
    const dz = W.dot(direction);

    if (Math.abs(dz) == 1) {
        const radialSqrDist = rSqr - P[0] * P[0] - P[1] * P[1];

        if (radialSqrDist >= 0) {
            result.intersect = true;
            result.numIntersections = 2;

            if (dz > 0) {
                result.parameter = [
                    -P[2] - halfHeight,
                    -P[2] + halfHeight
                ];
            } else {
                result.parameter = [
                    P[2] - halfHeight,
                    P[2] - halfHeight
                ];
            }
        }
        return;
    }

    const D = [U.dot(direction), V.dot(direction), dz];

    if (D[2] == zero) {

        if (Math.abs(P[2]) <= halfHeight) {
            const a0 = P[0] * P[0] + P[1] * P[1] - rSqr;
            const a1 = P[0] * D[0] + P[1] * D[1];
            const a2 = D[0] * D[0] + D[1] * D[1];
            const discr = a1 * a1 - a0 * a2;

            if (discr > 0) {
                result.intersect = true;
                result.numIntersections = 2;
                const root = Math.sqrt(discr);
                result.parameter = [
                    (-a1 - root) / a2,
                    (-a1 + root) / a2
                ];
            } else if (discr == 0) {
                result.intersect = true;
                result.numIntersections = 1;
                result.parameter = [
                    -a1 / a2,
                ]
            }
        }

        return;
    }

    const t0 = (-halfHeight - P[2]) / D[2];
    let xTmp = P[0] + t0 * D[0];
    let yTmp = P[1] + t0 * D[1];

    
    if (xTmp * xTmp + yTmp * yTmp <= rSqr) {
        result.parameter[result.numIntersections++] = t0;
    }

    const t1 = (halfHeight - P[2]) / D[2];
    xTmp = P[0] + t1 * D[0];
    yTmp = P[1] + t1 * D[1];

    if (xTmp * xTmp + yTmp * yTmp <= rSqr) {
        result.parameter[result.numIntersections++] = t1;
    }

    if (result.numIntersections < 2) {
        const a0 = P[0] * P[0] + P[1] * P[1] - rSqr;
        const a1 = P[0] * D[0] + P[1] * D[1];
        const a2 = D[0] * D[0] + D[1] * D[1];
        const discr = a1 * a1 - a0 * a2;

        if (discr > 0) {
            const root = Math.sqrt(discr);
            const tValue = (-a1 - root) / a2;

            if (t0 <= t1) {
                if (t0 <= tValue && tValue <= t1) {
                    result.parameter[result.numIntersections++] = tValue;
                }
            } else {
                if (t1 <= tValue && tValue <= t0) {
                    result.parameter[result.numIntersections++] = tValue;
                }
            }

            if (result.numIntersections < 2) {
                tValue = (-a1 + root) / a2;
                if (t0 <= t1) {
                    if (t0 <= tValue && tValue <= t1) {
                        result.parameter[result.numIntersections++] = tValue;
                    }
                } else {
                    if (t1 <= tValue && tValue <= t0) {
                        result.parameter[result.numIntersections++] = tValue;
                    }
                }
            }
        } else if (discr == 0) {
            const tValue = -a1 / a2;
            if (t0 <= t1) {
                if (t0 <= tValue && tValue <= t1) {
                    result.parameter[result.numIntersections++] = tValue;
                }
            } else {
                if (t1 <= tValue && tValue <= t0) {
                    result.parameter[result.numIntersections++] = tValue;
                }
            }
        }
    }

    if (result.numIntersections == 2) {
        result.intersect = true;

        if (result.parameter[0] > result.parameter[1]) {
            const tmp = result.parameter[0];
            result.parameter[0] = result.parameter[1];
            result.parameter[1] = tmp;
        }
    } else if (result.numIntersections == 1) {
        result.intersect = true;
        result.parameter[1] = result.parameter[0];
    }
}
```