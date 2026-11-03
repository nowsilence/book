```js
module.exports = {
  presets: [
    /**
     * 按目标浏览器自动转译：读取 package.json 里的 browserslist 配置，根据你要兼容的浏览器范围，自动决定把哪些 ES 新语法（箭头函数、解构、async/await 等）降级。
     * 按需注入 polyfill：结合 useBuiltIns（由 CLI 自动管理），只引入目标浏览器缺失的 API 垫片（如 Promise、Array.prototype.includes），不会全量打包 core-js，减小体积。
     * 支持新特性与 JSX：内置 @babel/preset-env 等，支持最新 ECMAScript 语法，并能处理 Vue 的 JSX/函数式组件写法。
     * 集成 transform-runtime：避免 polyfill 污染全局，复用 helper 函数。
     * 关键点：
     * 这个 preset 是 Vue CLI 的标准入口，绝大多数转换规则都由它内部统一处理，你通常不需要再手写一堆 preset/plugin
     */
    // https://github.com/vuejs/vue-cli/tree/master/packages/@vue/babel-preset-app
    '@vue/cli-plugin-babel/preset'
  ],
  'env': {
    'development': {
        /**
         *  在 development（开发）环境下，把代码中所有 ES 动态导入 import('xxx') 转成 CommonJS 的 require('xxx')。
            动态 import() 在 webpack 里会触发代码分割（生成独立 chunk）。项目页面很多时，每次热更新都要重新生成这些 chunk，HMR 很慢。
            改成 require() 后不再分割代码，热更新几乎瞬间完成，开发体验大幅提升。
            注意点：

            只在 env.development 生效，生产构建仍走正常 import() + 懒加载分包，不影响产物体积。
            这是 vue-element-admin 系脚手架的标配优化（注释里也引用了它的文档）。
            一句话：开发时把路由懒加载“关掉”以加速热更新，生产时保留分包。
         */
      // babel-plugin-dynamic-import-node plugin only does one thing by converting all import() to require().
      // This plugin can significantly increase the speed of hot updates, when you have a large number of pages.
      // https://panjiachen.github.io/vue-element-admin-site/guide/advanced/lazy-loading.html
      'plugins': ['dynamic-import-node']
    }
  }
}

```