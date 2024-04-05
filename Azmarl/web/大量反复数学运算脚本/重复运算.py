import requests,time,re

url = "http://e749f54d-60da-47e0-adfd-a21f7770cc72.node5.buuoj.cn:81/index.php"
req = requests.session()    #保持会话
getRe = req.get(url)    #get请求
getRe.encoding = "UTF-8"    #将返回的结果用UTF-8编码，不然会返回乱码
reContent = re.findall("[0-9]* [-+*/] [0-9]*",getRe.text)   #提取表达式。math和search正则只会匹配一次，findall会一直匹配
formula = ''.join(reContent).replace(" ", "")   #提取表达式
comResult = eval(formula)   #eval执行一个表达式
print(comResult)    
data = {"answer":comResult}
postRe = req.post(url,data)
postRe.encoding = "UTF-8"
print(postRe.text)

for i in range(1005):   #多运行几次，避免其中的请求失败
    reContent = re.findall("[0-9]* [-+*/] [0-9]*",postRe.text)
    formula = ''.join(reContent).replace(" ", "")
    comResult = eval(formula)
    print(comResult)
    data = {"answer":comResult}
    postRe = req.post(url,data)
    postRe.encoding = "UTF-8"
    time.sleep(0.1)		#请求太快会被禁掉
    print(postRe.text) 
