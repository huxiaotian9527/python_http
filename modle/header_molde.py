import time
import random
import arrow


def header_modle(service_code):
    header = {
        "host_ip": '10.10.1.24',
        "txn_no": arrow.now().format('YYYYMMDD') + str(random.randint(10000000003, 99999999999)),
        "txn_time": str(time.strftime("%Y%m%d%H%M%S", time.localtime())),
        "service_code": service_code,
        "client_id": "CLS100000001",  # 合作方ID
        "host_name": "demo-server"
    }
    return header


if __name__ == '__main__':
    a = header_modle('1000')
    print(a)
