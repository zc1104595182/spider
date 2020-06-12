import json,random,os,math
import re
import time
from img_locate import ImgProcess
import execjs,queue
import requests
from urllib import request
from threading import Thread
from track import get_trace_fast,get_trace_normal,format_track,choice_track_list,choice_track
def get_trace_normal(distance):
    global current_x
    track = [[random.randint(-30, -19), random.randint(-25, -20), 0]]
    track.append([0, 0, 0])

    #random.randint(20, 30)
    step_list = [1,2,3]
    x = 0
    x_list = []
    while True:
        x = x + random.randint(1,4)

        if x < distance:
            x_list.append(x)
        else:
            break
    # x_list.append(distance)


    # x = [(10 / 20) * i for i in range(random.randint(25,35))]
    x = [(10 / 20) * i for i in x_list]
    _y = random.randint(-1, 1)
    current_t = random.randint(-40, -30)
    for _x in x:
        current_x = int(sigmoid(_x, distance))
        _t = random.randint(40,60)
        current_t += _t
        track.append([
            current_x,
            _y,
            current_t
        ])
    track.append([
        current_x,
        _y,
        current_t + random.randint(100, 200)
    ])
    passtime = (track[-1][2]/1000)
    # print(passtime)
    time.sleep(1)
    # print(track)
    return track
# b偏移量
def sigmoid(x, b):
    # t =2
    # return (2/ (2+ math.exp(-x + t))) * b

    t = 8

    s=(2/(2+math.exp(-x+t)))
    return s*b
def spider(data9):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch''rome/83.0.4103.56 Safari/537.36 Edg/83.0.478.33',
                   }
      
        url = 'https://api.shujuling.com/uaa/geetest/pc/register'
        r = requests.get(url,headers=headers,timeout=10)
        with open('mix.js', 'r', encoding='utf-8')as f:
            content = f.read()
        ctx = execjs.compile(content)
        gt = json.loads(r.text)["gt"]
        challenge = json.loads(r.text)["challenge"]
        res = ctx.call('first_w', gt, challenge)
        headers = {
            #'Host': 'api.geetest.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.56 Safari/537.36 Edg/83.0.478.33'
        }
        data = {
            'gt': gt,
            'callback':'geetest_' + str(int(time.time() * 1000))
        }
        session = requests.session()
        r = session.get('https://api.geetest.com/gettype.php',headers=headers, params=data,timeout=10)
        data = {
            'gt': gt,
            'challenge': challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'w': res,
            'callback': 'geetest_' + str(int(time.time() * 1000))
        }
        r = session.get('https://api.geetest.com/get.php',params=data, headers=headers,timeout=10)
        ret_data = re.findall('.*?({.*?})\)',r.text)[0]
        ret_data = json.loads(ret_data)
        sec_w = ctx.call('ajaxphp',gt,challenge,ret_data["data"]["c"],ret_data["data"]["s"])
        data = {
            'gt': gt,
            'challenge': challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'w': sec_w,
            'callback': 'geetest_' + str(int(time.time() * 1000))
        }
        r = session.get('https://api.geetest.com/ajax.php', params=data, headers=headers,timeout=10)
        data = {"is_next":"true",
                "type":"slide3",
                "gt":gt,
                "challenge":challenge,
                "lang":"zh-cn",
                "https":"false",
                "protocol":"https://",
                "offline":"false",
                "product":"embed",
                "api_server":"api.geetest.com",
                "isPC":"true",
                "area":"#geetest-wrap",
                "width":"100%",
                "callback":"geetest_1590163487388"
                }
        r = session.get('https://api.geetest.com/get.php', params=data,headers=headers,timeout=10)
        ret_data = re.findall('.*?({.*?})\)', r.text)[0]
        initData = json.loads(ret_data)
        # 下载图片
        fullbg = str(time.time()) + str(random.random())
        bg = str(time.time()) + str(random.random())
        a1 = "https://static.geetest.com/" + initData["fullbg"]
        a1_con = requests.get(url=a1,timeout=10, headers=headers).content
        a2 = "https://static.geetest.com/" + initData["bg"]
        a2_con = requests.get(url=a2,timeout=10, headers=headers).content
        open("Image/" + fullbg + ".jpg", "wb").write(a1_con)
        open("Image/" + bg + ".jpg", "wb").write(a2_con)

        img_process = ImgProcess()
        img1 = img_process.get_merge_image('Image/' + fullbg + '.jpg')
        img2 = img_process.get_merge_image('Image/' + bg + '.jpg')
        os.remove("Image/" + fullbg + ".jpg")
        os.remove("Image/" + bg + ".jpg")
        distance = int(img_process.get_gap(img1, img2) - 7)
        #arr = choice_track(distance)
        arr = get_trace_normal(distance)
        devarr = []
        t = arr[-1][0]
        n = arr[-1][2]
        for i in range(len(arr)-1):
            devarr.append([arr[i+1][0]-arr[i][0],arr[i+1][1]-arr[i][1],arr[i+1][2]-arr[i][2]])
        three_w = ctx.call('D',arr,devarr,t,n,initData["c"],initData["s"],gt,initData["challenge"])
        data = {
            'gt': gt,
            'challenge': initData["challenge"],
            'lang': 'zh-cn',
            'pt': '0',
            'w': three_w,
            'callback': 'geetest_' + str(int(time.time() * 1000))
        }
        r = session.get('https://api.geetest.com/ajax.php', params=data, headers=headers,timeout=10)
        print(r.text)
q = queue.Queue(100)
if __name__ == "__main__":
    x_list = []
    class Work(Thread):
        def run(self):
            while True:
                spider(q.get())
    for i in range(10):      #控制线程数
        Work().start()
    while True:
        try:
            for conn in range(1,100):
                q.put(conn, timeout=None)
        except Exception as e:
            pass
