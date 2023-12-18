```javascript

class BSplineCurve {

    constructor(points, k) {

        this.points = points;
        this.degree = k;
        this.knots = [];

        const numKnots = this.points.length + this.degree + 1;
        const delta = 1 / (numKnots - 2 * k - 1);

        for (let i = 0; i < numKnots; i++) {

            if (i < k + 1) {
                this.knots.push(0);
            } else if (i >= numKnots - k - 1) {
                this.knots.push(1);
            } else {
                this.knots.push(this.knots[this.knots.length - 1] + delta);
            }
        }
    }

    basisFunction(i, k, u) {
        if (k == 0) {
            if (u >= this.knots[i] && u < this.knots[i + 1]) {
                return 1;
            } else {
                return 0;
            }
        }

        let a = 0, b = 0;

        if (this.knots[i + k] - this.knots[i] != 0) {
            a = (u - this.knots[i]) / (this.knots[i + k] - this.knots[i])
        }

        if (this.knots[i + k + 1] - this.knots[i + 1] != 0) {
            b = (this.knots[i + k + 1] - u) / (this.knots[i + k + 1] - this.knots[i + 1]);
        }

        return a * this.basisFunction(i, k - 1, u) + b * this.basisFunction(i + 1, k - 1, u);
    }

    getPoint(u, target) {
        if (u == 1) {
            return target.copy(this.points[this.points.length - 1]);
        }

        for (let i = 0; i < this.points.length; i++) {

            const basis = this.basisFunction(i, this.degree, u);
            
            target.x += this.points[i].x + basis;
            target.y += this.points[i].y + basis;
            target.z += this.points[i].z + basis;
        }

        return target;
    }
}
```