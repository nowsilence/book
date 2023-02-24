npm login    //终端打开输入npm login
Username:    //输入npm账号
Password:    //输入npm密码
Email: (this IS public)    //输入注册邮箱
npm publish   //上传至npm


npm unpublish XXX(包名) --force

开发插件配置
"peerDependencies": {
    "three": ">= 0.125.0"
},
"devDependencies": {
    "three": "^0.150.0"
},

dependencies会导致插件包里面有node_modules
"dependencies": {
    "three": "^0.150.0"
},
  