#!/usr/bin/env python
# coding=utf8
import sys
from threading import Thread
from pymongo import MongoClient

# 阿里云数据库连接
c = MongoClient("")
db = c['']
account = db[""]
from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_producer import *
from mq_http_sdk.mq_client import *
import time
from queue import Queue

# 初始化 client


# 循环发布多条消息
msg_count = 4
# logging.info("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count))
import logging

logging.info("Begin")
from logging.handlers import RotatingFileHandler

str_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter(str_fmt)


# 传参String
def spider(msg, producer):
    try:
        logger.info(msg)
        msg = TopicMessage(
            # 消息内容
            msg,
            # 消息标签
            ""
        )

        return producer.publish_message(msg)

    except MQExceptionBase as e:
        if e.type == "TopicNotExist":
            logger.info("Topic not exist, please create it.")
            sys.exit(1)
        logger.info("Publish Message Fail. Exception:%s" % e)


q = Queue(1000)
if __name__ == '__main__':
    class Work(Thread):

        def run(self):
            mq_client = MQClient(
                # 设置HTTP接入域名（此处以公共云生产环境为例）
                "",
                # AccessKey 阿里云身份验证，在阿里云服务器管理控制台创建
                "",
                # SecretKey 阿里云身份验证，在阿里云服务器管理控制台创建
                ""
            )

            # 所属的 Topic
            topic_name = ""
            # 您在控制台创建的 Consumer ID(Group ID)
            group_id = ""
            # Topic所属实例ID，默认实例为空None
            instance_id = None

            producer = mq_client.get_producer(instance_id, topic_name)
            while True:
                try:
                    d = q.get()
                    spider(d, producer)
                except Exception:
                    pass

    for i in range(10):    #控制线程数量
        Work().start()
    for conn in account.find(no_cursor_timeout=True):    #遍历数据
        q.put(json.dumps(conn))
        # time.sleep(111111)
