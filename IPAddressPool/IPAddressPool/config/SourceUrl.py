import random
from db.RedisUtils import RedisQueue

urls = [

    r'',    #放第三方代理api
]


# redis = RedisQueue("ip_url")
# for i in urls:
#     redis.put(i)


def getUrl():
    # url = redis.getAll()
    # u = []
    # for i in urls:
    #     u.append(str(i, encoding='utf-8'))
    return urls[random.randint(0, len(urls) - 1)]  # 随机返回urls


if __name__ == '__main__':
    print(getUrl())
