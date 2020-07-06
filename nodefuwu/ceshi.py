# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 17:31
# @Author  : zhangchen
# @Email   : zc15238092914@163.com
# @File    : ip_jianyan1.py
# @Software: PyCharm
#coding=utf-8
import requests,json,re
def deal_js(x3,y3):
    params = {
        "callback":x3,
        "callback2": y3
    }
    clearance = requests.get(url="""http://172.0.0.1:30021/wenshu/jiasuText""", params=params)
    return clearance.text
def get_cookie():
    try:
        headers = {
            'Host': 'www.gsxt.gov.cn',
            'Referer': 'http://www.gsxt.gov.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',

        }

        req = requests.session()
        r = req.get(url="http://www.gsxt.gov.cn/", headers=headers, timeout=8, verify=False,
                    allow_redirects=False)
        __jsluid = r.headers["Set-Cookie"].split(';')[0]
        txt_521 = ''.join(re.findall('<script>(.*?)</script>', r.text))
        if txt_521 != "":
            txt_5211 = txt_521.split('return c}')[0] + "return c}"
            x1 = re.findall('x="(.*?)"', txt_5211)
            y1 = re.findall('y="(.*?)"', txt_5211)
            x2 = str(x1[0]).replace("/@*$/", "").split("@")
            y2 = str(y1[0])
            __jsl_clearance = deal_js(x2, y2)
            __jsl_clearance = __jsl_clearance.split(';')[0]
        return {"jsluid":__jsluid,"clearance":__jsl_clearance}
    except:
        pass
cookie = get_cookie()
print(cookie)
