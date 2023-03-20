class Polynomial {
    constructor(degree, coeff) {
        this.degree = degree || 0;
        this.coeff = coeff || [];
    }

    evaluate(u) {
        let w = 1.0;
        let value = 0.0;

        for (let i = 0; i <= this.degree; i++) {
            value += this.coeff[i] * w;
            w *= u;
        }

        return value;
    }
}

class Interval {
    constructor(u1, u2, length) {
        this.u1 = u1 || 0;
        this.u2 = u2 || 0;
        this.length = length || 0;
    }
}

function integratePolynomial(polynomial, interval) {
    const x =[.1488743389,.4333953941,.6794095682,.8650633666,.9739065285];
    const w =[.2966242247,.2692667193,.2190863625,.1494513491,.0666713443];
    
    let length, midu, dx, diff;
    
    ua = interval.u1;
    ub = interval.u2;
    midu = (ua + ub) / 2.0;
    diff = (ub - ua) / 2.0;
    length = 0.0;
    
    for (let i = 0; i < 5; i++) {
        dx = diff * x[i];
        const pol1 = polynomial.evaluate(midu + dx);
        const pol2 = polynomial.evaluate(midu - dx);
        length += (Math.sqrt(pol1) + Math.sqrt(pol2)) * w[i];
    }

    length *= diff;

    return length;
}

function subdivide(table, fullInterval, polynomial, totalLength, tolerangce) {
    const leftInterval = new Interval();
    const rightInterval = new Interval();

    const midu = (fullInterval.u1 + fullInterval.u2) * 0.5;
    leftInterval.u1 = fullInterval.u1;
    leftInterval.u2 = midu;
    rightInterval.u1 = midu;
    rightInterval.u2 = fullInterval.u2;

    const leftLength = integratePolynomial(polynomial, leftInterval);
    const rightLength = integratePolynomial(polynomial, rightInterval);

    const temp = Math.abs(fullInterval.length - (leftLength + rightLength));

    if (temp > tolerangce) {
        leftInterval.length = leftLength;
        rightInterval.length = rightLength;

        totalLength = subdivide(table, leftInterval, polynomial, totalLength, tolerangce * 0.5);
        totalLength = subdivide(table, rightInterval, polynomial,totalLength, tolerangce * 0.5);

        return totalLength;
    } else {
        totalLength += leftLength;
        table.push({ u: midu, length: totalLength });

        totalLength += rightLength;
        table.push({ u: fullInterval.u2, length: totalLength });

        return totalLength;
    }
}

function adaptiveIntegration(curve, u1, u2, tolerangce) {

    const func = new Polynomial(4);

    const a = curve.a();
    const b = curve.b();
    const c = curve.c();

    func.coeff[4] = 9 * (a.x * a.x  + a.y * a.y);
    func.coeff[3] = 12 * (a.x * b.x + a.y * b.y);
    func.coeff[2] = 6 * (a.x * c.x + a.y * c.y) + 4 * (b.x * b.x + b.y * b.y);
    func.coeff[1] = 4 * (b.x * c.x + b.y * c.y);
    func.coeff[0] = c.x * c.x + c.y * c.y;

    const fullInterval = new Interval(u1, u2);
    fullInterval.length = integratePolynomial(func, fullInterval);
    
    const al = new ArcLength(u1, u2);
    al.length = subdivide(al.table, fullInterval, func, 0, tolerangce);

    return al;
}

class ArcLength {
    constructor(u1, u2) {
        this.u1 = u1;
        this.u2 = u2;
        this.length = 0;
        this.table = [];
    }

    getValueU(offset) {
        let indice = 0;
        for (let i = 1;i < this.table.length; i++){
            if(this.table[i].length >= offset && this.table[i - 1].length <= offset){
                indice = i - 1;
            }
        }
        return this.getU(indice,offset);
    }

    getU(indice, s) {
        const u1 = this.table[indice].u;
        const u2 = this.table[indice + 1].u;

        const s1 = this.table[indice].length;
        const s2 = this.table[indice + 1].length;

        let u = s * (2 * u1 * u2 - u1 * u1 - u2 * u2) - (u1 * u2 - u2 * u2) * s1 - (u1 * u2 - u1 * u1) * s2;
        u = u / ((u2 - u1) * s1 + (u1 - u2) * s2);

        return u;
    }
}

class CubicBezier {
	/**
	 * @param {number} pa 起点
	 * @param {number} pb 控制点
	 * @param {number} pc 控制点
	 * @param {number} pd 终点
	 */
    constructor(pa, pb, pc, pd) {
        this.pa = pa;
        this.pb = pb;
        this.pc = pc;
        this.pd = pd;
    }

    a() {
        const x = -1 * this.pa.x + 3 * this.pb.x - 3 * this.pc.x + 1 * this.pd.x;
        const y = -1 * this.pa.y + 3 * this.pb.y - 3 * this.pc.y + 1 * this.pd.y;

        return { x, y };
    }

    b() {
        const x = 3 * this.pa.x - 6 * this.pb.x + 3 * this.pc.x; // + 0 * this.pd.x;
        const y = 3 * this.pa.y - 6 * this.pb.y + 3 * this.pc.y; // + 0 * this.pd.y;

        return { x, y };
    }

    c() {
        const x = -3 * this.pa.x + 3 * this.pb.x; // - 0 * this.pc.x + 0 * this.pd.x;
        const y = -3 * this.pa.y + 3 * this.pb.y; // - 0 * this.pc.y + 0 * this.pd.y;

        return { x, y };
    }

    get length() {
        if (!this._arcLength) {
            const lengthSq = (this.pa.x - this.pd.x) * (this.pa.x - this.pd.x) + (this.pa.y - this.pd.y) * (this.pa.y - this.pd.y);
            //const tolerance = Math.sqrt(lengthSq) / 100000000; // 
            this._arcLength = adaptiveIntegration(this, 0, 1, 0.0000001);
        }

        return this._arcLength.length;
    }

    evaluate(t) {
        const t2 = t * t;
        const t3 = t2 * t;

        const b0 = -t3 + 3 * t2 - 3 * t + 1;
        const b1 = 3 * t3 - 6 * t2 + 3 * t;
        const b2 = -3 * t3 + 3 * t2;
        const b3 = t3;

        return {
            x: this.pa.x * b0 + this.pb.x * b1 + this.pc.x * b2 + this.pd.x * b3,
            y: this.pa.y * b0 + this.pb.y * b1 + this.pc.y * b2 + this.pd.y * b3
        };
    }

	/**
	 * 计算到起始点距离为offset的坐标点
	 * @param {number} offset 距离起始点距离
	 */
    evaluateByOffset(offset) {
        const u = this._arcLength.getValueU(offset);
        return this.evaluate(u);
    }
}

// export { CubicBezier, adaptiveIntegration };