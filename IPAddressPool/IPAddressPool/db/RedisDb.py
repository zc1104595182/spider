from db.RedisUtils import RedisQueue as queue


class RedisDb:
    def __init__(self, col, db=10, host='', port=''):   #redis配置
        self.col = col
        self.available = queue(col, db=db, host=host, port=port)
        self.notAvailable = queue(col + "_not", db=db, host=host, port=port)

    def delect(self):
        return self.notAvailable.clear()

    def updata(self, ip, isValid):
        if isValid == 1:  # 有效
            self.available.put(ip)
            if self.notAvailable.has(ip):
                self.notAvailable.delete(ip)
        else:
            self.notAvailable.put(ip)
            if self.available.has(ip):
                self.available.delete(ip)

    def select_all(self):
        return self.available.getAll().union(self.notAvailable.getAll())

    def select_all_available_ip(self):
        return self.available.getAll()

    def insert_mongo(self, ip):
        self.available.put(ip)
