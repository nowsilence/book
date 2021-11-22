```javascript
// 计算三角形外心
function create(a, b, c) {
    const t = b.clone().sub(a);
    const u = c.clone().sub(a);
    const v = c.clone().sub(b);

    const w = t.clone().cross(u);
    const wsl = w.dot(w);

    if (wsl < 10e-14) {
        return null;
    }

    const iwsl2 = 1.0 / (2.0 * wsl);
    const tt = t.dot(t);
    const uu = u.dot(u);

    const n = u.clone().multiplyScalar(tt * u.dot(v));
    const m = t.clone().multiplyScalar(uu * t.dot(v));

    const center = a.clone().add(n.sub(m).multiplyScalar(iwsl2));
    const radius = Math.sqrt(tt * uu *  v.dot(v) * iwsl2 * 0.5);

    return { radius, center, direction: w };
}

```