
mix(x, y, a): x, y的线性混叠， x * (1 - a) + y * a;

LinearRGB转换为sRGB：

var linear = xxx;  // xxx是0-1的数值
var s;
if (linear <= 0.0031308) {
  s = linear * 12.92;
} else {
  s = 1.055 * Math.pow(linear, 1.0/2.4) - 0.055;
}


sRGB转换为LinearRGB：

var s = xxx;    // xxx是0-1的数值
var linear;
if (s <= 0.04045) {
  linear = s / 12.92;
} else {
  linear = Math.pow((s + 0.055) / 1.055, 2.4);
}


对于sRGB色彩空间，颜色的相对亮度定义为
L = 0.2126 * R + 0.7152 * G + 0.0722 * B其中R，G和B定义为：

如果R sRGB <= 0.03928，则R = R sRGB /12.92
否则R =（（R sRGB +0.055）/1.055）^ 2.4

如果G sRGB <= 0.03928，则G = G sRGB /12.92
否则G =（（G sRGB +0.055）/1.055）^ 2.4

如果B sRGB <= 0.03928，则B = B sRGB /12.92
否则B =（（B sRGB +0.055）/1.055）^ 2.4

R sRGB ，G sRGB和B sRGB定义为：

R sRGB = R 8位 / 255

G sRGB = G 8位 / 255

B sRGB = B 8位 / 255



将它们相乘最后得到diffuse，可以称它为漫反射强度。漫反射就是投射在粗糙表面上的光向各个方向反射的现象。我们求解diffuse就是模拟的漫反射现象。

代码最后还有一个vec3 ambient = vec3(0.3);是什么呢？根据漫反射的公式，总会有强度为0的地方，为了使场景不那么暗，就增加了一个基本光照强度，也可称为环境光强度。

https://www.jianshu.com/p/de4b3f9b2177