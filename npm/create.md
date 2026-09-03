
# 创建项目

```bash
npm create vite@latest my‑react‑demo -- --template react
```

用 npm 调用最新版 create‑vite，创建一个叫 my‑react‑demo 的项目，模板选用 React（JSX JavaScript 版本，不是 TS）。

* npm create vite@latest
npm create xxx@latest 等价于 npm init xxx@latest
会临时下载最新的 create‑vite 脚手架包，执行创建项目，用完自动删掉，不会全局安装。
my‑react‑demo
新项目文件夹名字，生成后本地会多出 ./my‑react‑demo/。
* -- ⚠️很关键
npm 的分隔符：-- 后面的参数，不再交给 npm，全部透传给 create‑vite 脚手架程序。
不加这个 --，后面的 --template 会被 npm 解析，不是传给 vite，会报错。
* --template react
指定模板：
react → React + JavaScript（普通 jsx）
react‑ts → React + TypeScript

```bash
# vue3 js
npm create vite@latest my-vue-demo -- --template vue
# vue3 ts
npm create vite@latest my-vue-ts -- --template vue-ts

npm create vite@latest my‑react‑demo -- --template react
# react ts
npm create vite@latest my-react-ts -- --template react-ts
```