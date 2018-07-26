from api import huankuanchaxun
import config
import requests, json, logging
from modle import header_molde


# 还款
def huankuan(num):
    dat = huankuanchaxun.huankuanchxa(num)
    body = chuli(dat)
    data = {}
    data['body'] = body
    data['header'] = header_molde.header_modle('50020')
    header = config.header
    url = config.url['jinjian_url']
    req = requests.post(url, headers=header, data=json.dumps(data))
    if req.status_code == 200:
        req_dict = json.loads(req.text)
        if req_dict['header']['status_code'] == 200:
            logging.warning('还款成功')
            return req_dict
        else:
            logging.warning('还款失败，请求:{}，返回：{}'.format(url, req.text))
            exit()
    else:
        logging.warning('还款失败，请求:{}，返回：{}'.format(url, req.text))
        exit()


def chuli():
    pass


if __name__ == '__main__':
    a = huankuan('21212')
    print(a)
