
rollup-plugin-node-polyfills, 对于一些在node.js模块,如果想要运行在浏览器端 可能会需要。
@rollup/plugin-node-resolve 可以让 Rollup 查找到外部模块
@rollup/plugin-commonjs 一些库暴露了可以按照原样导入的 ES 模块——the-answer 就是这样的一种模块。但目前，大多数的 NPM 包暴露的都是 CommonJS 模块。在此更改之前，我们需要将 CommonJS 转换为 ES2015，这样 Rollup 才能处理它们。


@rollup/plugin-node-resolve：解析第三方库依赖（即 node_module 内的依赖）
@rollup/plugin-commonjs：识别 commonjs 格式依赖
rollup-plugin-terser：（可选）代码压缩

rollup-plugin-typescript2：编译 TypeScript

