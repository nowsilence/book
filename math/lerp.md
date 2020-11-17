float lerp(float a, float b, float w) {
  return a(1-w) + b * w;
}

等价

float lerp(float a, float b, float w) {
  return a + w*(b-a);
}

混合公式，俗称线性插值， 只不过w相当于以第二个参数为源，第一个参数为目标。 直白点，就是把b向a上混合


a与b为同类形，即都是float或者float2之类的，那lerp函数返回的结果也是与ab同类型的值。
w是比重，在0到1之间
当w为0时返回a，为1时返回b，在01之间时，以比重w将ab进行线性插值计算。


和webgl里的mix函数功能相同

x(1-a)+ya