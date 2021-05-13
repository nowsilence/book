entry
```
import x from "some-npm-package";
console.log(x);
```

config
```
...
output: {
  ...
  globals: {
    // map 'some-npm-package' to 'SomeNPMPackage' global variable
    "some-npm-package": "SomeNPMPackage" // SomeNPMPackagew为全局变量名称
  }
},
external: ["some-npm-package"]
```