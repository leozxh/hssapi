'''
登录生成token
'''
from common.httprequest import http_request
from encryption.encryption_signature import get_str_sha1_md5_str
from common.gettime import  timeStamp



def getToken():  # 获取token函数
    url = "https://api-clevguard.ifonelab.net/user/signin"
    save = open('C:/Users/2021/PycharmProjects/api_test/data/test.txt', 'r')
    random1 = save.read()
    save.close()
    login_data = {'email': 'liaoxf@imyfone.cn',#该账号存在订单，方便后续查询
                      'password': '123456a',
                      'device_type': 'web',
                      'randomStr': str(random1),
                      'signature': get_str_sha1_md5_str(),
                      'timeStamp': timeStamp()}
    r = http_request.http_post(url, login_data)  # 发送post请求
    token = r.json()["data"]["token"]
    with open("C:/Users/2021/PycharmProjects/api_test/data/token.txt", "wt") as out_file:
        out_file.write(str(token))
    return (r.json()["data"]["token"])  # 将获取的token返回