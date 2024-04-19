```
#设置淘宝镜像#
npm config set registry http://registry.npm.taobao.org/


#恢复镜像#
npm config set registry https://registry.npmjs.org/


npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm是什么？
简单的讲就是中国版的NPM，因为npm安装插件是从国外服务器下载，受网络影响大，可能出现异常，所以我们乐于分享的淘宝团队干了这事。

这是一个完整 npmjs.org 镜像，你可以用此代替官方版本(只读)，同步频率目前为 10分钟 一次以保证尽量与官方服务同步。—来自淘宝 NPM 镜像


百度和谷歌搜索，各种换源加代理都没解决。 最后找到了https://npmmirror.com/这个网站，根据指导，安装定制的cnpm管理工具npm install -g cnpm --registry=https://registry.npmmirror.com
然后执行cnpm install –save-dev electron 成功了。


```