# header

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/59.0',
    'Accept': 'application/json',
    'content-type': 'application/json',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}

url = 'http://10.116.3.163:8080'
# 登录信息
login_data = {
    'admin': {'username': 'system', 'password': '123456', 'roleId': '1'}
}

# 代理
proxy = {'http': 'http:/127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}

text = ['D:\python\九江\身份证正反面.pdf', 'D:\python\九江\驾照照片.jpg', 'D:\python\九江\大头照.jpg']
