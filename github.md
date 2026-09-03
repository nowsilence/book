ping github.com
获取IP，例如20.205.243.166

Mac：
打开/etc/hosts文件，增加一行
20.205.243.166 github.com
sudo killall -HUP mDNSResponder 使其立即生效
Windows:
打开C:\Windows\System32\drivers\etc下的hosts，增加一行
20.205.243.166 github.com
ipconfig /flushdns 刷新DNS缓存

查询IP地址：https://www.ipaddress.com/

‌github.global.ssl.fastly.net是GitHub的CDN域名，主要用于加速全球访问。‌

GitHub使用Fastly提供的CDN（内容分发网络）来加速用户对GitHub网站和资源的访问。
通过使用CDN，GitHub可以将内容缓存到全球各地的节点，从而减少用户访问GitHub时的延迟，提高访问速度和性能。
当用户访问使用CDN加速的GitHub内容时，会从离用户最近的CDN节点获取内容，这有助于提高访问速度和性能‌

clone加速：
原命令：git clone https://github.com/shadcn-ui/ui.git
加速：git clone https://mirror.ghproxy.com/https://github.com/shadcn-ui/ui.git

zip包：https://github.com/shadcn-ui/ui/archive/refs/heads/main.zip
加速：https://mirror.ghproxy.com/https://github.com/shadcn-ui/ui/archive/refs/heads/main.zip

https://gh.llkk.cc/https://github.com/shadcn-ui/ui.git