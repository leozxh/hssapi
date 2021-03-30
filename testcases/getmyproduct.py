'''
获取我购买的产品
'''

import unittest
from common.httprequest import http_request
from encryption.encryption_signature import get_str_sha1_md5_str
from common.gettime import  timeStamp
from config.gettoken import getToken

class GetMyproduct(unittest.TestCase):
    myproduct = "https://api-clevguard.ifonelab.net/user/user/getMyProduct"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Monimaster-Token': getToken(),
        'Monimaster-Device-Type': 'web'
    }

    def test_001_getmyproduct(self):
        product_url = self.myproduct
        product_headers =self.headers
        save = open('C:/Users/2021/PycharmProjects/api_test/data/test.txt', 'r')
        random1 = save.read()
        save.close()
        product_data = {
                      'randomStr': str(random1),
                      'signature': get_str_sha1_md5_str(),
                      'timeStamp': timeStamp()}
        product_msg = http_request.http_get(product_url,product_data, product_headers)
        try:
            self.assertEqual('success', product_msg.json()['msg'])
            self.assertEqual(7816, product_msg.json()['data'][1]['id'])
            print('test_001_getmyproduct 测试通过')
            print("transaction_id is:%s"%product_msg.json()['data'][1]['id'])
        except Exception as e:
            print('test_001_getmyproduct 测试不通过')
            raise e

if __name__ == '__main__':
    unittest.main()