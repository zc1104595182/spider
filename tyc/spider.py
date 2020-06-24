import os,execjs,random,hashlib,requests,time,json,re
from track import get_track
from ras_str import rsa_js as htmlstr
from userresponse import user_response_str as htmlstr1
from AES import str1 as aes_str
from aes_key import aes_key_str
from aa import aa_str as aa_str
os.environ["EXECJS_RUNTIME"] = "Node"

def run(challenge, gt, c, s, distance, track):
    try:
        # challenge,gt,c,s,distance,track,proxies=get_track()
        #获取userresponse
        js_ctx1=execjs.compile(htmlstr1)
        userresponse1=js_ctx1.call('get_userresponse',distance,challenge)


        #获取aa
        js_ctx2=execjs.compile(aa_str)
        aa1=js_ctx2.call("get_aa",track)
        aa=js_ctx2.call("get_Aa",aa1,c,s)
        #获取passtime
        passtime=track[-1][2]
        #获取以及要提交的字符串
        m2 = hashlib.md5()
        src=(gt+challenge+str(passtime)).encode("utf8")
        m2.update(src)
        rp=m2.hexdigest()
        data='{"userresponse":%s,"passtime":%s,"imgload":%s,"aa":%s,"ep":{"v":"6.0.9"},"rp":%s}'%('"'+userresponse1+'"',passtime,random.randint(300,400),'"'+aa+'"','"'+rp+'"')
        #获取aes的key
        js_ctx3=execjs.compile(aes_key_str)
        key=js_ctx3.call("get_aes")

        #获取rsa加密后的参数
        js_ctx4=execjs.compile(htmlstr)
        e9S=js_ctx4.call("get_rsa",key)

        js_ctx5=execjs.compile(aes_str)
        ciphertext=js_ctx5.call('getCiphertext',data,key)
        words=ciphertext.get("words")
        sigBytes=ciphertext.get("sigBytes")
        byte=js_ctx5.call('getD7W',words,sigBytes)
        aes=js_ctx5.call("get_Aes",byte)

        w=aes+e9S

        millis = int(round(time.time() * 1000))
        url="http://api.geetest.com/ajax.php?gt={}&challenge={}&w={}&callback=geetest_{}".format(gt,challenge,w,millis)
        # print(url)
        headers={
            "Referer":"http://www.ahcredit.gov.cn/index.jspx",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }

        res=requests.get(url,headers=headers,timeout=10)
        pattern_str="geetest_"+str(millis)
        result=json.loads(re.sub(pattern_str,"",res.text).strip("(").strip(")"))
        result['challenge']=challenge
        result['distance']=distance
        return result
    except Exception as e:
        print(e)
        pass










