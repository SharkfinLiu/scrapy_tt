# -*- coding：uhf-8 -*-
import time
import requests


def test_js():
    cur = (time.time()) * 1000
    url = "http://ct.p5w.net/api/sh/sh/article?keyword=小米&_=" + str(int(cur))

    # res = requests.get(url, headers=headers)
    # print(cur)
    # print(res.text)
    return url


def headers_s():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Content-Length": "72",
        "Content-Type":"application/x-www-form-urlencoded",
        "Host": "ef.zhiweidata.com",
        "Referer":"http: // ef.zhiweidata.com / ",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "X-Requested-With": "	XMLHttpRequest",

    }
    return headers

"""


"Cookie":"Hm_lvt_2ed01d2d0278f62aa71273d3e3eb52b4=1506655129,1506655529,1506655534,1506656611; Hm_lpvt_2ed01d2d0278f62aa71273d3e3eb52b4
=1506665316; eventsMuseum=B15290E2516D110334607089A9CC1F8A"


"""