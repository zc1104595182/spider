import requests,json,random,time,os,math
from img_locate import ImgProcess




def get_track(challenge,gt,ses):
    headers={
        "Referer":"http://218.22.14.70/gsxt/index.jspx",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    # url='http://www.ahcredit.gov.cn/registerValidate.jspx'
    # response=json.loads(requests.get(url,headers=headers,proxies=proxies,timeout=10).text)
    # challenge=response.get("challenge")
    # gt=response.get("gt")
    t1=int(time.time())
    uri = "gt=" + gt + \
          "&challenge=" + challenge + \
          "&width=100%&product=float&offline=false&protocol=https://&voice=/static/js/voice.1.1.3.js" \
          "&type=slide&pencil=/static/js/pencil.1.0.1.js&path=/static/js/geetest.6.0.9.js&callback=geetest_{}".format(t1)
    response1 = ses.get("https://api.geetest.com/get.php?" + uri,headers=headers,timeout=10)
    initData = json.loads(response1.text.replace("_"+str(t1),"").replace("geetest(", "")[:-1])
    challenge1=initData.get("challenge")
    c=initData.get("c")
    s=initData.get("s")

    # 下载图片
    fullbg = str(time.time()) + str(random.random())
    bg = str(time.time()) + str(random.random())
    open("Image/" + fullbg + ".jpg", "wb").write(requests.get("https://static.geetest.com/" + initData["fullbg"],timeout=10,headers=headers).content)
    open("Image/" + bg + ".jpg", "wb").write(requests.get("https://static.geetest.com/" + initData["bg"],timeout=10,headers=headers).content)

    img_process = ImgProcess()
    img1 = img_process.get_merge_image('Image/' + fullbg + '.jpg')
    img2 = img_process.get_merge_image('Image/' + bg + '.jpg')
    os.remove("Image/" + fullbg + ".jpg")
    os.remove("Image/" + bg + ".jpg")
    distance = int(img_process.get_gap(img1, img2) - 7)

    track=get_trace_normal(distance)
    return challenge1,gt,c,s,distance,track

# def get_trace_normal(distance):
#     global current_x
#     track = [[random.randint(-30, -19), random.randint(-25, -20), 0]]
#     track.append([0, 0, 0])
#
#     #random.randint(20, 30)
#     x = [(10/20) * i for i in range(int(distance/3)*2)]
#     # x = [(10 / 20) * i for i in range(random.randint(25,35))]
#     # x = [(10 / 20) * i for i in range(20)]
#     _y = random.randint(-1, 1)
#     current_t = random.randint(-30, -20)
#     for _x in x:
#         current_x = int(sigmoid(_x, distance))
#         _t = random.randint(30,50)
#         current_t += _t
#         track.append([
#             current_x,
#             _y,
#             current_t
#         ])
#     track.append([
#         current_x,
#         _y,
#         current_t + random.randint(200, 300)
#     ])
#     passtime = (track[-1][2]/1200)
#     # print(passtime)
#     # print(track)
#     time.sleep(passtime)
#     return track
#
#
# # b偏移量
# def sigmoid(x, b):
#     t =4
#     return (1/(1+ math.exp(-x + t))) * b

# def get_trace_normal(distance):
#     global current_x
#     track = [[random.randint(-30, -19), random.randint(-25, -20), 0]]
#     track.append([0, 0, 0])
#
#     #random.randint(20, 30)
#     x = [(10/20) * i for i in range(int(distance/2)-2)]
#     # x = [(10 / 20) * i for i in range(random.randint(25,35))]
#     # x = [(10 / 20) * i for i in range(20)]
#     _y = random.randint(-1, 1)
#     current_t = random.randint(50, 60)
#     for _x in x:
#         current_x = int(sigmoid(_x, distance))
#         _t = random.randint(40,60)
#         current_t += _t
#         track.append([
#             current_x,
#             _y,
#             current_t
#         ])
#     track.append([
#         current_x,
#         _y,
#         current_t + random.randint(200, 300)
#     ])
#     passtime = (track[-1][2]/1000)
#     # print(passtime)
#     # print(track)
#     time.sleep(passtime)
#     # print(track)
#     return track
#
#
# # b偏移量
# def sigmoid(x, b):
#     # t =2
#     # return (2/ (2+ math.exp(-x + t))) * b
#
#     t = 6
#     return (4/ (4 + math.exp(-x + t))) * b

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