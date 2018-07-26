from modle import header_molde
import requests
import config, json, logging


# 查询还款计划
def huankuanchxa(num):
    body = {'borrow_no': num}
    data = {}
    data['body'] = body
    data['header'] = header_molde.header_modle('50010')
    url = config.url['jinjian_url']
    header = config.header
    req = requests.post(url, data=json.dumps(data), headers=header)
    if req.status_code == 200:
        req_dict = json.loads(req.text)
        if req_dict['header']['status_code'] == 200:
            logging.warning('查询还款计划成功')
            return req_dict
        else:
            logging.warning('查询还款计划失败，请求:{}，返回：{}'.format(url, req.text))
            exit()
    else:
        logging.warning('查询还款计划失败，请求:{}，返回：{}'.format(url, req.text))
        exit()
