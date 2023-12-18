编译babyloy
编译babylon比较简单，将代码clone下来，在项目根目录执行以下npm命令即可。编译会生成babylon.js.

npm run build:babylonjs
1
运行dev host进行测试
babylon自带了测试工程，其代码在tools/devHost下，可改其代码测试修改的源码。运行以下命令即可启动测试工程：

npm run serve -w @tools/dev-host