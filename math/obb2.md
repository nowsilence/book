import * as THREE from 'three';
import { isCollinear } from './geom/segment';
import { Vector2 } from 'three';
import { convexHull } from './util';

/**
 * 计算中心点
 * @param {*} points 
 * @returns 
 */
function computeCentroid(points) {
    const v = points[0].clone();
    const len = points.length;
    for (let i = 1; i < len; i++) {
        v.add(points[i]);
    }

    return v.divideScalar(len);
}

/**
 * 计算方差
 * @param {*} points 
 * @returns 
 */
function computeCoVariance(points) {
    const array = [[0, 0], [0, 0]];
    
    const count = points.length;
    for (let i = 0; i < count; i++) {
        array[0][0] += points[i].x * points[i].x;
        array[0][1] += points[i].x * points[i].y;

        array[1][0] = array[0][1];
        array[1][1] += points[i].y * points[i].y;
    }
    array[0][0] /= count;
    array[0][1] /= count;
    array[1][0] /= count;
    array[1][1] /= count;

    return array;
}

/**
 * 计算姿态
 * @param {*} covarianceMatrix 
 * @returns 
 */
function computeOrientation(covarianceMatrix) {
    const targetVector = new THREE.Vector2();
    if (covarianceMatrix[0][1] == 0 || covarianceMatrix[1][0] == 0) {
        targetVector.x = 1;
        targetVector.y = 0;
        return targetVector;
    }

    const a = -covarianceMatrix[0][0] - covarianceMatrix[1][1];
    const b = covarianceMatrix[0][0] * covarianceMatrix[1][1] - covarianceMatrix[0][1] * covarianceMatrix[1][0];
    const value = a / 2;
    const rightside = Math.sqrt(Math.pow(value, 2) - b);
    const lambda1 = -value + rightside;
    const lambda2 = -value - rightside;
    if (lambda1 == lambda2) {
        targetVector.x = 0;
        targetVector.y = 0;
    } else {
        const lambda = lambda1 > lambda2 ? lambda1 : lambda2;
        targetVector.x = 1;
        targetVector.y = (lambda - covarianceMatrix[0][0]) / covarianceMatrix[0][1];
    }
    return targetVector;
}

/**
 * 旋转
 * @param {*} points 
 * @param {*} angle 
 * @returns 
 */
function rotate(points, angle) {
    const cos = Math.cos(angle);
    const sin = Math.sin(angle);
    const size = points.length;
    for (let i = 0; i < size; i += 2) {
        const x = points[i].x * cos - points[i].y * sin;
        const y = points[i].x * sin + points[i].y * cos;
        points[i].x = x;
        points[i].y = y;
    }
    return points;
}

/**
 * 二维有向包围盒
 */
export default class OBB2 {

    /**
     * 
     * @param {*} center 
     * @param {*} halfAxes 
     */
    constructor(center, halfAxes) {
        this.center = center || new THREE.Vector2();
        this.halfAxes = halfAxes || new THREE.Matrix3();
    }

    /**
     * 包围盒的角点
     * @returns 
     */
    getVertices() {
        const points = [
            new THREE.Vector2(-1, -1),
            new THREE.Vector2(1, -1),
            new THREE.Vector2(1, 1),
            new THREE.Vector2(-1, 1),
        ];

        points.forEach(it => it.applyMatrix3(this.halfAxes).add(this.center));

        return points;
    }
}

/**
 * 
 * @param {*} _points 
 * @param {*} pmin 
 * @param {*} pmax 
 * @param {*} evec 
 */
function fromPoints_getMax(_points, pmin, pmax, evec) {
    
    for (let i = 1; i < _points.length; ++i) {
        
        for (let j = 0; j < 2; ++j) {
        
            const dot = _points[i].dot(evec[j]);
            
            if (dot < pmin.getComponent(j)) {
                pmin.setComponent(j, dot);
            }
            else if (dot > pmax.getComponent(j)) {
                pmax.setComponent(j, dot);
            }
        }
    }
}

/**
 * 从一堆点计算obb
 * @param {*} points 
 * @returns 
 */
OBB2.fromPoints = (points) => {

    if (!points || points.length == 0) {
        return null;
    }

    const _points = points.map(it => (Array.isArray(it) ? new THREE.Vector2(...it) : new THREE.Vector2(it.x, it.y)));
  

    const centroid = computeCentroid(_points);

    for (const pos of _points) {
        pos.sub(centroid);
    }

    const cov = computeCoVariance(_points);
    const a00 = cov[0][0];
    const a01 = cov[0][1];
    const a11 = cov[1][1];
    const zero = 0;
    const one = 1;
    const half = 0.5;
    let c2 = half * (a00 - a11);
    let s2 = a01;

    const maxAbsComp = Math.max(Math.abs(c2), Math.abs(s2));

    if (maxAbsComp > zero) {
        c2 /= maxAbsComp;
        s2 /= maxAbsComp;
        const length = Math.sqrt(c2 * c2 + s2 * s2);
        c2 /= length;
        s2 /= length;

        if (c2 > zero) {
            c2 = -c2;
            s2 = -s2;
        }
    } else {
        c2 = -one;
        s2 = zero;
    }

    const s = Math.sqrt(half * (one - c2));
    const c = half * s2 / s;
    const diagonal = [];
    const csqr = c * c;
    const ssqr = s * s;
    const mid = s2 * a01;
    diagonal[0] = csqr * a00 + mid + ssqr * a11;
    diagonal[1] = csqr * a11 - mid + ssqr * a00;

    const eval1 = [];
    const evec = [];

    if (diagonal[0] <= diagonal[1]) {
        eval1[0] = diagonal[0];
        eval1[1] = diagonal[1];
        
        evec[0] = new THREE.Vector2(c, s);
        evec[1] = new THREE.Vector2(-s, c);
    } else {
        eval1[0] = diagonal[1];
        eval1[1] = diagonal[0];
        evec[0] = new THREE.Vector2(s, -c);
        evec[1] = new THREE.Vector2(c, s);
    }
    
    const diff = _points[0];
    const pmin = new THREE.Vector2(diff.dot(evec[0]), diff.dot(evec[1]));
    let pmax = pmin.clone();

    fromPoints_getMax(_points, pmin, pmax, evec);

    for (let j = 0; j < 2; ++j) {
        centroid.add(evec[j].clone().multiplyScalar(0.5 * (pmin.getComponent(j) + pmax.getComponent(j))));
        const x = pmax.getComponent(j);
        const y = pmin.getComponent(j);

        eval1[j] = 0.5 * (x - y);
    }

    evec[0].multiplyScalar(eval1[0]);
    evec[1].multiplyScalar(eval1[1]);

    const matrix = new THREE.Matrix3();
    matrix.set(evec[0].x, evec[1].x, 0, evec[0].y, evec[1].y, 0, 0, 0, 1);

    return new OBB2(centroid, matrix);
};

/**
 * 三维在同一平面上的点，生成一个包围矩形
 * @param {Vector3} points 
 * @returns 
 */
OBB2.computeRectFromPoints3 = points => {

    if (points.length < 3) {
        throw new Error('points.length < 3');
    }

    let triangle;
    
    for (let i = 2; i < points.length; i++) {
        const a = points[i - 2];
        const b = points[i - 1];
        const c = points[i];

        if (!isCollinear(a, b , c)) {
            triangle = new THREE.Triangle(a, b, c);
        }
    }

    if (!triangle) {
        throw new Error('points is collinear');
    }

    const normal = triangle.getNormal();
    const x = new THREE.Vector3().copy(triangle.a).sub(triangle.b).normalize();
    const y = normal.clone().cross(x);

    const matrix = new THREE.Matrix4().makeBasis(x, y, normal);
    matrix.setPosition(triangle.a);

    const invert = matrix.clone().invert();

    const _points = points.map(it => it.clone().applyMatrix4(invert));

    const obb = OBB2.fromPoints(_points);
  
    const positions = obb.getVertices();

    return positions.map(it => new THREE.Vector3(it.x, it.y).applyMatrix4(matrix));
};


/**
 * 计算指定方向下的OBB
 */
function computeOBBForDirection(points, direction, normal) {
    let minProjDir = Infinity;
    let maxProjDir = -Infinity;
    let minProjNormal = Infinity;
    let maxProjNormal = -Infinity;
    
    // 计算在方向和法向量方向上的投影极值
    for (const point of points) {
        const projDir = point.dot(direction);
        const projNormal = point.dot(normal);
        
        minProjDir = Math.min(minProjDir, projDir);
        maxProjDir = Math.max(maxProjDir, projDir);
        minProjNormal = Math.min(minProjNormal, projNormal);
        maxProjNormal = Math.max(maxProjNormal, projNormal);
    }
    
    // 计算OBB尺寸
    const width = maxProjDir - minProjDir;
    const height = maxProjNormal - minProjNormal;
    
    // 计算OBB中心点
    const centerDir = (minProjDir + maxProjDir) / 2;
    const centerNormal = (minProjNormal + maxProjNormal) / 2;
    
    const center = new Vector2(
        direction.x * centerDir + normal.x * centerNormal,
        direction.y * centerDir + normal.y * centerNormal
    );
  
    const area = width * height;

    return {
        area,
        width,
        height,
        center,
        direction,
        normal
    };
    
}

OBB2.fromPoints2 = (points) => {

    if (!points || points.length == 0) {
        return null;
    }

    const _points = points.map(it => (Array.isArray(it) ? new THREE.Vector2(...it) : new THREE.Vector2(it.x, it.y)));

    // 1. 计算凸包
    const convexHull1 = convexHullMonotoneChain(_points);
    
    // 2. 使用旋转卡壳法找到最小面积包围盒
    let minArea = Infinity;
    let bestOBB = null;
    
    const n = convexHull1.length;
    
    for (let i = 0; i < n; i++) {
        // 当前边
        const current = convexHull1[i];
        const next = convexHull1[(i + 1) % n];
        
        // 计算边的方向向量
        const edge = new Vector2().subVectors(next, current).normalize();
        
        // 计算垂直方向（法向量）
        const normal = new Vector2(-edge.y, edge.x);
        
        // 计算OBB
        const obb = computeOBBForDirection(convexHull1, edge, normal);
        
        if (obb.area < minArea) {
            minArea = obb.area;
            bestOBB = obb;
        }
    }

    if (bestOBB) {
        const {
            width,
            height,
            center,
            direction,
            normal
        } = bestOBB;

        direction.multiplyScalar(width * 0.5);
        normal.multiplyScalar(height * 0.5);

        const mat = new THREE.Matrix3();
        mat.set(direction.x, normal.x, 0, direction.y, normal.y, 0, 0, 0, 1);
        
        return new OBB2(center, mat);
    }
    

    return null;
};