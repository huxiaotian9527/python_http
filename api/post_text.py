import requests
import config


def post_pdf(da):
    img = config.text[da]
    url = config.url + ''
    file = {'file': open(img, 'rb')}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/59.0',
        'Host': 'cj-file-cjtest.xinzhentech.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://cj-manage-cjtest.xinzhentech.com /',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
    }
    res = requests.post(url, files=file, headers=header)
    print(res.text)


if __name__ == '__main__':
    post_pdf(1)
