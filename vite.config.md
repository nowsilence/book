```js
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import VueSetupExtend from "vite-plugin-vue-setup-extend";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";
export default defineConfig({
  base: "./", // import.meta.env.BASE_URL 这个环境变量可以拿到这个值
  //  build: {
  //    sourcemap: true, // 生成完整的 source map
  // },
  plugins: [
    vue(),
    VueSetupExtend(),
    /**
     * 是跨构建工具的自动导入插件，支持 Vite / Webpack / Rspack / Rollup / esbuild，作用：不用手写 import，直接使用库 API
     * / 以前要手动导入
     *import { ref, computed, onMounted } from 'vue'
     * import { useRoute } from 'vue-router'
     * 
     * // 使用插件后，直接写
     * const count = ref(0)
     * const route = useRoute()
     * onMounted(() => {})
     **/
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    /**
     *  自动按需导入 Vue 组件，无需手动写 import xxx from 'xxx'
     **/ 
    Components({
        dirs: ['src/components'], // 默认值 为['src/components']
        extensions: ['vue'], // 默认值为 ['vue'] 其他：['vue', 'tsx', 'jsx']
        dts: 'src/components.d.ts', // 默认值为true 在项目根目录生成 components.d.ts；自定义路径: dts: 'src/components.d.ts'; dts = false
        deep: true, // 默认true 递归子文件扫描
        exclude: [/src\/components\/demo/], // 排除不需要自动导入的组件
        /**
         * 自动导入组件代码
         * 自动引入对应组件样式，无需全局引入 Element Plus
         * 模板写 <el-button>，插件底层自动生成：
         * import ElButton from 'element-plus/es/components/button'
         * import 'element-plus/es/components/button/style/css'
         **/ 
        resolvers: [ElementPlusResolver()],
    }),
  ],
  //包含 Element Plus） // 如果遇到 @use 报错,将 @use 改为 @import
//    css: {
//     preprocessorOptions: {
//       scss: {
//         additionalData: `
//           @use "@/styles/element/index.scss" as *;
//           @import "@/styles/variables.scss";
//         `
//       }
//     }
//   },
  css: {
    preprocessorOptions: {
      scss: {
       // additionalData: `@import "@/styles/variables.scss";`,
         additionalData: `@use "@/styles/variables.scss" as *;`
      },
    //   sass: {
    //     additionalData: `@import "@/styles/variables.sass"`,
    //   },
    },
    postcss: {
      plugins: [
        // 也可以使用和vite.config.js同目录下的postcss.config.js文件进行配置，下方的配置是postcss.config.js的配置，不能是字符串，必须是实例化后的对象
        postcssPxtorem({
          // 设计稿宽度 1920 / 10 = 192
            rootValue: 192,
            // 转换所有包含 px 的属性
            propList: ['*'],
            // 排除 Element Plus 组件，保持其原始 px 尺寸
            // selectorBlackList: [/^\.el-/],
            // selectorBlackList: [/^.el-/, '.no-rem'],
            // 保留 1px 边框，不转换
            minPixelValue: 2,
            // rem 小数精度
            unitPrecision: 5,
            // 媒体查询断点保持 px，不转换
            mediaQuery: false,
            exclude: /node_modules/i
        })
      ]
    }
  },
  server: {
    host: "0.0.0.0",
    //   port: 5173,
    //   open: true,
    //   proxy: {
    //     // 代理 /dev-api 的请求
    //     [env.VITE_APP_BASE_API]: {
    //       changeOrigin: true,
    //       // 代理目标地址：https://api.youlai.tech
    //       target: env.VITE_APP_API_URL,
    //       rewrite: (path: string) => path.replace(new RegExp("^" + env.VITE_APP_BASE_API), ""),
    //     },
    //   },
    proxy: {
      '/api': { // 发出请求时：http://10.12.36.10:8000/api会带api
        // target: 'http://127.0.0.1:8000',
        target: 'http://10.12.36.10:8000',
        changeOrigin: true,
      },
      '/dev-api': {
        target: 'http://127.0.0.1:8080', // 后端真实域名
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/dev-api/, ''), // 发出请求时http://127.0.0.1:8080, 不带dev-api
      },
      '/ws': {
        // target: 'ws://127.0.0.1:8000',
        // target: 'ws://10.12.36.10:8000',
        target: 'ws://10.12.10.160:8057',
        ws: true,
        changeOrigin: true,
      },
    },
  },
  esbuild: {
    sourcemap: true,
  },
  optimizeDeps: {
    include: ["schart.js"],
  },
  resolve: {
    alias: {
      "@": "/src",
      "~": "/src/assets",
    },
  },
  define: {
    __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: "true",
  },
});

```

## postcss配置

```javascript
// postcss.config.js
export default {
  plugins: {
    'postcss-pxtorem': { // 不需要到手动require('postcss-pxtorem') PostCSS 内核拿到这个字符串，会内部执行 require('postcss-pxtorem') 动态加载模块，前提是这个模块已经安装过了
      rootValue: 37.5, // 设计稿375，1rem = 37.5px
      propList: ['*'], // 所有css属性都转rem
      propBlackList: ['font-size'], // ✅ font‑size禁止转rem，字体直接写px
      selectorBlackList: ['.norem'], // class="norem" 的所有属性都不转rem
      minPixelValue: 1, // 小于1px不转换
      replace: true,
      mediaQuery: false
    }
  }
}
```

1.Vite 在处理 css、scss、less、vue 单文件里的 <style> 时，会进入它内置的 CSS 处理插件流水线。
2.到 PostCSS 环节，Vite 调用第三方库 postcss‑load‑config，默认从项目根目录（process.cwd()，和 vite.config.ts 同级）查找 postcss 配置文件。
  postcss‑load‑config 支持识别这些文件名：
  **postcss.config.js**
  **postcss.config.mjs**
  **postcss.config.cjs**
也可以在 package.json 里写 "postcss": {...} 配置块
读到配置后，取出里面的 plugins 插件列表（你的 postcss‑pxtorem），交给 PostCSS 内核执行转换。
转换完的 css 再继续交给 Vite 做后续处理（HMR、压缩、输出）。