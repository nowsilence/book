Voronoi Diagram 
Voronoi图又称泰森多边形，维诺图/沃罗诺伊图

Voronoi图 被称为 泰森多边形 是因为其命名来源于荷兰气候学家A•H•Thiessen。‌他在1911年提出了一种方法，通过将所有相邻气象站连成三角形，并作这些三角形各边的垂直平分线，每个气象站周围的若干垂直平分线围成一个多边形。这个多边形内所包含的一个唯一气象站的降雨强度被用来表示这个多边形区域内的降雨强度，因此这个多边形被称为泰森多边形‌

是一种基于离散点集的空间划分方法。每个区域内的点到其对应控制点的距离比到其他控制点更近，边界由相邻控制点连线的垂直平分线构成。
广泛应用于地理信息系统（如服务区划分）、计算机图形学（如自然纹理生成）、机器人路径规划、生物学（如细胞结构模拟）等领域。其核心优势在于高效的空间分割能力和对偶性（与Delaunay三角剖分互为对偶）。

或者可以用来生成道路中心线

d3-voronoi库
[参考](https://zhuanlan.zhihu.com/p/1894662718138591127)
[参考](https://zhuanlan.zhihu.com/p/27084187348)
```javascript
const polygon = [];
// 这里为polygon外包矩形的最大值最小值, d3默认精度是小数点6位，如果精度不够需要自行缩放处理
const voronoi = d3.voronoi().extent([[minx, miny], [maxx, maxy]]);
const diagram = voronoi(polygon);
diagram.links().forEach(it => {
    // 这里是三角刨分后的三角形的边，点为polygon的形状点
});

diagram.edges.forEach(it => {
    // 这里为cel的一条边，it[0], it[1]
});

diagram.cells.forEach(cell => {
    /**
     * 这个是一个cell，
     * cell.halfedges为cell的边，里面是整型数组，值为diagram.edges的索引
     * cell.site为cell包含的点（polygon的形状点）
     * 
     * */
})

diagram.polygons().forEach(p => {
    // p代表着组成一个cell的所有点，diagram.polygons()[n]对应diagram.cells[n]
});
```