```
+a         椭球体长半轴长度
+alpha     ? 用于斜墨卡托和其它几个可能的投影
+axis      轴方向 (new in 4.8.0)
+b         椭球体短半轴长度
+datum     基准面名(见`proj -ld`)
+ellps     椭球体名(见`proj -le`)
+k         比例因子(old name)
+k_0       比例因子(new name)
+lat_0     维度起点
+lat_1     标准平行纬线第一条
+lat_2     标准平行纬线第二条
+lat_ts    有效纬度范围Latitude of true scale
+lon_0     中央经线
+lonc      ? 经度用于斜墨卡托和其它几个可能的投影
+lon_wrap  Center longitude to use for wrapping (见下文)
+nadgrids  NTv2网格文件的文件名，用于基准面转换(见下文)
+no_defs   不要使用/usr/share/proj/proj_def.dat缺省文件
+over      允许经度超出-180到180范围,禁止wrapping (见下文)
+pm        备用本初子午线(通常是一个城市的名字，见下文)
+proj      投影名(见`proj -l`)
+south     表示南半球UTM区域
+to_meter  乘数，转换地图单位为1.0m
+towgs84   3或7参数基准面转换(见下文)
+units     meters(米), US survey feet(美国测量英尺),等.
+vto_meter 垂直变换为米.
+vunits    垂直单位.
+x_0       东伪偏移
+y_0       北伪偏移
+zone      UTM区域
```