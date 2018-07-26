import config
from modle import dzzhkl_molde
import json, logging
import requests

# 电子账户开立
def dzzhkl(req):
    data = dzzhkl_molde.dzzhkl_modle(req)
    header = config.header
    url = config.url['jinjian_url']
    req = requests.post(url, headers=header, data=json.dumps(data))
    if req.status_code == 200:
        req_dict = json.loads(req.text)
        if req_dict['header']['status_code'] == 200:
            logging.warning('开立电子账户成功')
            return req.text
        else:
            logging.warning('开立电子账户，请求:{}，返回：{}'.format(url, req.text))
            exit()
    else:
        logging.warning('开立电子账户，请求:{}，返回：{}'.format(url, req.text))
        exit()
