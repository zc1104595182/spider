import threading
from ip.IpAcquire import acquireIp

from my_pool.Pool_ip import pools

from Log import log


def deleteIp():
    for db in pools:
        db.delect()


def testIp():
    for db in pools:
        threading.Thread(target=testDB, args=(db,)).start()


def testDB(db):
    for i in db.select_all():
        threading.Thread(target=testOne, args=(i, db.getForVerifyMethod(), db, db.getDesc())).start()


def acquire(num):
    for i in range(0, num):
        acquireIp()


def testOne(ip, fun, db, sign):
    if fun(ip):
        db.updata(ip, 1)
    #        print('{}ip:{}有效'.format(sign, ip))
    else:
        db.updata(ip, 0)
        log.info('{}ip:{}不可用'.format(sign, ip))
