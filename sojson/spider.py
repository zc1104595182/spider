import requests,re,execjs



def get_url(s, headers):
    url_1 = 'http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html'
    response = s.get(url_1, headers=headers)
    js = re.findall('<script type="text/javascript">(.*?)</script>',response.content.decode(),re.S|re.M)[0]
    ll = re.sub("window\[_0x56ae\('0x3c','\)9A&'\)\]=_0x35ace3;", "return _0x35ace3;", js)
    ctx = execjs.compile(ll)
    href = ctx.call('_0x33f22a')
    print(href)

    return href



if __name__ == '__main__':
    s = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    }

    href = get_url(s, headers)
    url = "http://www.pbc.gov.cn"+href
    zhuye = s.get(url=url,headers=headers)
    print(zhuye.content.decode())