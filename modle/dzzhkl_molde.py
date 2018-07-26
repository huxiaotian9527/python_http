from modle import header_molde


def dzzhkl_modle(data):
    body = {}
    body['user_id'] = data['user_id']
    body['user_name'] = data['user_name']
    body['credential_type'] = data['credential_type']
    body['credential_number'] = data['credential_number']
    body['bank_phone'] = data['bank_phone']
    body['bank_name'] = data['bank_name']
    body['bank_card'] = data['bank_card']
    data = {}
    data['body'] = body
    data['header'] = header_molde.header_modle('10030')
    return data
