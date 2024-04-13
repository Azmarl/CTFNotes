# parse_url()解析漏洞利用

## 1、原理

* 此函数解析一个 URL 并返回一个关联数组，包含在 URL 中出现的各种组成部分。 本函数不是用来验证给定 URL 的合法性的，只是将其分解为下面列出的部分。不完整的 URL 也被接受，parse_url() 会尝试尽量正确地将其解析

```php
<?php
    $url = '//127.0.0.1/user.php?page=php://filter/read=convert.base64-eocode/resource=ffffllllaaaaggg';
	echo $_SERVER['REQUEST_URL'];
    var_dump(parse_url($url));
	print_r(parse_url($_SERVER[‘REQUEST_URI’]));

/user.php?page=php://filter/read=convert.base64-encode/resource=ffffllllaaaaggg

array(3) { ["host"]=> string(9) "127.0.0.1" ["path"]=> string(9) "/user.php" ["query"]=> string(69) "page=php://filter/read=convert.base64-encode/resource=ffffllllaaaaggg" }

Array(["path"]=> string(9) "/user.php" ["query"]=> string(69) "page=php://filter/read=convert.base64-encode/resource=ffffllllaaaaggg")
```

## 2、利用场景和方法

* 如果题目将`parse_url($_SERVER[‘REQUEST_URI’])`的数组值存储并对其中内容进行过滤，那么绕过的方法即为在url中的path前添加`///`（`127.0.0.1/user.php => 127.0.0.1///user.php`）使parse_url解析出错，从而无法进行后续的判断