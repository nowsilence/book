源颜色（即将要绘制的颜色）片段着色器的颜色输出
目标颜色（已经绘制的颜色） 当前存储在颜色缓冲区中的颜色

vec3 luma = vec3( 0.299, 0.587, 0.114 );

人眼对绿色的敏感度最高，对红色的敏感度次之，对蓝色的敏感度最低，因此使用不同的权重将得到比较合理的灰度图像

void glBlendFunc(GLenum srcfactor, Glenum dstfactor);
RGBA = <源颜色> * srcfactor + <目标颜色> * dstfactor
void glBlendFuncSeperate(GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, Glenum dstAlpha);
相较于glBlendFunc将rgb与a分量的计算因子拆分出来。
RGB = <源颜色> * srcRGB + <目标颜色> * dstRGB
A = As * srcAlpha + Ad * dstAlpha
