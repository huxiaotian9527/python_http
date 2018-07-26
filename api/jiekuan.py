from modle import jksq_modle
import config
import logging
import requests
import json


def jksq(data):
    header = config.header
    url = config.url + '/api/qudian/loan/apply'
    try:
        req = requests.post(url, headers=header, data=json.dumps(data))
        logging.info('借款请求数据：{}, URL：{}, 返回数据{}'.format(data, url, req.text))
    except Exception as e:
        logging.warning('借款失败,{}'.format(e))
    finally:
        logging.warning('借款结束{}'.format('-' * 100))


if __name__ == '__main__':
    jk_data = jksq_modle.jksq_modle()
    jksq(jk_data)
