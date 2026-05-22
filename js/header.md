# Http Header

## referer
来源页，浏览器自动告诉目标服务器：我是从哪个页面跳过来 / 发起请求的
主要用途：
* 网站流量统计
* 服务器看 Referer 就知道：用户从哪个网站点进来的，用来统计引流来源、SEO 来源。
* 日志分析、用户行为追踪
* 记录用户浏览路径。
* 表单防跳转劫持
* 简单校验是不是本站页面提交的表单。
* 资源溯源
* 知道图片 / JS / 视频是哪个页面在用。
* 防盗链：不是我允许的网站，不给你加载资源

例如天地图栅格瓦片请求使用Prefer进行防盗链，在主线程请求的话浏览器会自动添加referer，在webworker内不会主动添加，故在子线程请求报403错误，
解决方法：
* 主动添加referer，可选地址有：https://www.tianditu.gov.cn/或https://map.tianditu.gov.cn
* 使用nginx代理，配置referer

## Accept
客户端告诉服务器本次请求：我能接收、想要什么类型的数据
格式：Accept: 类型1,类型2;权重
* 浏览器打开图片：Accept: image/* → 我只要图片
* 普通网页请求：Accept: text/html → 我要网页文本
* Ajax 默认：Accept: */* → 啥都能收

常见风控场景：
* 防盗链：只允许图片类型请求拿图片
* 接口隔离：图片接口只放行 image/* 请求，服务器可能配置如果请求图片资源，那么accept必须是image/*,若不是报403，Ajax默认的Accept: */*
* 防爬虫、非法跨站调取资源

async function task() {
  console.log('开始')
  console.log('一秒后')
}