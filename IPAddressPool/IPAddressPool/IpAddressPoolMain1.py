import time
import threading
from service.IpService import testIp
from service.IpService import acquire
from service.IpService import deleteIp
import traceback
from Log import log


def main():
    log.info('程序启动')
    try:
        threading.Thread(target=checkIpMain).start()
        threading.Thread(target=updata).start()
    except:
        main()


def updata():
    log.info('更新线程启动！！！')
    while (True):
        try:
            acquire(1)
            time.sleep(6)
        except:
            traceback.print_exc()
            log.error("更新时有异常。。。。")
            time.sleep(2)


def checkIpMain():
    while True:
        try:
            log.info('测试线程执行！！！')
            testIp()
            deleteIp()
            time.sleep(6)
        except:
            traceback.print_exc()
            log.error("测试时有异常。。。。")
            time.sleep(2)


if __name__ == '__main__':
    main()
