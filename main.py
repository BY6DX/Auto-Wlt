#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json
import time, schedule, datetime

wltName = None
wltPass = None

# 0: 教育网出口 (国际, 仅用教育网访问, 适合看文献)
# 1: 电信网出口 (国际, 到教育网走教育网)
# 2: 联通网出口 (国际, 到教育网走教育网)
# 3: 电信网出口 2(国际, 到教育网免费地址走教育网)
# 4: 联通网出口 2(国际, 到教育网免费地址走教育网)
# 5: 电信网出口 3(国际, 到教育网走教育网, 到联通走联通)
# 6: 联通网出口 3(国际, 到教育网走教育网, 到电信走电信)
# 7: 教育网国际出口 (国际, 国内使用电信和联通, 国际使用教育网)
# 8: 移动测试国际出口 (国际, 无 P2P 或带宽限制)
wltPort = 0

# 0 for unlimited
wltExp = 0

with open("wlt.json") as fp:
    wltJson = json.load(fp)
    wltName = wltJson["username"]
    wltPass = wltJson["password"]

wltUrl = 'http://wlt.ustc.edu.cn/cgi-bin/ip'

def wltLogin():
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Wlt login attempt")
    payload = {
        'cmd':      'set',
        'exp':      wltExp,
        'name':     wltName,
        'password': wltPass,
        'type':     wltPort,
    }
    r = requests.get(wltUrl, data=payload)

    # NOTE: wlt can return 200 but fail to login when wrong password given
    if r.status_code != requests.codes.ok:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Wlt login requested: Got code {r.status_code}")
    else:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Wlt login requested: Got code {r.status_code}")
        print("NOTE: wlt can return 200 but fail to login when wrong password given")

schedule.every(10).minutes.do(wltLogin)

while True:
    schedule.run_pending()
    time.sleep(5)

