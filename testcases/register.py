'''
注册接口
'''
import unittest
from common.httprequest import http_request
from encryption.encryption_signature import get_str_sha1_md5_str
from encryption.encryption_password import get_str_password_md5
from common.gettime import  timeStamp
from common.myunit import StartEnd
from common.randomemail import eamil
from common.randomno import random1


class Testregister(StartEnd):
    register = 'https://api-clevguard.ifonelab.net/user/register'
    random1()
    # 随机邮箱注册
    def test_001_randomEmail(self):
        register_url = self.register
        save = open('C:/Users/2021/PycharmProjects/api_test/data/test.txt', 'r')
        random1 = save.read()
        save.close()
        register_data = {'email': eamil(),
                         'password': get_str_password_md5(),
                         'confirm_password': get_str_password_md5(),
                         'is_agreement': '1',
                         'device_type': 'web',
                         'timeStamp': timeStamp(),
                         'randomStr': str(random1),
                         'signature': get_str_sha1_md5_str()}
        login_msg = http_request.http_post(register_url, register_data)
        try:
            self.assertEqual('注册并激活成功!', login_msg.json()['msg'])
            print('test_001_randomEmail 测试通过')
        except Exception as e:
            print('test_001_randomEmail 测试不通过')
            raise e

    # 已存在的邮箱
    def test_002_existedEmail(self):
        register_url = self.register
        save = open('C:/Users/2021/PycharmProjects/api_test/data/test.txt', 'r')
        random1 = save.read()
        save.close()
        #取第一条用例生成的邮箱
        save1 = open('C:/Users/2021/PycharmProjects/api_test/data/email.txt', 'r')
        a= save1.read()
        existemail = str(a)
        save1.close()
        register_data = {'email':existemail,
                        'password': get_str_password_md5(),
                        'confirm_password': get_str_password_md5(),
                        'is_agreement': '1',
                        'device_type': 'web',
                        'timeStamp': timeStamp(),
                        'randomStr':str(random1),
                        'signature':get_str_sha1_md5_str()}
        login_msg = http_request.http_post(register_url, register_data)
        try:
            self.assertEqual('邮箱已存在!', login_msg.json()['msg'])
            print('test_002_existedEmail 测试通过')
        except Exception as e:
            print('test_002_existedEmail 测试不通过')
            raise e


if __name__ == '__main__':
    unittest.main()