import random
import re
import time
from urllib.parse import urlencode

import requests


def q():
    i = ["56", "49", "56", "47", "52", "2", "72", "76", "51"]
    id = random.choice(i)
    cookie1 = "REDX_2132_nofavfid=1; REDX_2132_smile=1D1; REDX_2132_styleid=7; REDX_2132_saltkey=bG7pUI7c; REDX_2132_lastvisit=1604155117; REDX_2132_auth=bfc5DPKzWkYBkzDIS86jkscwhOHrm9sn3Pcjme%2BxPX2e%2F5JbY1hUbTGvlmyCQ%2BVmEOl1TGXgtftoQmfTjy5n2%2BKZocA; REDX_2132_lastcheckfeed=619687%7C1604202771; REDX_2132_visitedfid=94D2D56D76; REDX_2132_security_cookiereport=edbeMPrljXW8IXVCydsgtCBdBU3NthjLdhDttJWUF8I1OQmcwkjl; REDX_2132_styleuid=619687; REDX_2132_ulastactivity=3faa%2FTpsZV4l8dQQwf1w%2B3AHbZRClI44vK2km8ADXDzbtrPnQvGN; REDX_2132_home_diymode=1; PHPSESSID=sm8mp8bvoqjv5epp8gaeuakue0; REDX_2132_sid=Av359P; REDX_2132_lip=47.103.76.154%2C1605759499; REDX_2132_lastact=1605759516%09plugin.php%09"
    url = "https://www.93book.com/forum-" + str(id) + "-1.html"
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": cookie1,
    }
    res = requests.get(url=url, headers=headers).text
    c = str(res)
    zz = r'<tbody id="normalthread_.+?">(.+?)</tbody>'
    d = str(re.findall(zz, c, re.S))
    zzz = r'mod=redirect&amp;tid=(.+?)&amp;goto=lastpost#lastpost'
    f = re.findall(zzz, d, re.S)
    g = str(f[-1])
    url1 = (
        "https://www.93book.com/forum.php?mod=post&action=reply&fid=" +
        str(id) + "&tid=" + str(g) +
        "&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
    )
    headers1 = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "cookie": cookie1,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    replylist = [
        u"这个帖子不回对不起自己！我想我是一天也不能离开好书友。",
        u"楼主太厉害了！楼主，我觉得好书友真是个好地方！",
        u"楼主发贴辛苦了，谢谢楼主分享！我觉得好书友论坛是注册对了！",
        u"这东西我收了！谢谢楼主！好书友真好！",
        u"我看不错噢 谢谢楼主！好书友越来越好！",
        u"既然你诚信诚意的推荐了，那我就勉为其难的看看吧！好书友不走平凡路。",
        u"其实我一直觉得楼主的品味不错！呵呵！好书友太棒了！",
        u"感谢楼主的无私分享！要想好书友好 就靠你我他",
        u"楼主，大恩不言谢了！好书友是最棒的！",
        u"楼主，我太崇拜你了！我想我是一天也不能离开好书友。",
        u"论坛不能没有像楼主这样的人才啊！我会一直支持好书友。",
    ]
    z = random.choice(replylist)
    data1 = {
        "posttime": str(int(time.time())),
        "formhash": "924c2c59",
        "usesig": "1",
        "message": z,
    }
    data1 = urlencode(data1, encoding="gb2312")
    res1 = requests.post(url=url1, headers=headers1, data=data1).text
    print(res1)


if __name__ == "__main__":
    q()
