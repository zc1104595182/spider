# from db.RedisDb import RedisDb
from db.MongoDb import MongoDBUtil as mongo
from Log import log


class DBInterface:
    def __init__(self, col, input_verify, forVerify, describe):
        self.instance = mongo(col)
        self.inDbVerifyMethod = input_verify
        self.forVerifyMethod = forVerify
        self.describe = describe

    def delect(self):
        log.info('删除无用ip:{}-->{}'.format(self.getDesc(), self.instance.delect()))

    def updata(self, ip, isValid):
        self.instance.updata(ip, isValid)

    def select_all(self):
        return self.instance.select_all()

    def select_all_available_ip(self):
        return self.instance.select_all_available_ip()

    def insert_mongo(self, ip):
        self.instance.insert_mongo(ip)

    def getInputMethod(self):
        return self.inDbVerifyMethod

    def getForVerifyMethod(self):
        return self.forVerifyMethod

    def getDesc(self):
        return self.describe
