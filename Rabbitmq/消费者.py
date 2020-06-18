# -*- coding:utf-8 -*-
import requests, json, re, arrow, sys, time, threadpool, collections,pika

reload(sys)
sys.setdefaultencoding('utf8')
import Queue
from datetime import datetime
import logging
logging.info("Begin")
from logging.handlers import RotatingFileHandler
str_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter(str_fmt)

def spider2(data8):
    try:
        pass
    except Exception,e:
        logger.error(e)
        raise Noconsumer     #如果业务需要，比如报错了，要把任务仍会队列，则raise Noconsumer

class Noconsumer(Exception):
    pass

def callback(ch, method, propertities, body):

    try:
        spider2(json.loads(body))   #爬虫函数
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Noconsumer as e:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        ch.basic_publish(exchange='', routing_key='队列名字', body=body)
    except Exception:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        ch.basic_publish(exchange='', routing_key='队列名字', body=body)
from threading import Thread

q = Queue.Queue(1000)
if __name__ == "__main__":

    class Work(Thread):
        def run(self):
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='',
                                                                           credentials=pika.PlainCredentials(
                                                                               password='',
                                                                               username='')
                                                                           ,heartbeat=0 ))
            # 建立隧道
            channel = connection.channel()
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume('队列名字', callback, auto_ack=False)
            channel.start_consuming()

    for i in range(8):
        Work().start()