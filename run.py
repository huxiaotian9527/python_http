from api import jinjian, jiekuan
from modle import jinjian_modle, jksq_modle


def run():
    # 进件
    jj_data = jinjian_modle.jinjian_modle()
    jinjian.jin_jan(jj_data)
    # 借款
    jk_data = jksq_modle.jksq_modle()
    jk_data['header']['txn_no'] = jj_data['header']['txn_no']
    jiekuan.jksq(jk_data)


if __name__ == '__main__':
    run()
