import requests


def testBaidu(ip):
    try:
        ip = {
            "https": "https://%s" % (ip),
            "http": "http://%s" % (ip),
        }
        r = requests.get('http://current.ip.16yun.cn:802', proxies=ip, timeout=5)

        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False
