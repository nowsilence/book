```js
// https://github.com/michael-ciniawsky/postcss-load-config

module.exports = {
  'plugins': {
    // to edit target browsers: use "browserslist" field in package.json
    'autoprefixer': {} // 依赖库：autoprefixer，在 PostCSS 的 plugins 中注册 autoprefixer 插件，autoprefixer 会根据目标浏览器自动为 CSS 添加厂商前缀（如 -webkit-、-moz-、-ms-），编译时添加
  }
}

```