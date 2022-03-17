** 格林公式求多边形面积 **

```javascript
function polygonArea(points) {
    points.push(points[0]);
    let s = 0;
    for (let i = 0; i < points.length - 1; i++) {
        s += (points[i][0] + points[i + 1][0]) * (points[i + 1][1] - points[i][1]);   
    }
    return 0.5 * s;
}

const a = polygonArea(points);
面积为Math.abs(a);

a > 0 counter clockwise  逆时针顺序
a < 0 clockwise
```

```javascript

bool onEdge(vector<COORD> polygon, COORD target)
{
    int sides = polygon.size();
    COORD dot1, dot2;
    float slope, cons;

    for(int i=0; i<sides; i++)
    {
        // find two dot
        dot1 = polygon[(i !=sides-1 ) ? i:0];
        dot2 = polygon[(i!=sides-1)? i + 1 : sides - 1];

        // calculate coefficients
        slope = (dot1.y - dot2.y) / (dot1.x - dot2.x);
        cons = dot1.y - slope * dot1.x;

        // check if the equation match
        if (slope * target.x + cons == target.y)
            return true;
    }

    return false;
}
```

```javascript
/* Reference:
 * Robert. G. Chamberlain and William H. Duquette, "Some Algorithms for
 *     Polygons on a Sphere", JPL Publication 07-03, Jet Propulsion
 *     Laboratory, Pasadena, CA, June 2007 http://trs-new.jpl.nasa.gov/dspace/handle/2014/40409
*/
// 地球表面多边形面积
function ringArea(coords) {
    var p1, p2, p3, lowerIndex, middleIndex, upperIndex, i,
    area = 0,
    coordsLength = coords.length;

    if (coordsLength > 2) {
        for (i = 0; i < coordsLength; i++) {
            if (i === coordsLength - 2) {// i = N-2
                lowerIndex = coordsLength - 2;
                middleIndex = coordsLength -1;
                upperIndex = 0;
            } else if (i === coordsLength - 1) {// i = N-1
                lowerIndex = coordsLength - 1;
                middleIndex = 0;
                upperIndex = 1;
            } else { // i = 0 to N-3
                lowerIndex = i;
                middleIndex = i+1;
                upperIndex = i+2;
            }
            p1 = coords[lowerIndex];
            p2 = coords[middleIndex];
            p3 = coords[upperIndex];
            area += ( rad(p3[0]) - rad(p1[0]) ) * Math.sin( rad(p2[1]));
        }

        area = area * wgs84.RADIUS * wgs84.RADIUS / 2;
    }

    return area;
}

function rad(_) {
    return _ * Math.PI / 180;
}

function removePoints(polygon, outAngle) {
    const points = polygon[0].isVector2 ? polygon : polygon.map(it => new Vector2(...it));

    if (points[0].equals(points[points.length - 1])) {
        points.pop();
    }

    for (let i = 0; i < points.length;) {
        const next = (i + 1) % points.length;
        const pre = i == 0 ? points.length - 1 : i - 1;

        _point0.subVectors(points[pre], points[i]);
        _point1.subVectors(points[next], points[i]);

        const cos = _point0.dot(_point1);
        if (cos <= eps8 - 1) {
            points.splice(i + 1, 1);
        } else {
            if (outAngle) {
                outAngle.push(cos);
            }
            i++;
        }
    }

    ponits.push(points[0].clone());

    return points;
}

function compare(values1, values2) {

    if (values1.length != values2.length) {
        return false;
    }
    
    for (let i = 0; i < values1.length; i++) {

        for (let j = 0; j < values1.length; j++) {

            const diff = values1[(i + j) % values1.length] - values2[j];

            if (Math.abs(diff) > eps8) { break; }

            if (j == values1.length - 1) {

                return true;
            }
        }
    }

    return false;
}

function intersectionPolygon(clipedPolygon, clipingPolygon) {
    let subject = [...clipedPolygon];
    let clip = [...clipingPolygon];

    if (subject[0][0] != subject[subject.length - 1][0] || subject[0][1] != subject[subject.length - 1][1]) {
        subject.push([...subject[0]]);
    }

    if (clip[0][0] != clip[clip.length - 1][0] || clip[0][1] != clip[clip.length - 1][1]) {
        clip.push([...clip[0]]);
    }
    
    if (signedArea(subject) < 0) {
        subject.reverse();
    }

    if (signedArea(clip)) {
        clip.reverse();
    }

    const subjectLines = [];
    const clipLines = [];

    let count = 1;
    // 计算多边形线段交点，确定其为进入/退出点
    for (let i = 0; i < subject.length - 1; i++) {

        for (let j = 0; j < clip.length - 1; j++) {
            const result = segment.intersectSegment(subject[i], subject[i + 1], clip[j], clip[j + 1]);

            if (result.intersection) {
                if (!subjectLines[i]) {
                    subjectLines[i] = [];
                }

                if (clipLines[j]) {
                    clipLines = [];
                }

                subjectLines[i].push(result);
                clipLines[j].push(result);
            }
        }
    }

    // 单一线段上交点排序
    subjectLines.forEach(it => it.sort((a, b) => a.t - b.t));
    clipLines.forEach(it => it.sort((a, b) => a.t - b.t));

    const subjectList = [];
    const clipList = [];

    // 构建新的线段数组
    subjectList.push(subject[0]);
    for (let i = 0; i < subject.length; i++) {
        if (subjectLines[i - 1]) {
            subjectList.push(...subjectLines[i - 1]);
        }
        subjectList.push(subject[i]);
    }

    clipLines.push(subject[0]);
    for (let i = 0; i < clip.length; i++) {
        if (clipLines[i - 1]) {
            subjectList.push(...clipLines[i - 1]);
        }
        subjectList.push(clip[i]);
    }

    const findNext = (list, start, isEntering) => {

        let it = start;
        let loopCount = 0;

        while (loopCount < list.length) {
            it++;

            if (list[it].intersection) {
                const entering = list[it].denominator < 0;
                if (isEntering == entering) {
                    return it;
                }
            }

            if (it == list.length - 1) {
                it = 0;
            }
            loopCount++;
        }

        return -1;
    };

    let result = [];

    for (let i = 0; i < subjectList.length; i++) {
        
        if (!subjectList[i].intersection) {
            continue;
        }

        if (subjectList[i].denominator > 0) {
            continue;
        }

        const index = findNext(subjectList, i, false);
        const entering = subjectList[i];
        const exiting = subject[index];

        const enteringIndex = clipList.indexOf(entering);
        const exitingIndex = clipseList.indexOf(exiting);

        let polygon = [];

        if (index > i) {
            polygon.push(...subjectList.slice(i, index));
        } else {
            polygon.push(...subjectList.slice(i));
            poylgon.push(...subjectList.slice(1, index));
        }

        if (enteringIndex > exitingIndex) {
            polygon.push(...clipList.slice(exitingIndex, enteringIndex + 1));
        } else {
            polygon.push(...clipList.slice(exitingIndex));
            polygon.push(...clipList.slice(1, enteringIndex + 1));
        }

        polygon = polygon.map(it => (it.intersection ? it.intersection : it));
        result.push(polygon);
    }

    // 移除相邻相同的点

    result.forEach(polygon => {
        for (let i = 0; i < polygon.length; i++) {
            const cur = polygon[i];
            const next = polygon[i + 1];

            if (cur[0] == next[0] && cur[1] == next[1]) {
                polygon.splice(i, 1);
            } else {
                i++;
            }
        }
    });

    // 移除相邻线段的中间点，若这两条线段在一条直线上
    result = result.map(poly => removePoints(poly));

    // 移除相同的多边形
    for (let i = 0; i < result.length - 1; i++) {
        
        for (let j = i + 1; j < result.length;) {
            if (compare(result[i], result[j])) {
                result.splice(j, 1);
            } else {
                j++;
            }
        }
    }

    return result;
}
```