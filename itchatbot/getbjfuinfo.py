# -*- coding: utf-8 -*-
# author: Chan

import requests
from bs4 import BeautifulSoup
import time

url_start = 'http://newjwxt.bjfu.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL'  # GET
url_main = 'http://newjwxt.bjfu.edu.cn/jsxsd/framework/xsMain.jsp'  # GET
url_login = 'http://newjwxt.bjfu.edu.cn/jsxsd/xk/LoginToXk'  # POST
url_classes = 'http://newjwxt.bjfu.edu.cn/jsxsd/xskb/xskb_list.do'

num = {
    "1": "DCE888360E8F4C2587C7EA77AEF8984D-",
    "2": "5B4FD4964CC34B838A4605BDE2339AAE-",
    "3": "FB9A9C19924C47ABBD9DCBE9DD4CDB5A-",
    "4": "509B500DA0964DF88D32333D1EB47F32-",
    "5": "297455C8C0DF4DD89A1B1F517930AA2A-"
}

Weekday = {
    "Mon": "1-2",
    "Tue": "2-2",
    "Wed": "3-2",
    "Thu": "4-2",
    "Fri": "5-2",
    "Sat": "6-2",
    "Sun": "7-2"
}

Weekday_num = {
    "1": "1-2",
    "2": "2-2",
    "3": "3-2",
    "4": "4-2",
    "5": "5-2",
    "6": "6-2",
    "7": "7-2"
}

weekday_alpha = {
    "1": "Mon.",
    "2": "Tue.",
    "3": "Wed.",
    "4": "Thu.",
    "5": "Fri.",
    "6": "Sat.",
    "7": "Sun."
}

class_num = {
    "1": "12节:",
    "2": "34节:",
    "3": "56节:",
    "4": "78节:",
    "5": "910节:"
}

starttime = [2018, 3, 4]


class newjwxt(object):
    def __init__(self):

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'newjwxt.bjfu.edu.cn',
            'Referer': 'http://newjwxt.bjfu.edu.cn/Logon.do?method=logon',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.get(url_start)

    def login(self, chat_id,username,password):
        postdata = {
            'USERNAME': username,
            'PASSWORD': password
        }
        # print(postdata)
        self.session.post(url_login, data=postdata)
        return self.session.get(url_main).status_code
        # print("登录成功")

    def info(self, chat_id):
        r = self.session.get(url_main)
        # print(r.text)
        soup = BeautifulSoup(r.content, "html.parser")
        basic_info = soup.find_all("div", {"class": "Nsb_top_menu_nc"})
        info = basic_info[0].text.strip()
        # print(info)
        return info

    def get_classes(self, delta, weekday):
        localtime = time.localtime()
        # delta = int(
        #     (((localtime[1]-starttime[1])*30+(localtime[2]-starttime[2]))/7)+1)
        courses = {}
        cur_courses = {}
        t = 0
        r = self.session.get(url_classes)
        # print(r.text)
        soup = BeautifulSoup(r.content, "html.parser")
        for z in range(1, 6):
            id = num[str(z)] + weekday  # "4-2"
            Classes = soup.find_all("div", {"id": id})
            # print(Classes)
            if '---------------------' in Classes[0]:
                classes = Classes[0].text.replace(
                    '---------------------', '@').replace(",", "&").split('@')
            else:
                classes = [Classes[0].text.strip().replace(",", "&")
                           ]  # .split(',')
            # print(classes)
            l = len(classes)
            if classes == ['']:
                # print("今天没有课!")
                t = t+1
                if t == 5:
                    cur_courses.clear()
                    return cur_courses
                # pass
            Weeks = Classes[0].find_all("font", {"title": "周次(节次)"})
            L = len(Weeks)
            for i in range(0, l):
                try:
                    classes[i] = class_num[str(z)]+classes[i]
                    weeks = Weeks[i].text.replace("(周)", "").split(",")
                    w = []
                    for parts in weeks:
                        if '-' in parts:
                            part_infos = parts.split("-")
                            week_start = int(part_infos[0])
                            week_end = int(part_infos[1])
                            for week in range(week_start, week_end+1):
                                w.append(week)
                        else:
                            part_infos = parts.split(",")
                            for part in part_infos:
                                w.append(int(part))
                    W = repr(w)
                    # print(W)
                    courses[W] = classes[i]
                except:
                    pass
        # print(courses)
        for key in courses.keys():
            if str(delta) in key:
                # print(courses[key])
                cur_courses[key] = courses[key]
        return cur_courses