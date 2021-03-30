#登录接口
import unittest
from common.httprequest import http_request
from common.myunit import StartEnd
from encryption.encryption_signature import get_str_sha1_md5_str
from common.gettime import  timeStamp



class TestLogin(StartEnd):
    login = 'https://api-clevguard.ifonelab.net/user/signin'


    #新账号
    def test_001_login_newaccout(self):
        login_url = self.login
        save = open('C:/Users/2021/PycharmProjects/api_test/data/test.txt', 'r')
        random1 = save.read()
        save.close()
        #取第一条用例生成的邮箱
        save1 = open('C:/Users/2021/PycharmProjects/api_test/data/email.txt', 'r')
        a= save1.read()
        existemail = str(a)
        print("使用邮箱%s登录"%existemail)
        save1.close()
        login_data = {'email': existemail,
                      'password':'zxh123456',
                      'device_type': 'web',
                      'randomStr': str(random1),
                      'signature': get_str_sha1_md5_str(),
                      'timeStamp': timeStamp()}
        login_msg = http_request.http_post(login_url, login_data)
        try:
            self.assertEqual('登录成功!', login_msg.json()['msg'])
            print('test_001_login_newaccout 测试通过')
            print(login_msg.json())
        except Exception as e:
            print('test_001_login_newaccout 测试不通过')
            raise e




if __name__ == '__main__':
    unittest.main()