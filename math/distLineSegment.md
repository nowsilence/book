```javascript

const vectorTemp0 = new THREE.Vector3();
const vectorTemp1 = new THREE.Vector3();

function distLineSegment({ origin, direction} = Line, { start, end } = segment, pointOnLine, pointOnSegment) {

    const segDirection = vectorTemp0.copy(end).sub(start);
    const diff = vectorTemp1.copy(origin).sub(start);
    const a00 = direction.dot(direction);
    const a01 = -direction.dot(segDirection);
    const a11 = segDirection.dot(segDirection);
    const b0 = direction.dot(diff);
    const det = Math.max(a00 * a11 - a01 * a01, 0);

    let s0, s1;

    if (det > 0) {
        // The line and segment are not parallel.
        const b1 = -segDirection.dot(diff);
        s1 = a01 * b0 - a00 * b1;

        if (s1 >= 0) {
            if (s1 <= det) {
                // Two interior points are closest, one on the line
                // and one on the segment.
                s0 = (a01 * b1 - a11 * b0) / det;
                s1 /= det;
            } else {
                // The endpoint Q1 of the segment and an interior
                // point of the line are closest.
                s0 = -(a01 + b0) / a00;
                s1 = 1;
            }
        } else {
            // The endpoint Q0 of the segment and an interior point
            // of the line are closest.
            s0 = -b0 / a00;
            s1 = 0;
        }
    } else {
        // The line and segment are parallel. Select the pair of
        // closest points where the closest segment point is the
        // endpoint Q0.
        s0 = -b0 / a00;
        s1 = 0;
    }

    vectorTemp1.copy(direction).multiplyScalar(s0).add(origin);
    vectorTemp0.multiplyScalar(s1).add(start);

    if (pointOnLine) {
        pointOnLine.copy(vectorTemp1);
    }

    if (pointOnSegment) {
        pointOnSegment.copy(vectorTemp0);
    }

    return vectorTemp0.distanceTo(vectorTemp1);
}
```