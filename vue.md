Suspense/onServerPrefetch

在setup里使用await会警告，导致不加载，如果确要使用有两种方式：
1、在父组件里使用Suspense组件包裹子组件
2、使用onServerPrefetch，如果仅在服务端渲染时才需要加载，则使用此方法
```js
onServerPrefetch(async () => {
  await store.loadList(page.value, pageSize)
})
```