from modle import header_molde
import uilt
import arrow
from modle import jinjian_modle


def jksq_modle():
    dat = jinjian_modle.body
    body = {
        'contract_number': arrow.now().format('YYYYMMDDHHmmss'),
        'contract_start_date': '20180622',
        'contract_end_date': '20210625',
        'effective_time': arrow.now().format('YYYYMMDDHHmmss'),
        'insurance_code': '',
        'insurance_number': '',
        'user_id': dat['user_id'],
        'customer_name': dat['user_name'],
        'credential_type': dat['credential_type'],
        'credential_number': dat['credential_number'],
        'loan_money': '100000',
        'customer_apr': '10.00',
        'car_calculation_price': '130000',
        'car_guidance_price': '125000',
        'down_payment_per': '20.00',
        'down_payment_price': '25000',
        'car_type': '1',
        'car_model': '大众',
        'car_color': '红色',
        'registration_city': '深圳',
        'car_apply_type': '1',
        'carriage_number': uilt.cjh(),
        'attachment': '/cls/xinzhen'
    }
    data = dict()
    data['body'] = body
    data['header'] = header_molde.header_modle('40010')
    data['header']['txn_no'] = '2018072376076869472'
    return data


if __name__ == '__main__':
    jksq_modle()
