# Web常识

1. session的存放目录为`/runtime/session/xxx`
1. 可以通过故意访问不存在的目录来通过报错获取网站的框架
1. 存放flag的文件一般就是flag
1. POST传参优先级高于GET，如果参数名称相同，POST的值会覆盖FET的值，可以用于部分绕过
1. eval()函数在PHP和js里都有，可以用`Error().stack`测试判断到底是什么语言
1. 可以通过vm.js、VM.run等语句判断vm2沙箱
1. 不知道flag在哪时可以`system("env");`看看环境变量
1. 网站观察源码没收获的时候可以目录扫描和抓包获取信息，通过文件泄露和隐藏传参获取信息
1. SQL联合查询时可以查询和group_concat多个值用逗号隔开