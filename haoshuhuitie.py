import time

import requests


def q():
    url = 'https://www.93book.com/plugin.php?id=it618_award:ajax&ac=getaward&formhash=924c2c59&_=' + str(
        int(time.time()))
    url1 = 'https://www.93book.com/plugin.php?id=it618_award:ajax&formhash=37446b4c&ac=getcredits'
    cookie = 'REDX_2132_nofavfid=1; REDX_2132_smile=1D1; REDX_2132_styleid=7; REDX_2132_saltkey=bG7pUI7c; REDX_2132_lastvisit=1604155117; REDX_2132_auth=bfc5DPKzWkYBkzDIS86jkscwhOHrm9sn3Pcjme%2BxPX2e%2F5JbY1hUbTGvlmyCQ%2BVmEOl1TGXgtftoQmfTjy5n2%2BKZocA; REDX_2132_lastcheckfeed=619687%7C1604202771; REDX_2132_visitedfid=94D2D56D76; REDX_2132_security_cookiereport=edbeMPrljXW8IXVCydsgtCBdBU3NthjLdhDttJWUF8I1OQmcwkjl; REDX_2132_styleuid=619687; REDX_2132_ulastactivity=3faa%2FTpsZV4l8dQQwf1w%2B3AHbZRClI44vK2km8ADXDzbtrPnQvGN; REDX_2132_home_diymode=1; PHPSESSID=sm8mp8bvoqjv5epp8gaeuakue0; REDX_2132_sid=Av359P; REDX_2132_lip=47.103.76.154%2C1605759499; REDX_2132_lastact=1605759516%09plugin.php%09'
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'cookie': cookie
    }
    res = requests.get(url=url, headers=headers).text
    res1 = requests.get(url=url1, headers=headers).text
    print(res1)


for i in range(100):
    q()
