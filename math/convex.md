## Graham Scan 算法计算凸包 ##
```javascript
/**
 * Graham Scan 算法计算凸包
 * @param {Array} points - 点集，格式为 [{x: number, y: number}, ...]
 * @returns {Array} 凸包顶点数组，按逆时针顺序排列
 */
function convexHullGrahamScan(points) {
    if (points.length < 3) return points;
    
    // 找到y坐标最小的点（如果y相同则取x较小的）
    let pivot = points[0];
    for (const p of points) {
        if (p.y < pivot.y || (p.y === pivot.y && p.x < pivot.x)) {
            pivot = p;
        }
    }
    
    // 按极角排序
    const sorted = [...points].sort((a, b) => {
        const angleA = Math.atan2(a.y - pivot.y, a.x - pivot.x);
        const angleB = Math.atan2(b.y - pivot.y, b.x - pivot.x);
        if (angleA < angleB) return -1;
        if (angleA > angleB) return 1;
        // 如果角度相同，按距离排序
        const distA = (a.x - pivot.x) ** 2 + (a.y - pivot.y) ** 2;
        const distB = (b.x - pivot.x) ** 2 + (b.y - pivot.y) ** 2;
        return distA - distB;
    });
    
    const stack = [sorted[0], sorted[1]];
    
    for (let i = 2; i < sorted.length; i++) {
        let top = stack[stack.length - 1];
        let nextToTop = stack[stack.length - 2];
        
        // 当新点导致右转时，弹出栈顶点
        while (
            stack.length > 1 && 
            crossProduct(nextToTop, top, sorted[i]) <= 0
        ) {
            stack.pop();
            top = stack[stack.length - 1];
            nextToTop = stack[stack.length - 2];
        }
        stack.push(sorted[i]);
    }
    
    return stack;
}

// 计算叉积 (b-a) × (c-a)
function crossProduct(a, b, c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}
```


## Andrew's Monotone Chain 算法计算凸包 ##
```javascript
/**
 * Andrew's Monotone Chain 算法计算凸包
 * @param {Array} points - 点集
 * @returns {Array} 凸包顶点数组，按逆时针顺序排列
 */
function convexHullMonotoneChain(points) {
    if (points.length <= 1) return points;
    
    // 按x坐标排序（x相同则按y排序）
    points.sort((a, b) => a.x - b.x || a.y - b.y);
    
    const lower = [];
    for (const p of points) {
        while (
            lower.length >= 2 && 
            crossProduct(lower[lower.length - 2], lower[lower.length - 1], p) <= 0
        ) {
            lower.pop();
        }
        lower.push(p);
    }
    
    const upper = [];
    for (let i = points.length - 1; i >= 0; i--) {
        const p = points[i];
        while (
            upper.length >= 2 && 
            crossProduct(upper[upper.length - 2], upper[upper.length - 1], p) <= 0
        ) {
            upper.pop();
        }
        upper.push(p);
    }
    
    lower.pop();
    upper.pop();
    return lower.concat(upper);
}

```
## Jarvis March 算法计算凸包 ##

```javascript
/**
 * Jarvis March 算法计算凸包
 * @param {Array} points - 点集
 * @returns {Array} 凸包顶点数组
 */
function convexHullJarvisMarch(points) {
    if (points.length < 3) return points;
    
    const hull = [];
    // 找到最左边的点作为起点
    let leftmost = 0;
    for (let i = 1; i < points.length; i++) {
        if (points[i].x < points[leftmost].x) {
            leftmost = i;
        }
    }
    
    let p = leftmost, q;
    do {
        hull.push(points[p]);
        q = (p + 1) % points.length;
        
        for (let i = 0; i < points.length; i++) {
            // 如果i在pq的逆时针方向，则更新q
            if (crossProduct(points[p], points[q], points[i]) < 0) {
                q = i;
            }
        }
        p = q;
    } while (p !== leftmost);
    
    return hull;
}
```

## 算法比较 ##
Graham Scan:

时间复杂度: O(n log n)（主要来自排序）

适合中等规模的点集

Andrew's Monotone Chain:

时间复杂度: O(n log n)

实现简单，性能稳定

Jarvis March:

时间复杂度: O(nh)，h为凸包顶点数

当h较小时效率高，适合凸包顶点很少的情况

在实际应用中，Monotone Chain算法通常是较好的选择，因为它实现简单且性能稳定