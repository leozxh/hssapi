
import unittest
from common.httprequest import http_request
from common.myunit import StartEnd
from encryption.encryption_signature import get_str_sha1_md5_str
from common.gettime import  timeStamp
from config.gettoken import getToken
from xtest.gettransactionid import gettransavtionid



class TestgetTransaction(StartEnd):
    trans = 'https://api-clevguard.ifonelab.net/user/getTransaction'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Monimaster-Token': getToken(),
        'Monimaster-Device-Type': 'web'
    }

    def test_001_gettrans(self):
        trans_url = self.trans
        trans_headers =self.headers
        save = open('/data/test.txt', 'r')
        random1 = save.read()
        save.close()
        # save1 = open('C:/Users/2021/PycharmProjects/api_test/data/transaction.txt', 'r')
        # trans1 = save1.read()
        # save1.close()
        trans_data = {
                      'transaction_id':gettransavtionid(),
                      'randomStr': str(random1),
                      'signature': get_str_sha1_md5_str(),
                      'timeStamp': timeStamp()}
        trans_msg = http_request.http_post(trans_url, trans_data,trans_headers)

        try:
            self.assertEqual('success', trans_msg.json()['msg'])
            print('test_001_gettrans 测试通过')
            print(trans_msg.json())
        except Exception as e:
            print('test_001_gettrans 测试不通过')
            raise e




if __name__ == '__main__':
    unittest.main()
