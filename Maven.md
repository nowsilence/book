** 手动安装jar包 **

```
输入mvn install:install-file -Dfile=D:\commons-fileupload-1.3.3.jar -DgroupId=commons-fileupload -DartifactId=commons-fileupload -Dversion=1.3.3 -Dpackaging=jar

Dfile:jar包的路径
DgroupId、DartifactId、Dversion可以在下载jar包的页面找到相应信息

在pom.xml同一级目录执行

```