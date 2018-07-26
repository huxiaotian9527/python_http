from modle import jinjian_modle
import config
import json
import logging
import requests
import logging_config


# 进件
def jin_jan(data):
    logging_config.log_evel()
    logging.warning('进件开始{}'.format('-' * 10))
    header = config.header
    url = config.url + '/api/qudian/businessApplyAudit'
    try:
        req = requests.post(url, headers=header, data=json.dumps(data))
        logging.info('进件请求数据：{}, URL：{}, 返回数据{}'.format(data, url, req.text))
    except Exception as e:
        logging.warning('进件失败,{}'.format(e))
    finally:
        logging.warning('进件结束{}'.format('-' * 10))


if __name__ == '__main__':
    jj_data = jinjian_modle.jinjian_module()
    jin_jan(jj_data)
