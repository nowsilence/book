需要注意的是模型坐标系、世界坐标系、视坐标系以及裁剪坐标系任何时候都是右手坐标系。默认情况下这四个坐标系完全重合，默认这四个坐标系的原点都在屏幕中心，从原点向右为x轴正半轴，从原点向上为y轴正半轴，从原点垂直于屏幕向外是z轴的正半轴。如果进行了某些矩阵操作变换，那么这四个坐标系就很可能不在重合，不过这四个坐标系还是右手坐标系。NDC坐标系（归一化设备坐标系）是左手坐标系，其z轴方向与前四个坐标系的z轴方向相反。

https://img-blog.csdnimg.cn/20191014141442801.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RXOTM0NDQwNjUz,size_16,color_FFFFFF,t_70
![avatar](https://img-blog.csdnimg.cn/20191014141442801.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RXOTM0NDQwNjUz,size_16,color_FFFFFF,t_70)


(Vertex Shader) => Clip Space => (透视除法) => NDC => (视口变换) => Screen Space => (Fragment Shader)

gl_FragCoord.xy 为窗口坐标，单位像素

原点 的窗口坐标值为 (0.5, 0.5), 小数部分恒为 0.5， 当viewport 范围 为（0，0，800，600）时， x, y 的取值范围为（0.5, 0.5, 799.5, 599.5)

gl_FragCoord.z 值产生的过程：
（1）观察坐标系中的坐标通过乘上投影矩阵变换到裁剪空间 clip.z = projectMatrix * camera.z;
（2）裁剪坐标系 到 设备规范化坐标系 ，透视除法 ndc.z = clip.z / clip.w;
（3）规范化设备坐标系到窗口坐标系 win.z  = (dfar - dnear)/2 * ndc.z + (dfar+dnear)/2; 可以看出 gl_FragCoord.z 是 win.z .dfar ,dnear 是由 glDepthRange 给定的，按openGL 默认值 （0，1） ， win.z = ndc.z/2 + 0.5 , 那么 ndc.z = win.z * 2.0 - 1.0。


ndc.xyzw = ( gl_FragCoord.xy/viewport.wh * 2.0 - 1.0, gl_FragCoord.z * 2.0 - 1.0, 1.0 );

[参考](http://trading-sutra.com/2020/07/07/gl_fragcoord-%e7%9a%84%e6%84%8f%e4%b9%89/)
