
import requests,json,re
from track import get_track
from spider import run
import hashlib

def md5(str):
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5

def clean_data(string):
    pattern = re.compile("<.*?>|\n|\t|\r| |,")
    res = re.sub(pattern, "", string)
    return res

def spiders(zhanghao,mima):
    try:
        ses=requests.session()
        headers = {
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Content-Length":"24",
            "Content-Type":"application/json; charset=UTF-8",
            "Host":"www.tianyancha.com",
            "Origin":"https://www.tianyancha.com",
            "Pragma":"no-cache",
            "Referer":"https://www.tianyancha.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
        }
        url='https://www.tianyancha.com/verify/geetest.xhtml'
        data = {"uuid":"1592968082445"}
        res=ses.post(url,headers=headers,json=data,timeout=15)
        json_res=json.loads(res.text)
        gt=json_res["data"]["gt"]
        challenge1=json_res["data"]["challenge"]
        challenge, gt, c, s, distance, track=get_track(challenge1,gt,ses)
        result=run(challenge, gt, c, s, distance, track)
        challenge1 = result["challenge"]
        validate = result["validate"]
        print(result)
        data1  ={"mobile":"{}".format(zhanghao),"cdpassword":"{}".format(md5(mima)),"loginway":"PL","autoLogin":False,"challenge":"{}".format(challenge1),"validate":"{}".format(validate),"seccode":"{}|jordan".format(validate)}
        login = ses.post(url="https://www.tianyancha.com/cd/login.json",json=data1,headers=headers,timeout=15)
        print(login.text)
    except Exception as e:
        print(e)
import queue
from threading import Thread
q = queue.Queue(1000)
if __name__ == "__main__":
    #nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    #print(nowTime)
    zhanghao = input("请输入账号:")
    mima = input("请输入密码:")
    spiders(zhanghao,mima)

