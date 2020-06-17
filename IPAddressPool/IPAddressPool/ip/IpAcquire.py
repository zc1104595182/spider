from config.SourceUrl import getUrl
from ip.Ip2Db import insert
import threading
import requests
from Log import log

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def acquireIp():
    aUrl = getUrl()
    log.info('获取ip地址:{}'.format(aUrl))
    try:
        reponse = requests.get(aUrl, headers=header, timeout=5)
        if reponse.status_code == 200:
            parseHtml(reponse.text)
    except:
        # traceback.print_exc()
        log.error('请求ip异常:{}'.format(aUrl))


def parseHtml(html):
    html = html.replace('\'', '').replace('b', '').replace('<r/>', '').replace('\r', '')
    ips = html.split("\n")
    for ip in ips:
        ip = ip.strip()
        if 'false' in ip:
            log.war('您的套餐今日已到达上限')
            return
        elif '' == ip:
            return
        else:
            if '.' in ip:
                threading.Thread(target=insert, args=(ip,)).start()
