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