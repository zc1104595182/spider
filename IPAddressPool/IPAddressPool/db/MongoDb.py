# coding = utf - 8
from pymongo import MongoClient
import time
from Log import log


class MongoDBUtil:
    def __init__(self, col,
                 mongo_urls='',    #mongo配置
                 user='',
                 pwd='', dbName=''):
        self.client = MongoClient(mongo_urls)
        self.db_auth = self.client[dbName]
        self.db_auth.authenticate(user, pwd)
        self.db = self.client[dbName]
        self.account = self.db[col]

    def delect(self):
        a = {"isValid": 0}
        x = self.account.delete_many(a)
        return x.deleted_count

    def updata(self, ip, isValid):
        myquery = {"ip": ip}
        newvalues = {"$set": {"isValid": isValid}}
        self.account.update_one(myquery, newvalues)

    def select_all(self):
        all_ip = []
        # "_id": 0, "ip": 1, "isValid": 0, "count": 0
        for x in self.account.find({}, {"_id": 0, "isValid": 0, "count": 0}):
            all_ip.append(x['ip'])
        return all_ip

    def select_all_available_ip(self):
        ip_list = []
        for x in self.account.find({"isValid": 1}, {"_id": 0, "isValid": 0, "count": 0}):
            ip_list.append(x['ip'])
        print(ip_list)
        return ip_list

    def insert_mongo(self, ip):
        mydict = {"_id": ip, "ip": ip, "isValid": 1, "count": 0, "time": time.time()}
        try:
            x = self.account.insert_one(mydict)
        except:
            log.error("重复")
        # print(x)


if __name__ == '__main__':
    # insert_mongo('b')
    # delect()
    pass
