#coding=utf-8
import sys,requests,time,re,random,json
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from pymongo import MongoClient
import logging
logging.info("Begin")
from logging.handlers import RotatingFileHandler
str_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter(str_fmt)
c=MongoClient("")   #数据库链接
db=c['']            #库名
account1 = db[""]    #表名
def spider(data8):
    try:
        url = "http://credit.customs.gov.cn/ccppserver/ccpp/queryList"
        data = {"manaType":"DEC","apanage":"","depCodeChg":"","tradeType":"ALL","curPage":"{}".format(data8["page"]),"pageSize":20}
        headers = {
            "Referer":"http://credit.customs.gov.cn/ccppwebserver/pages/ccpp/html/declCompany.html",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
        }
        zhuye = requests.post(url=url,json=data,headers=headers,timeout=20)
        zhuye_result = json.loads(zhuye.content)
        if len(zhuye_result["data"]["copInfoList"])>0:
            for info in zhuye_result["data"]["copInfoList"]:
                seqNo = info["seqNo"]
                saicSysNo = info["saicSysNo"]
                companyName = info["nameSaic"]
                #请求详情页面
                detail_data = {"seqNo": "{}".format(seqNo), "saicSysNo": "{}".format(saicSysNo), "queryType": "0", "curPage": 1, "pageSize": 10}
                detail_content = requests.post(url="http://credit.customs.gov.cn/ccppserver/ccpp/queryDetail",json=detail_data,headers=headers,timeout=20)
                detail_content1 = json.loads(detail_content.content)
                if detail_content1["data"]["copInfo"]:
                    detail_content1["_id"] = companyName
                    try:
                        account1.insert_one(detail_content1)
                        logger.info(companyName)
                    except:
                        logger.info("%s,已存在"%(companyName))
    except Exception as e:
        logger.info(e)
from threading import Thread
from queue import Queue
q = Queue(200)
if __name__ == "__main__":
    class Work(Thread):
        def run(self):
            while True:
                spider(q.get())
    for i in range(1):   #控制线程数量
        Work().start()

    while True:
        try:
            for p in range(1,1200):
                q.put({"page":p})
                #account_mouth.remove({"_id": "asc_company"})
            logger.info("休眠5分钟。。。。。。。")
            time.sleep(300)
        except Exception as e:
            logger.error(e)
