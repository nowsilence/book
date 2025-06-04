
## Voronoi图法（最常用）##
更精确，但计算复杂
```javascript
import { Delaunay } from 'd3-delaunay';

/**
 * 使用Voronoi图提取多边形骨架线
 * @param {Array} polygon 多边形顶点坐标 [[x,y], [x,y], ...]
 * @param {number} density 采样密度（0-1）
 * @returns {Array} 骨架线坐标 [[x,y], ...]
 */
function extractSkeletonVoronoi(polygon, density = 0.05) {
    // 1. 在多边形内部生成密集采样点
    const points = samplePolygonPoints(polygon, density);
    
    // 2. 计算这些点的Voronoi图
    const delaunay = Delaunay.from(points.map(p => [p.x, p.y]));
    const voronoi = delaunay.voronoi([0, 0, 1000, 1000]); // 替换为你的边界
    
    // 3. 提取Voronoi边作为骨架候选
    const skeletonEdges = [];
    const { cells } = voronoi;
    
    for (let i = 0; i < cells.length; i++) {
        const cell = cells[i];
        for (let j = 0; j < cell.length; j++) {
            const edge = [cell[j], cell[(j + 1) % cell.length]];
            skeletonEdges.push(edge);
        }
    }
    
    // 4. 过滤保留完全在多边形内部的边
    const filteredEdges = skeletonEdges.filter(edge => {
        const midpoint = [
            (edge[0][0] + edge[1][0]) / 2,
            (edge[0][1] + edge[1][1]) / 2
        ];
        return pointInPolygon(midpoint, polygon);
    });
    
    return filteredEdges;
}

// 在多边形内部生成均匀采样点
function samplePolygonPoints(polygon, density) {
    const points = [];
    const bbox = getBoundingBox(polygon);
    
    // 简单网格采样
    const xStep = (bbox.maxX - bbox.minX) * density;
    const yStep = (bbox.maxY - bbox.minY) * density;
    
    for (let x = bbox.minX; x <= bbox.maxX; x += xStep) {
        for (let y = bbox.minY; y <= bbox.maxY; y += yStep) {
            if (pointInPolygon([x, y], polygon)) {
                points.push({ x, y });
            }
        }
    }
    
    return points;
}

// 判断点是否在多边形内（射线法）
function pointInPolygon(point, polygon) {
    const [x, y] = point;
    let inside = false;
    
    for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
        const [xi, yi] = polygon[i];
        const [xj, yj] = polygon[j];
        
        const intersect = ((yi > y) !== (yj > y)) &&
            (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
        if (intersect) inside = !inside;
    }
    
    return inside;
}

// 计算多边形包围盒
function getBoundingBox(polygon) {
    let minX = Infinity, minY = Infinity;
    let maxX = -Infinity, maxY = -Infinity;
    
    for (const [x, y] of polygon) {
        minX = Math.min(minX, x);
        minY = Math.min(minY, y);
        maxX = Math.max(maxX, x);
        maxY = Math.max(maxY, y);
    }
    
    return { minX, minY, maxX, maxY };
}
```

## 拓扑细化算法（Thinning Algorithm） ##
细化算法实现简单但对噪声敏感

```javascript
/**
 * 使用Zhang-Suen细化算法提取骨架
 * @param {Array} polygon 多边形坐标
 * @param {number} width 栅格化宽度
 * @param {number} height 栅格化高度
 * @returns {Array} 骨架点坐标
 */
function extractSkeletonThinning(polygon, width = 100, height = 100) {
    // 1. 将多边形栅格化为二值图像
    const grid = rasterizePolygon(polygon, width, height);
    
    // 2. 应用细化算法
    let changed;
    do {
        changed = false;
        // 第一子迭代
        changed |= zhangSuenIteration(grid, 1);
        // 第二子迭代
        changed |= zhangSuenIteration(grid, 2);
    } while (changed);
    
    // 3. 将骨架像素转换回坐标
    return extractSkeletonPoints(grid, polygon, width, height);
}

// 栅格化多边形为二值网格
function rasterizePolygon(polygon, width, height) {
    const grid = Array(height).fill().map(() => Array(width).fill(0));
    const bbox = getBoundingBox(polygon);
    
    const scaleX = width / (bbox.maxX - bbox.minX);
    const scaleY = height / (bbox.maxY - bbox.minY);
    
    // 简单扫描线填充算法
    for (let y = 0; y < height; y++) {
        const realY = bbox.minY + y / scaleY;
        const intersections = [];
        
        // 找出所有边与扫描线的交点
        for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
            const [xi, yi] = polygon[i];
            const [xj, yj] = polygon[j];
            
            if ((yi <= realY && yj > realY) || (yj <= realY && yi > realY)) {
                const x = xi + (realY - yi) * (xj - xi) / (yj - yi);
                intersections.push(x);
            }
        }
        
        // 排序交点并填充
        intersections.sort((a, b) => a - b);
        for (let i = 0; i < intersections.length; i += 2) {
            const x1 = Math.floor((intersections[i] - bbox.minX) * scaleX);
            const x2 = Math.ceil((intersections[i + 1] - bbox.minX) * scaleX);
            
            for (let x = x1; x <= x2 && x < width; x++) {
                grid[y][x] = 1;
            }
        }
    }
    
    return grid;
}

// Zhang-Suen细化算法的一次迭代
function zhangSuenIteration(grid, subiteration) {
    const toRemove = [];
    const height = grid.length;
    const width = grid[0].length;
    
    for (let y = 1; y < height - 1; y++) {
        for (let x = 1; x < width - 1; x++) {
            if (grid[y][x] !== 1) continue;
            
            // 获取8邻域
            const neighbors = [
                grid[y-1][x], grid[y-1][x+1], grid[y][x+1], grid[y+1][x+1],
                grid[y+1][x], grid[y+1][x-1], grid[y][x-1], grid[y-1][x-1]
            ];
            
            // 条件1: 2 ≤ B(P1) ≤ 6
            const B = neighbors.filter(v => v === 1).length;
            if (B < 2 || B > 6) continue;
            
            // 条件2: A(P1) = 1
            let A = 0;
            for (let i = 0; i < 8; i++) {
                if (neighbors[i] === 0 && neighbors[(i + 1) % 8] === 1) {
                    A++;
                }
            }
            if (A !== 1) continue;
            
            // 子迭代特定条件
            if (subiteration === 1) {
                // 条件3: P2 * P4 * P6 = 0
                // 条件4: P4 * P6 * P8 = 0
                if (neighbors[1] * neighbors[3] * neighbors[5] !== 0) continue;
                if (neighbors[3] * neighbors[5] * neighbors[7] !== 0) continue;
            } else {
                // 条件3: P2 * P4 * P8 = 0
                // 条件4: P2 * P6 * P8 = 0
                if (neighbors[1] * neighbors[3] * neighbors[7] !== 0) continue;
                if (neighbors[1] * neighbors[5] * neighbors[7] !== 0) continue;
            }
            
            toRemove.push([y, x]);
        }
    }
    
    // 移除标记的点
    toRemove.forEach(([y, x]) => grid[y][x] = 0);
    return toRemove.length > 0;
}

// 从细化后的网格提取骨架点
function extractSkeletonPoints(grid, originalPolygon, width, height) {
    const points = [];
    const bbox = getBoundingBox(originalPolygon);
    
    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            if (grid[y][x] === 1) {
                const realX = bbox.minX + x / width * (bbox.maxX - bbox.minX);
                const realY = bbox.minY + y / height * (bbox.maxY - bbox.minY);
                points.push([realX, realY]);
            }
        }
    }
    
    return points;
}
```
## 基于距离变换的骨架提取 ##

稳健但需要栅格化处理
```javascript
/**
 * 基于距离变换的骨架提取
 * @param {Array} polygon 多边形坐标
 * @param {number} width 栅格宽度
 * @param {number} height 栅格高度
 * @returns {Array} 骨架点坐标
 */
function extractSkeletonDistanceTransform(polygon, width = 100, height = 100) {
    // 1. 栅格化多边形
    const grid = rasterizePolygon(polygon, width, height);
    
    // 2. 计算距离变换
    const distanceMap = computeDistanceTransform(grid);
    
    // 3. 提取局部最大值作为骨架
    return extractRidgePoints(distanceMap, polygon, width, height);
}

// 计算距离变换（欧几里得距离）
function computeDistanceTransform(grid) {
    const height = grid.length;
    const width = grid[0].length;
    const distances = Array(height).fill().map(() => Array(width).fill(Infinity));
    
    // 第一遍：从左到右，从上到下
    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            if (grid[y][x] === 1) {
                distances[y][x] = 0;
            } else {
                const candidates = [];
                if (y > 0) candidates.push(distances[y-1][x] + 1);
                if (x > 0) candidates.push(distances[y][x-1] + 1);
                if (y > 0 && x > 0) candidates.push(distances[y-1][x-1] + Math.SQRT2);
                if (candidates.length > 0) {
                    distances[y][x] = Math.min(...candidates);
                }
            }
        }
    }
    
    // 第二遍：从右到左，从下到上
    for (let y = height - 1; y >= 0; y--) {
        for (let x = width - 1; x >= 0; x--) {
            const candidates = [distances[y][x]];
            if (y < height - 1) candidates.push(distances[y+1][x] + 1);
            if (x < width - 1) candidates.push(distances[y][x+1] + 1);
            if (y < height - 1 && x < width - 1) candidates.push(distances[y+1][x+1] + Math.SQRT2);
            distances[y][x] = Math.min(...candidates);
        }
    }
    
    return distances;
}

// 提取距离变换的脊线点（骨架）
function extractRidgePoints(distanceMap, originalPolygon, width, height) {
    const ridgePoints = [];
    const bbox = getBoundingBox(originalPolygon);
    
    for (let y = 1; y < height - 1; y++) {
        for (let x = 1; x < width - 1; x++) {
            const center = distanceMap[y][x];
            if (center === 0) continue;
            
            // 检查是否是局部最大值
            let isRidge = true;
            for (let ny = y - 1; ny <= y + 1 && isRidge; ny++) {
                for (let nx = x - 1; nx <= x + 1 && isRidge; nx++) {
                    if ((ny !== y || nx !== x) && distanceMap[ny][nx] > center) {
                        isRidge = false;
                    }
                }
            }
            
            if (isRidge) {
                const realX = bbox.minX + x / width * (bbox.maxX - bbox.minX);
                const realY = bbox.minY + y / height * (bbox.maxY - bbox.minY);
                ridgePoints.push([realX, realY]);
            }
        }
    }
    
    return ridgePoints;
}
```