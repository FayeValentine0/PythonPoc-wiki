import configparser
import requests
import urllib3

urllib3.disable_warnings()


def aqcapi(name, output, page):
    fileopen = open(output, "w+",encoding="utf-8")
    flag = 0
    readconfig = configparser.RawConfigParser()  # 读取配置文件
    readconfig.read('config.ini')
    Cookie = readconfig.get('QUAKEkey', 'Cookie')

    url = "https://aiqicha.baidu.com/icpsearch/sAjax"  # url编码
    header = {
        "X-QuakeToken": "用户API Key"
    }

    qure = "变量:"+ "变量读取"   #if判断id mode 为1时为命令行模式直接拼接qure，为0时则读取文件与查询标签
    data = {
        "query": qure,
        "start": 0,
        "size": 10
    }
    response = requests.post(url="https://quake.360.net/api/v3/search/quake_service", headers=headers, json=data)
    print(response.json())

    for qure in readzc(name):
        for o in range(int(page)):
            qure = qure.replace("\n", "")
            data = {
                "query": "port: 443",
                "start": 0,
                "size": 10
            }

            requestsdata = requests.get(url=url, headers=header, params=quredict)
            if requestsdata.json():
                try:
                    quredata = requestsdata.json()["data"]["resultList"]
                    for i in range(len(quredata)):
                        fromdata = quredata[i]
                        for j in fromdata["domainName"]:
                            if j.rfind('</em>') == -1:
                                fileopen.write(j + '\n')
                            else:
                                print("<em></em>文本不写入")
                except:
                    print("当前资产【 " + qure + " 】无相关信息")
        flag = flag + 1
        print("line: " + str(flag) + " ===>>>当前资产【 " + qure + " 】查询并写入成功!")
    fileopen.close()


def readzc(name):
    f = open(name, "r+", encoding='utf-8')
    linesdata = f.readlines()
    f.close()
    return linesdata


if __name__ == '__main__':
    print('''    ______      
   / ____/___ ___  _____  
  / /_  / __ `/ / / / _ \ 
 / __/ / /_/ / /_/ /  __/ 
/_/    \__,_/\__, /\___/  
        /____/
            --by Faye Valentine
''')
    zcqd = input("输入资产清单(Input Asset Manifest):")
    scwj = input("输出文件(Output File):")
    page = input("爬取页数(Page):")
    aqcapi(zcqd, scwj, page)
