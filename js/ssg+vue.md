

onMounted方法在SSG/SSR中无效，不会被执行
不要在onMounted方法里请求数据或者把props赋值给其他ref对象；
在setup里输出console.log(content.value)，导致ssg输出的文件会重新触发请求，导致ssg失败，尽量还是不要用吧

**vite‑ssg：预渲染只发生在「浏览器首次 HTTP 加载这个 html 文件」的时候。`router‑link` 是客户端 JS 跳转，**不会重新去网络下载 `/news/index.html` 静态文件 **，只会在内存里重新执行组件，重新跑一遍数据请求，不会复用磁盘上预渲染好的静态 HTML 与里面的预取数据
也就是说，如果在首页点击新闻列表，走的是路由，则不会加载预先生成的静态文件，如果不在新闻组件里重新请求数据，则列表为空。
很多人踩这个坑，误以为 vite‑ssg 打包出来一堆 html，SPA 跳转就会读取这些 html，**不是的**。dist 下一堆 html，只用于「直接访问该 URL」的 HTTP 请求（刷新、新开标签、a 硬跳转）。
那ssg与渲染还有什么用？
1、如果是通过url直接访问，比如：https://www.baidu.com/news/index.html，则会直接加载生成好的静态文件。爬虫不受影响，这样的话就可以做SEO，核心价值就是 **SEO / 爬虫抓取**
2、在预渲染阶段可以把每个路由对应的 state 单独输出成 json 文件到 dist（这正是nuxtjs内部做的事情），这样也可以做到spa，同时也有静态文件
```js
// vite‑ssg构建阶段
onSSRAppRendered((routePath)=>{
  // 将当前路由initialState写入 public/_ssg_states/${routePath}.json
})

router.beforeEach((to, from, next) => {
  // 拉取json恢复数据
})
```

## SEO  ##
```html
<head>
  <meta name="keywords" content="vue,vite-ssg,教程">
  <meta name="description" content="页面描述">
  <title>页面标题</title>
</head>
```

- `<title>`：**非常重要**，搜索结果标题，权重很高。
- `meta description`：搜索结果下面的摘要，影响点击率，重要。
- `meta keywords`：**谷歌、百度早已不把它作为排名依据**，写了几乎没用，很多站点直接删掉。

现在：HTML 内要有真实可见文本内容
语义化标签：`<h1>`页面大标题，`<h2>`小标题，`<p>`正文，`<a>`站内链接


## nginx 配置 ##
```nginx
# 需要添加以下配置
# ---------- 静态页面路由 ----------
# vite-ssg 多页静态站：每个路由对应一个 .html 文件
# /news -> news.html, /about -> about.html, /news/53 -> news/53.html
# 必须加 $uri.html 让 /news 命中 news.html，否则会 fallback 到 index.html
# 而 index.html 的 __INITIAL_STATE__ 只含 counter store，不含 news 数据
location / { # 匹配**所有以 `/` 开头的请求 URI**
    try_files $uri $uri.html $uri/ /index.html;
}
```        

## SSR 渲染 ##

SSR也是一样的，首屏请求会在服务器动态生成html，然后返回给客户端，客户端渲染。但如果是路由进入的组件也是需要请求接口数据的。
好处：
首屏加载快
爬虫拉取、实现SEO