# Proxy

## 属性拦截

错误写法：

```js
const target = {
  _name: 'Alice',
  get name() {
    console.log('getter this === proxy ?', this === proxy);
    return this._name;
  }
};

const proxy = new Proxy(target, {
  get(target, key, receiver) {
    console.log('trap:', key);
    return target[key]; // 直接取
  }
});

console.log(proxy.name);
```
输出：
trap: name
getter this === proxy ? false
Alice

这里 name 的 getter 里，this 指向的是 target，不是 proxy。
所以 getter 里面如果再访问 this.xxx，就绕过 Proxy 了。

正确写法：
```js
const target = {
  _name: 'Alice',
  get name() {
    console.log('getter this === proxy ?', this === proxy);
    return this._name;
  }
};

const proxy = new Proxy(target, {
  get(target, key, receiver) {
    console.log('trap:', key);
    return Reflect.get(target, key, receiver);
  }
});

console.log(proxy.name);
```
输出：
trap: name
getter this === proxy ? true
trap: _name
Alice

## 函数拦截

```js
const obj = {
  name: 'Nigel',
  say(msg) {
    console.log(this.name + ': ' + msg);
    return 'done';
  }
};

const proxy = new Proxy(obj, {
  get(target, key, receiver) {
    const value = Reflect.get(target, key, receiver);

    if (typeof value !== 'function') {
      return value;
    }

    return function (...args) {
      console.log('before:', String(key), args);

      const result = Reflect.apply(value, this, args);

      console.log('after:', String(key), result);
      return result;
    };
  }
});

proxy.say('hello');
```