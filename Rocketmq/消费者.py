# coding=utf8
import time
from queue import Queue
from threading import Thread
import logging

logging.info("Begin")
from logging.handlers import RotatingFileHandler

str_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter(str_fmt)
from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_consumer import *
from mq_http_sdk.mq_client import *

q = Queue(256)

def spider(data,producer):
    try:

        #生产逻辑
        logger.info(data)
        # 这里出错把消息扔回队列
        pass
    except Exception as e:
        logger.error(e)
        deal_error(data,producer)

#报错处理，如果报错扔回队列
def deal_error(data,producer):
    producer.publish_message(data)

if __name__ == '__main__':
    class Worker(Thread):
        def run(self) -> None:
            while True:
                data = q.get()
                if data is None:
                    q.put(None)
                    break
                spider(data,producer)


    # 设置消费者消费
    consume_num = 16
    for i in range(10):    #控制线程数量
        Worker().start()
    # 初始化 client
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

    consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
    producer = mq_client.get_producer(instance_id, topic_name)
    # 长轮询表示如果topic没有消息则请求会在服务端挂住3s，3s内如果有消息可以消费则立即返回
    # 长轮询时间3秒（最多可设置为30秒）
    wait_seconds = 3
    # 一次最多消费3条(最多可设置为16条)
    batch = 16
    logger.info(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n"
                 % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
    while True:
        try:
            # 长轮询消费消息
            recv_msgs = consumer.consume_message(batch, wait_seconds)
            for msg in recv_msgs:
                data = msg.message_body
                spider(data,producer)
        except MQExceptionBase as e:
            if e.type == "MessageNotExist":
                logger.info(("No new message! RequestId: %s" % e.req_id))
                continue

            logger.info(("Consume Message Fail! Exception:%s\n" % e))
            time.sleep(2)
            continue

        # msg.next_consume_time前若不确认消息消费成功，则消息会重复消费
        # 消息句柄有时间戳，同一条消息每次消费拿到的都不一样
        try:
            receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
            consumer.ack_message(receipt_handle_list)
            logger.info(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
        except MQExceptionBase as e:
            logger.info(("\nAk Message Fail! Exception:%s" % e))
            # 某些消息的句柄可能超时了会导致确认不成功
            if e.sub_errors:
                for sub_error in e.sub_errors:
                    logger.info(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                                 (sub_error["ReceiptHandle"], sub_error["ErrorCode"], sub_error["ErrorMessage"])))
