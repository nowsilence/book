** 两条线段相交于一点（包括延长线）**

```
// Java Implementation. To find the point of 
// intersection of two lines 
  
// Class used to  used to store the X and Y 
// coordinates of a point respectively 
class Point 
{ 
    double x,y; 
      
    public Point(double x, double y)  
    { 
        this.x = x; 
        this.y = y; 
    } 
      
    // Method used to display X and Y coordinates 
    // of a point 
    static void displayPoint(Point p) 
    { 
        System.out.println("(" + p.x + ", " + p.y + ")"); 
    } 
} 
  
class Test 
{      
    static Point lineLineIntersection(Point A, Point B, Point C, Point D) 
    { 
        // Line AB represented as a1x + b1y = c1 
        double a1 = B.y - A.y; 
        double b1 = A.x - B.x; 
        double c1 = a1*(A.x) + b1*(A.y); 
       
        // Line CD represented as a2x + b2y = c2 
        double a2 = D.y - C.y; 
        double b2 = C.x - D.x; 
        double c2 = a2*(C.x)+ b2*(C.y); 
       
        double determinant = a1*b2 - a2*b1; 
       
        if (determinant == 0) 
        { a
            // The lines are parallel. This is simplified 
            // by returning a pair of FLT_MAX 
            return new Point(Double.MAX_VALUE, Double.MAX_VALUE); 
        } 
        else
        { 
            double x = (b2*c1 - b1*c2)/determinant; 
            double y = (a1*c2 - a2*c1)/determinant; 
            return new Point(x, y); 
        } 
    } 
      
    // Driver method 
    public static void main(String args[]) 
    { 
        Point A = new Point(1, 1); 
        Point B = new Point(4, 4); 
        Point C = new Point(1, 8); 
        Point D = new Point(2, 4); 
       
        Point intersection = lineLineIntersection(A, B, C, D); 
       
        if (intersection.x == Double.MAX_VALUE && 
            intersection.y == Double.MAX_VALUE) 
        { 
            System.out.println("The given lines AB and CD are parallel."); 
        } 
       
        else
        { 
            // NOTE: Further check can be applied in case 
            // of line segments. Here, we have considered AB 
            // and CD as lines 
           System.out.print("The intersection of the given lines AB " +  
                               "and CD is: "); 
           Point.displayPoint(intersection); 
        } 
    } 
} 

```

[参考](https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/)


** 点是否在线段上 **
```java
final static double EPSILON = 0.0000001;

public static boolean pointInSegment(Point p, Point p0, Point p1) {
    // 叉乘
    double cross = (p.x - p0.x) * (p1.y - p0.y) - (p1.x - p0.x) * (p.y - p0.y);

    if (Math.abs(cross) < EPSILON && 
        min(p0.x, p1.x) <= p.x && 
        p.x <= max(p0.x, p1.x) && 
        min(p0.y, p1.y) <= p.y && 
        p.y <= max(p0.y, p1.y)) {
        return true;
    }

    return false;
}
```

** 三维空间两条线段是否相交 **
```javascript

function intersectionLineSegment(p00, p01, p10, p11) {
    _v0.subVectors(p01, p00);
    _v1.subVectors(p11, p10);

    return _intersectionLineSegment(p00, _v0, p10, _v1);
}

function _intersectionLineSegment(p0, v0, p1, v1) {
    // 是否平行
    if (v0.dot(v0) == 1) return false;

    const startPointSeg = new Vector3().copy(p1).sub(p0);
    // 有向面积1
    const vs1 = new Vector3().copy(v0).cross(v1);
    // 有向面积2
    const vs2 = new Vector3().copy(startPointSeg).cross(v1);
    
    const val = startPointSeg.dot(vs1);

    const esp = 0.000001;
    // 若不共面
    if (val >= eps || val <= -eps) return false;

    const val2 = vs2.dot(vs1) / vs1.lengthSq();

    // 若交点在延长线上
    if (val2 > 1 || val2 < 0) return false;

    return p0.clone().add(v0.multiplyScalar(val2));
}
```


[参考](https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments)
```javascript
function distance(a, b, c, d, clampToLine = true) {
    let clampA = false, clampB = false, clampC = false, clampD = false;

    if (clampToLine) {
        clampA = true;
        clampB = true;
        clampC = true;
        clampD = true;
    }

    const ab = b.clone().sub(a);
    const cd = d.clone().sub(c);

    const _ab = ab.clone().normalize();
    const _cd = cd.clone().normalize();

    const cross = _ab.clone().cross(_cd);
    const denom = Math.pow(cross.length, 2);

    // 平行
    if (denom == 0) {
        const d0 = _ab.dot(c.clone().sub(a));
        const dis = _ab.clone().multiplyScalar(d0).add(a).sub(c).length();

        if (clampA || clampB || clampC || clampD) {
            const d1 = _ab.dot(d.clone().sub(a));

            if (d0 <= 0 && d1 <= 0) {
                if (clampA && clampD) {
                    if (Math.abs(d0) < Math.abs(d1)) {
                        return [c, a, c.clone().sub(a).length()];
                    }
                    return [d, a, d.clone().sub(a).lenght()];
                }
            } else if (d0 >= ab.length() && d1 >= ab.length()) {
                if (clampB && clampC) {
                    return [c, b, c.clone().sub(b).length()];
                }
                return [d, b, d.clone().sub(b).length()];
            }
        }

        return [null, null, dis];
    }

    const t = c.clone().sub(a);

    const matrix = new Matrix3();
    const det0 = matrix.fromArray([...t.toArray(), ..._cd.toArray(), ...cross.toArray()]).determinant();
    const det1 = matrix.fromArray([...t.toArray(), ..._ab.toArray(), ...cross.toArray()]).determinant();

    const t0 = det0 / denom;
    const t1 = det1 / denom;

    let pab = _ab.clone().multiplyScalar(t0).add(a);
    let pcd = _cd.clone().multiplyScalar(t1).add(c);

    if (clampA || clampB || clampC || clampD) {
        if (t0 < 0 && clampA) {
            pab = a;
        } else if (t0 > ab.length() && clampB) {
            pab = b;
        }

        if (t1 < 0 && clampC) {
            pcd = c;
        } else if (t1 > cd.length() && clampD) {
            pcd = d;
        }
    }

    const dis = pab.sub(pcd).length();

    return [pab, pcd, dis];
}
```

```javascript
function distance(P0, P1, Q0, Q1) {
    const P1mP0 = P1.clone().sub(P0);
    const Q1mQ0 = Q1.clone().sub(Q0);
    const P0mQ0 = P0.clone().sub(Q0);

    const a = P1mP0.dot(P1mP0);
    const b = P1mP0.dot(Q1mQ0);
    const c = Q1mQ0.dot(Q1mQ0);
    const d = P1mP0.dot(P0mQ0);
    const e = Q1mQ0.dot(P0mQ0);
    const det = a * c - b * b;

    let s, t, nd, bmd, bte, ctd, bpe, ate, btd;

    const zero = 0;
    const one = 1;

    if (det > 0) {

        bte = b * e;
        ctd = c * d;

        if (bte <= ctd) { // s <= 0
            s = 0;
            if (e <= 0) { // t <= 0
                // region 6
                t = 0;
                nd = -d;
                if (nd >= a) {
                    s = 1;
                } else if (nd > 0) {
                    s = nd / a;
                }
                // else: s is already zero
            } else if (e < c) { // 0 < t < 1
                // region 5
                t = e / c;
            } else { // t >= 1
                // region 4
                t = 1;
                bmd = b - d;
                if (bmd >= a) {
                    s = 0;
                } else if (bmd > 0) {
                    s = bmd / a;
                } 
                // else: s is already zero
            }
        } else { // s > 0
            s = bte - ctd;
            if (s >= det) { // s >= 1
                // s = 1;
                s = 1;
                bpe = b + e;
                if (bpe <= 0) { // t <= 0
                    // region 8
                    t = 0;
                    nd = -d;
                    if (nd <= 0) {
                        s = 0;
                    } else if (nd < a) {
                        s = nd / a;
                    }
                    // else: s is already one
                } else if (bpe < c) { // 0 < t < 1
                    // region 1
                    t = bpe / c;
                } else { // t >= 1
                    // region 2
                    t = 1;
                    bmd = b - d;
                    if (bmd <= 0) {
                        s = 0;
                    } else if (bmd < a) {
                        s = bmd / a;
                    }
                    // else: s is already one
                }
            } else { // 0 < s < 1
                ate = a * e;
                btd = b * d;
                if (ate <= btd) { // t <= 0
                    // region 7
                    t = 0;
                    nd = -d;
                    if (nd <= 0) {
                        s = 0;
                    } else if (nd >= a) {
                        s = 1;
                    } else {
                        s = nd / a;
                    }
                } else { // t > 0
                    t = ate - btd;
                    if (t >= det) { // t >= 1
                        // region 3
                        t = one;
                        bmd = b - d;
                        if (bmd <= zero)
                        {
                            s = zero;
                        }
                        else if (bmd >= a)
                        {
                            s = one;
                        }
                        else
                        {
                            s = bmd / a;
                        }
                    } else { // 0 < t < 1
                        // region 0
                        s /= det;
                        t /= det;
                    }
                }
            }
        }
    } else {
        // The segments are parallel. The quadratic factors to
        //   R(s,t) = a*(s-(b/a)*t)^2 + 2*d*(s - (b/a)*t) + f
        // where a*c = b^2, e = b*d/a, f = |P0-Q0|^2, and b is not
        // zero. R is constant along lines of the form s-(b/a)*t = k
        // and its occurs on the line a*s - b*t + d = 0. This line
        // must intersect both the s-axis and the t-axis because 'a'
        // and 'b' are not zero. Because of parallelism, the line is
        // also represented by -b*s + c*t - e = 0.
        //
        // The code determines an edge of the domain [0,1]^2 that
        // intersects the minimum line, or if none of the edges
        // intersect, it determines the closest corner to the minimum
        // line. The conditionals are designed to test first for
        // intersection with the t-axis (s = 0) using
        // -b*s + c*t - e = 0 and then with the s-axis (t = 0) using
        // a*s - b*t + d = 0.

        // When s = 0, solve c*t - e = 0 (t = e/c).
        if (e <= 0)  // t <= 0
        {
            // Now solve a*s - b*t + d = 0 for t = 0 (s = -d/a).
            t = 0;
            nd = -d;
            if (nd <= 0)  // s <= 0
            {
                // region 6
                s = 0;
            }
            else if (nd >= a)  // s >= 1
            {
                // region 8
                s = 1;
            }
            else  // 0 < s < 1
            {
                // region 7
                s = nd / a;
            }
        }
        else if (e >= c)  // t >= 1
        {
            // Now solve a*s - b*t + d = 0 for t = 1 (s = (b-d)/a).
            t = 1;
            bmd = b - d;
            if (bmd <= 0)  // s <= 0
            {
                // region 4
                s = 0;
            }
            else if (bmd >= a)  // s >= 1
            {
                // region 2
                s = 1;
            }
            else  // 0 < s < 1
            {
                // region 3
                s = bmd / a;
            }
        }
        else  // 0 < t < 1
        {
            // The point (0,e/c) is on the line and domain, so we have
            // one point at which R is a minimum.
            s = 0;
            t = e / c;
        }
    }


    const result = {
        parameter: [s, t],
        closest: [P0.clone().add(P1mP0.multiplyScalar(s)), Q0.clone().add(Q1mQ0.multiplyScalar(t))]
    };

    const diff = result.closest[0].clone().sub(result.closest[1]);
    result.sqrDistance = diff.dot(diff);
    result.distance = Math.sqrt(result.sqrDistance);

    return result;
}

function isPointOnSegment(p0, p1, p0) {
    const ab = p1.clone().sub(p0);
    const ac = p.clone().sub(p);

    if (ab.clone().cross(ac).length() != 0) {
        return -1;
    } else

    const kac = ab.dot(ac);

    if (kac < 0) {
        return -1;
    }  if (kac == 0) {
        return 0;
    }

    const kab = ab.dot(ab);

    if (kac > kab) {
        return -1;
    } else if (kac == kab) {
        return 1;
    }

    return Math.sqrt(kac) / Math.sqrt(kab);
}
```