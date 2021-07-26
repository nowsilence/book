[参考](https://blog.csdn.net/qq_35732147/article/details/81867017)
GetMap请求参数:

service=WMS    ——    表示使用WMS服务
version=1.3.0    ——    表示使用1.3.0版本
request=GetMap    ——    表示执行GetMap操作
layers=tasmania    ——    表示请求图层为Tasmania
由于没有设置STYLE参数的值，所以表示使用默认样式绘制图层
crs=EPSG:4326    ——    表示使用坐标参照系统为EPSG:4326
bbox=-43.648056,143.83482400000003,-39.573891,148.47914100000003    ——    表示需要绘制的地图范围
format=image/png    ——    表示返回的地图图片格式为PNG
width与height    ——    指定返回图像的宽与高，单位为像素   