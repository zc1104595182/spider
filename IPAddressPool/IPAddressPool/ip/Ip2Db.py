import threading
from my_pool.Pool_ip import pools

from Log import log


def insert(ip):
    log.info("获取新的ip：{}".format(str(ip)))
    for db in pools:
        threading.Thread(target=insertOne, args=(ip, db.getInputMethod(), db, db.getDesc())).start()


def insertOne(ip, fun, db, sign):
    try:
        if fun(ip):
            db.insert_mongo(ip)
            log.info('入库{}ip:{}'.format(sign, ip))
    except:
        pass
