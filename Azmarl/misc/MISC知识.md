# MISC知识

## 1、命令

1. `ren * *.jpg`：把当前目录下所有文件后缀修改为.xxx

## 2、工具网站

1. 标准中文电码查询：https://apps.chasedream.com/chinese-commercial-code/
   1. 中文编码eg：0086 1562 2535 5174   人工智能
2. 五笔输入法编码：[五笔输入法编码在线查询系统.汉字转拼音 (zd9999.com)](http://www.zd9999.com/wb/search.asp)

## 3、关系知识点

1. administrator是windows操作系统管理员用户，如果有提示有关administrator，猜测应该和用户密码有关
   * dmp文件是windows系统中的错误转储文件，当Windows发生错误蓝屏的时候，系统将当前内存【含虚拟内存】中的数据直接写到文件中去，方便定位故障原因，而里面包含主机用户密码信息
2. 如果base64解码出来是Salted文件，那么应该是`AES`或者`3DES`加密