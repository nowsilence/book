
# watch 的第一个参数，支持 3 种类型：ref、reactive 代理对象、getter 函数。

```javascript

/**  监听 ref对象 **/
const count = ref(0)
watch(count, (newVal,oldVal)=>{
  console.log(newVal)
})

const objRef = ref({name:'a'})
watch(objRef,(n)=>{
  console.log(n)
}, {deep:true})

/**  watch 直接传 reactive 实例，默认自动开启 deep，不需要写deep:true **/
const state = reactive({
  name:'张三',
  info:{age:18}
})

watch(state,(newVal)=>{
  console.log('state变化',newVal)
})

// 只监听某一个属性，需要写成getter函数, 直接 watch(state.name,fn) ❌错误，必须用函数 ()=> state.name
// 直接写 watch(state.age, callback)，传进去的不是响应式源，而是普通原始值。
watch(() => state.info.age, (n)=>{
  console.log('age变了',n)
})

/** 监听computed **/
const count = ref(1)
const double = computed(()=>count.value * 2)

// ✅直接监听computed
watch(double, (newVal)=>{
  console.log('计算值变化', newVal)
})
```