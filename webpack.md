mkdir filename
cd filename
npm init
npm i webpack webpack-cli -D
npm i html-webpack-plugin -D
npm i webpack-merge -D
npm i clean-webpack-plugin -D
npm i babel-loader -D
npm i @babel/core @babel/preset-env -D
npm i @babel/plugin-transform-runtime -D
npm i @babel/plugin-proposal-class-properties -D
npm i webpack-dev-server -D



@babel/plugin-transform-runtime
babel默认只转换新的 JavaScript 语法，比如箭头函数、spread。
不转换新的 API，例如Iterator、Generator、Set、Maps、Proxy、Reflect、Symbol、Promise 等全局对象
类型插件有： .babel-polyfill、babel-runtime

npm i @babel/plugin-proposal-class-properties -D

{
  "plugins": [
    ["@babel/plugin-proposal-class-properties", { "loose": true }]
  ]
}
options
loose：boolean，默认为false
当loose设置为true，代码被以赋值表达式的形式编译，否则，代码以Object.defineProperty来编译。
class A{
	foo!: string
	bar: string = "bar";
	static rogen = "rogen";
}


babel-plugin-transform-decorators-legacy
装饰器


@babel/plugin-proposal-optional-chaining
可选链 ？
配置
{
  "plugins": ["@babel/plugin-proposal-optional-chaining"]
}


babel-plugin-syntax-dynamic-import
用以解析识别import()动态导入语法---并非转换，而是解析识别
{
  "plugins": ["syntax-dynamic-import"]
}

import('./a.js').then(()=>{
  console.log('a.js is loaded dynamically');
});


.babelrc
{
    "plugins": [
        "@babel/plugin-transform-runtime",

        /*
            loose
            boolean, 默认是false
            当为false的时候, 属性会通过Object.defineProperty的方式为对象赋值, 为true的时候, 直接通过点语法赋值
            class A{
                foo!: string
                bar: string = "bar";
                static rogen = "rogen";
            }

            参数 loose = true 编译后得效果

            class A{
                construtor(){
                    this.foo = void 0 
                    this.bar = 'bar'
                }
            }
            A.rogen = 'rogen'

            参数 loose = false 编译后得效果


            function _defineProperty(obj, key, value) { 
                if (key in obj) { 
                    Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); 
                } else { 
                    obj[key] = value; 
                }
                return obj; 
            }

            class A{
                construtor(){
                    _defineProperty(this, "bar", "rogen");
                    _defineProperty(this, "foo", void 0);
                }
            }
            _defineProperty(A, "rogen", "rogen");
        */
        ["@babel/plugin-proposal-class-properties", { "loose": true }],
        ["transform-decorators-legacy"]
    ],
    "preset": [
        [
            '@babel/preset-env', // 转译包,主要对 JavaScript 最新的语法糖进行编译，并不负责转译新增的 API 和全局对象。
            {
                "modules": false // 以前我们需要使用babel来将ES6的模块语法转换为AMD, CommonJS，UMD之类的模块化标准语法，但是现在webpack都帮我做了这件事了，所以我们不需要babel来做，因此需要在babel配置项中设置modules为false，因为它默认值是commonjs, 否则的话，会产生冲突。
            }
        ]
    ]
}

package.json
{
    "scripts": {
    "build":"webpack --mode development -w", // 自动打包
    },
}