** 两个向量夹角 **

```
单位化两个向量，点乘后值为余弦值，反余弦得角度
```

** 向量与坐标轴夹角(0~2π) **
```
# 与y轴夹角
# 逆时针 -π~+π 
double rad = Math.atan2(-this.x, this.y);
# 顺时针 -π~+π 
Math.atan2(this.x, this.y);

# 与x轴夹角
Math.atan2(this.y, this.x);  // 逆时针
Math.atan2(-this.y, this.x); // 顺时针

# 0~2π
rad = rad < 0 ? Math.PI * 2 + rad : rad;

# 或者（仅列与y轴夹角）
double cos = new Vector(0, 1).dot(this);
double rad = Math.acos(cos);
rad =  this.x > 0 ? Math.PI * 2 - rad : rad;
```