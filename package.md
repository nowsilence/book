```json
{
    "browserslist": [ // 被多个工具共享读取：autoprefixer（决定加哪些 CSS 前缀）、Babel（决定转译哪些 ES 语法）、postcss 等
        "> 1%", // 全球使用率超过 1% 的浏览器都支持。
        "last 2 versions" // 每个主流浏览器的最近 2 个版本都支持
    ],
}

```