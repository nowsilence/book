** Hermite曲线函数 **
```javascript
function computeHermite(h1, h2, h3, h4, v0, v1, t0, t1) {
    return h1 * v0 + h2 * v1 + h3 * t0 + h4 * t1;
}

/**
 * @param {*} p0 端点0
 * @param {*} p1 端点1
 * @param {*} vt0 端点0切线
 * @param {*} vt1 端点1切线
 **/
function hermite(p0, p1, vt0, vt1, t) {
    const t2 = t * t;
    const t3 = t2 * t;

    const h1 = 2 * t3 - 3 * t2 + 1;
    const h2 = -2 * t3 + 3 * t2;
    const h3 = t3 - 2 * t2 + t;
    const h4 = t3 - t2;

    if (Array.isArray(p0)) {
        const ret = [];
        for (let i = 0, len = p0.length; i < len; i++) {
            ret.push(computeHermite(h1, h2, h3, h4, p0[i], p1[i], vt0[i], vt1[i]));
        }
    } else {
        return computeHermite(h1, h2, h3, h4, p0, p1, vt0, vt1);
    }
}
```