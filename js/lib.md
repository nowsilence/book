# 常用js库 #
-词云
echarts-wordcloud
vue-wordcloud

-视差动画
gsap

-Cookie
js-cookie

-加解密
jsencrypt

-DOCX到HTML/Markdown/TEXT转换
mammoth

-事件总线
mitt

-轻量级的进度条库，主要用于在页面加载或路由切换时在顶部显示进度条，提升用户体验 
nprogress

-触摸滑动 可实现轮播图、焦点图、触摸导航等滑动效果[演示](https://swiper.com.cn/demo/index.html)
swiper

-控件
element-plus

-解析、验证、操作和显示日期和时间
dayjs

-数字倒计时，可设置动画曲线
countup.js

-大屏开发
autofit.js // 基于 `transform: scale` 整体等比缩放
amfe-flexible + postcss-pxtorem 也可以实现
vfit.js 类似autofit

-图表
vue-echarts 针对echarts的封装库，两个都需要安装
echarts 通用库

-解压
pako
    pako.inflate(data);      // zlib 包装的 deflate（带头）
    pako.inflateRaw(data);   // 裸 deflate（无 gzip/zlib 外壳）
    pako.ungzip(data);       // gzip 文件
jszip 依赖pako