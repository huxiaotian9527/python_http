#!/usr/bin/env python
# coding=utf-8
# @Author: jun_liu@sui.com
# @Date  : 2019/01/09
# @Desc  : 人事服务平台-工时提交,总工时计算

import time
import datetime
import requests


class WeekPlan(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.session.post(url="http://weekplan.sui.work/weekplan/loginCheck", data=f"username={self.username}&password={self.password}&type=1", headers=self.headers)

    def datetime_timestamp(self, dt):
        ft = '%Y-%m-%d %H:%M'
        time.strptime(dt, ft)
        s = time.mktime(time.strptime(dt, ft))

        return str(s).split(".")[0]

    def next_day(self, days=7):
        init_day = datetime.datetime(2018, 6, 4, 8, 0, 0, 0)
        next_d = init_day + datetime.timedelta(days=days)

        return self.datetime_timestamp(next_d.strftime("%Y-%m-%d %H:%M"))

    def working_hours(self):
        all_days = int((datetime.datetime.now() - datetime.datetime(2018, 6, 4)).days)
        all_monday = [self.next_day(x) for x in range(0, all_days) if x % 7 == 0]
        all_time = 0
        for monday in all_monday:
            url = f"http://weekplan.sui.work/weekplan/workhour/add/query?date={monday}"
            for x in self.session.get(url=url).json():
                if x.get("timeout"):
                    print(x)
                all_time += float(x["timeout"])

        print(f"截止到本周,总工时(小时): {all_time}")

    def do_work(self, work_dic):
        data = f"""data[0][start]={self.datetime_timestamp(f'{work_dic["date_str"]} {work_dic["start_time"]}')}&data[0][finish]={self.datetime_timestamp(f'{work_dic["date_str"]} {work_dic["finish_time"]}')}&data[0][do]={work_dic["do_str"]}&data[0][timeout]={work_dic["timeout"]}&data[0][date]={self.datetime_timestamp(f'{work_dic["date_str"]} 00:00')}"""
        url = "http://weekplan.sui.work/weekplan/workhour/add/form"
        res = self.session.post(data=data.encode("utf-8"), url=url, headers=self.headers)
        if "添加成功" in eval(res.text):
            print(f"提交成功,详细信息: {work_dic}")
        else:
            print("执行异常,请检查提交数据和用户名账号密码是否正确!")


if __name__ == '__main__':
    # 初始化: 用户名, 密码
    # plan = WeekPlan("xiaoqiang_zhang", "ZhangXQ@2018@")
    # plan = WeekPlan("zhongchao_chen2", "Tyz6683983czc")
    plan = WeekPlan("tiantian_hu", "Hu_1234567")
    plan.working_hours()

    # 提交工时参数,谨慎修改
    work_dic = {
        "date_str": "2019-04-19",
        "start_time": "19:00",
        "finish_time": "21:30",
        "timeout": "2.5",
        "do_str": "版本上线",
    }
    # plan.do_work(work_dic)
