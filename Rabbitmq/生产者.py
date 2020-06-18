# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 15:57
# @Author  : zhangchen
# @Email   : zc15238092914@163.com
# @File    : 生产者.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
from Queue import Queue
from threading import Thread
import json,sys
import pika
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient
client = MongoClient('')
db = client[""]
account1 = db[""]    #生产者表名
import logging
logging.info("Begin")
from logging.handlers import RotatingFileHandler

str_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter(str_fmt)

def spider(data8, channel):
    try:
        data1 = {}
        channel.basic_publish(exchange='', routing_key='队列名字', body=json.dumps(data1))   #把data1   扔进队列
    except Exception, e:
        logger.error(e)


q = Queue(1000)
if __name__ == "__main__":
    class Work(Thread):

        def run(self):
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='',
                                                                           credentials=pika.PlainCredentials(
                                                                               password='',
                                                                               username=''), heartbeat=0))
            channel = connection.channel()
            while True:
                try:
                    d = q.get()
                    spider(d, channel)
                except Exception:
                    pass
    for i in range(8):   #控制线程
        Work().start()

    while True:
        try:
            for conn in account1.find(no_cursor_timeout=True):
                try:
                    q.put(conn, timeout=None)   #从数据库取任务去消费

                except Exception, e:
                    logger.error(e)
                    continue
        except Exception, e:
            logger.error(e)
            pass
