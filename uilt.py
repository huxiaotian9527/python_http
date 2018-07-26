import random


# 生成九江银行卡号
def cardNum_generator():
    cardNum = '6222'  # 可以更改，银行卡号前四位
    cardname = '九江银行'

    for i in range(11):
        cardNum = cardNum + str(random.randint(0, 9))

    summation = 0
    for i in range(16):
        if i == 0:
            continue

        tmp1 = int(cardNum[15 - i: 16 - i])

        if ((i + 1) % 2 == 0):
            if tmp1 < 5:
                summation = summation + tmp1 * 2
            else:
                tmp2 = str(tmp1 * 2)
                summation = summation + int(tmp2[0]) + int(tmp2[1])
        else:
            summation = summation + tmp1

    check = str(10 - (summation % 10))
    if check == '10':
        check = '0'
    a = cardNum + check

    return a


# 统一社会信用代码中不使用I,O,Z,S,V
SOCIAL_CREDIT_CHECK_CODE_DICT = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22,
    'P': 23, 'Q': 24,
    'R': 25, 'T': 26, 'U': 27, 'W': 28, 'X': 29, 'Y': 30}
# GB11714-1997全国组织机构代码编制规则中代码字符集
ORGANIZATION_CHECK_CODE_DICT = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22,
    'N': 23, 'O': 24, 'P': 25, 'Q': 26,
    'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}


class CreditIdentifier(object):
    def CreateC9(self, code):
        # 第i位置上的加权因子
        weighting_factor = [3, 7, 9, 10, 5, 8, 4, 2]
        # 第9~17位为主体标识码(组织机构代码)
        organization_code = code[8:17]
        # 本体代码
        ontology_code = organization_code[0:8]
        # 生成校验码
        tmp_check_code = self.gen_check_code(
            weighting_factor, ontology_code, 11, ORGANIZATION_CHECK_CODE_DICT)
        return code[:16] + tmp_check_code

    def getSocialCreditCode(self, code):
        code = self.CreateC9(code[:16])
        # 第i位置上的加权因子
        weighting_factor = [1, 3, 9, 27, 19, 26, 16,
                            17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
        # 本体代码
        ontology_code = code[0:17]
        # 计算校验码
        tmp_check_code = self.gen_check_code(
            weighting_factor, ontology_code, 31, SOCIAL_CREDIT_CHECK_CODE_DICT)
        return code[:17] + tmp_check_code

    def gen_check_code(self, weighting_factor, ontology_code, modulus, check_code_dict):
        total = 0
        for i in range(len(ontology_code)):
            if ontology_code[i].isdigit():
                total += int(ontology_code[i]) * weighting_factor[i]
            else:
                total += check_code_dict[ontology_code[i]
                         ] * weighting_factor[i]
        C9 = modulus - total % modulus
        C9 = 0 if C9 == 31 else C9
        C9 = list(check_code_dict.keys())[
            list(check_code_dict.values()).index(C9)]
        return C9


def daima():
    codeHelper = CreditIdentifier()
    a = str(random.randint(1000000000000000, 9999999999999999))
    return codeHelper.getSocialCreditCode(a)


a = cardNum_generator()


# 车架号生成
def cjh():
    # 车架号（没有“I”、“O”、“Q”）
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
         'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # 对应实际值
    b = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7,
         'Q': 8, 'R': 9, 'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9}
    # 加权
    c = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 10, '10': 9, '11': 8, '12': 7, '13': 6, '14': 5,
         '15': 4, '16': 3, '17': 2}
    vin = 'VNN'
    nn = 0
    for i in range(14):
        vin = vin + random.choice(a)
    for i in range(1, 18):
        da = vin[i - 1]
        if i == 9:
            continue
        else:
            a = c[str(i)]  # 加权
            try:
                dd = int(da)
            except:
                dd = b[da]
            nn = nn + a * dd
    if 0 <= nn % 11 <= 9:
        vvn = vin[:8] + str(nn % 11) + vin[9:17]
    else:
        vvn = vin[:8] + 'X' + vin[9:17]

    return vvn
