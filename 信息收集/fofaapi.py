import configparser
import requests
import base64
import urllib3

urllib3.disable_warnings()


def fofare(writetxt, zctxt, zctiltle, tz, mode1):
    readconfig = configparser.ConfigParser()  # 读取配置文件
    readconfig.read('config.ini')
    key = readconfig.get("Fofakey", "key")
    email = readconfig.get("Fofakey", "email")

    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    redata = open(zctxt, 'r+', encoding="utf-8")  # 读取资产
    lines = redata.readlines()

    flag = 1
    for line in lines:
        line = line.replace("\n", "")
        qure = zctiltle + "=" + '"' + line + '"' + "&&" + tz
        print("line:" + str(flag) + "   =====>The current query:" + qure)
        qure = base64.b64encode(qure.encode())

        params = {
            "email": email,
            "key": key,
            "qbase64": qure.decode(),
        }
        fofahttp = "https://fofa.info/api/v1/search/all"
        response = requests.get(fofahttp, verify=False, headers=headers, params=params)
        try:
            hostdata = response.json()["results"]
            writedata(writetxt, hostdata, mode1)
            print("写入成功")
            response.close()
        except:
            print("ERRO:" + response.json())
            response.close()
    redata.close()


def writedata(writetxt, hostdata, mode1):
    f = open(writetxt, 'a+')
    mode1 = int(mode1)
    if mode1 == 0:
        for i in hostdata:
            f.write(i[0] + '\n')
    elif mode1 == 1:
        for i in hostdata:
            f.write(i[1] + '\n')
    elif mode1 == 2:
        for i in hostdata:
            f.write(i[1] + ":" + i[2] + '\n')
    else:
        print("!!!mode错了哦!!!")
    f.close()


if __name__ == '__main__':
    print(''' _____                 __     __    _            _   _            
|  ___|_ _ _   _  ___  \ \   / /_ _| | ___ _ __ | |_(_)_ __   ___ 
| |_ / _` | | | |/ _ \  \ \ / / _` | |/ _ \ '_ \| __| | '_ \ / _ \\
|  _| (_| | |_| |  __/   \ V / (_| | |  __/ | | | |_| | | | |  __/
|_|  \__,_|\__, |\___|    \_/ \__,_|_|\___|_| |_|\__|_|_| |_|\___|
           |___/                                                  ''')
    print("                                             ---(使用前请更改config.ini中的Fofakey)Fofa资产鉴别")
    zcbq = input("输入资产标签(Input Asset Index):")
    zcqd = input("输入资产清单(Input Asset Manifest):")
    ldtz = input("输入漏洞特征(Input Characteristics):")
    scwj = input("输出文件(Output File):")
    mode1 = input("输出格式{仅host:0}{仅IP:1}{IP and Port:2}(Output Mode 0 || 1 || 2):")
    fofare(scwj, zcqd, zcbq, ldtz, mode1)
