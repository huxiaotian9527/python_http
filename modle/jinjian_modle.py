from faker import Faker
import time
from modle import header_molde
import random as random


def jinjian_module():
    f = Faker(locale='zh_CN')
    certNo = f.ssn()
    body = {
        "production_code": 'QD01',  # 产品代码
        "user_id": str(random.randint(1000, 9999)),
        "user_name": '赵力唯',
        "credential_type": "0",
        "credential_number": '330100199005301578',
        "credential_expire_date": "20280511",
        "gender": str(random.randint(0, 2)),
        "age": str(random.randint(20, 60)),
        "credit_score": str(random.randint(600, 800)),
        "bank_phone": '18100000006',
        "bank_name": "中国九江银行",
        "bank_card": '6212562159000000009',
        "education": str(random.choice([10, 20, 30, 60, 70])),
        "marital_status": "20",
        "spouse_name": f.name(),
        "spouse_credential_type": "0",
        "spouse_credential_number": certNo,
        "spouse_company_name": f.company(),
        "income": str(random.randint(100000, 300000)),
        "company_name": f.company(),
        "contact_relationship": str(random.randint(1, 10)),
        "contact_name": f.name(),
        "contact_phone": f.phone_number(),
        "degree": str(random.randint(1, 5)),
        "position": str(random.randint(1, 4)),
        "tech_name": str(random.randint(0, 3)),
        "occupation": random.choice(['0', '1', '3', '4', '5', '6', 'X', 'Y', 'Z']),
        "live_status": str(random.randint(1, 7)),
        "residential_address": f.address(),
        "credential_area": f.province(),
        "pass_facial_recognition": "1",
        "drive_license_number": certNo,
        "create_time": str(time.strftime("%Y%m%d%H%M%S", time.localtime())),
        "attachment": "/cls/xinzhen"
    }

    data = dict()
    data['body'] = body
    data['header'] = header_molde.header_modle('10010')

    return data


if __name__ == '__main__':
    a = jinjian_module()
    print(a)
