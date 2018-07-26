import requests
import config
import logging
import json


# 登录
def login(para=config.login_data['admin']):
    url = config.url + '/api/ajaxLoginProcess.htm'
    header = config.header
    s = requests.session()
    req = s.get(url, params=para, headers=header)
    if req.status_code == 200:
        req_dict = json.loads(req.text)
        if req_dict['code'] == 200:
            logging.warning('登录成功')
            return s
        else:
            logging.warning('登录失败，请求:{}，参数{}，返回：{}'.format(url, para, req.text))
            exit()
    else:
        logging.warning('登录失败，请求:{}，参数{}，返回：{}'.format(url, para, req.text))
        exit()


if __name__ == '__main__':
    login()
