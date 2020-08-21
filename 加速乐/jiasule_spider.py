import re,json
import time
import queue
import requests

from threading import Thread
from datetime import datetime,timezone, timedelta
import logging
logging.info("Begin")
from logging.handlers import RotatingFileHandler
str_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter(str_fmt)
def deal_clearance(data8):
    #print(data8)
    url = "http://172.0.0.1:6666/jiasule"    #node服务地址
    data = {
        "content": json.dumps(data8),
    }
    ajaxphp_result = requests.post(url=url, data=data).text
    return "__jsl_clearance="+ajaxphp_result
def spider(data9):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        }
        req = requests.session()
        r = req.get(url="http://www.gsxt.gov.cn/", headers=headers,timeout=8, verify=False, allow_redirects=False)
        r.encoding = 'utf-8'
        __jsluid = r.headers["Set-Cookie"].split(';')[0]
        jsCode = ''.join(re.findall('<script>(.*?)</script>', r.text))
        if jsCode:
            json_data = jsCode.split(';go')[1].replace('(','').replace(')','')
            json_data1 = json.loads(json_data)
            __jsl_clearance = deal_clearance(json_data1)
            logger.info(__jsl_clearance)
    except Exception as e:
        logger.error(e)
q = queue.Queue(100)
if __name__ == "__main__":
    class Work(Thread):
        def run(self):
            while True:
                spider(q.get())

    #控制线程数量
    for i in range(2):
        Work().start()
    num1 = 1
    while True:
        try:
            logger.info("第{},次。。。。。。。。。。。。。。。。。".format(num1))
            for conn in range(1,2):

                q.put({"page":conn})

            num1 += 1
            time.sleep(5)
        except Exception as e:
            logger.error(e)

