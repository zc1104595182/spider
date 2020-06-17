#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class RedisQueue(object):
    def __init__(self, name, db=14, host='', port=''):   #redis配置
        pool_db = redis.ConnectionPool(host=host, port=port, db=db)
        self.r_db = redis.Redis(connection_pool=pool_db)
        self.key = name

    def size(self):
        return self.r_db.scard(self.key)  # 返回里面set内元素的数量

    def has(self, value):
        return self.r_db.sismember(self.key, str(value))  # 判断value是否在set集合里

    def put(self, item):
        self.r_db.sadd(self.key, str(item))  # 添加新元素

    def pop(self):
        # 直接返回队列第一个元素，如果队列为空返回的是None
        item = self.r_db.spop(self.key)
        return str(item, encoding='utf-8')

    def delete(self, item):
        self.r_db.srem(self.key, item)

    def clear(self):
        # 清空集合中的所有元素
        li = []
        for i in range(self.size()):
            li.append(self.pop())
        return li

    def getAll(self):
        return self.r_db.smembers(self.key)
