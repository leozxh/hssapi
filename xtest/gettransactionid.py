'''
获取transactionid
'''


from common.httprequest import http_request
from encryption.encryption_signature import get_str_sha1_md5_str
from common.gettime import  timeStamp
from config.gettoken import getToken


def gettransavtionid():
    myproduct = "https://api-clevguard.ifonelab.net/user/user/getMyProduct"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Monimaster-Token': getToken(),
        'Monimaster-Device-Type': 'web'
    }
    product_url = myproduct
    product_headers =headers
    save = open('/data/test.txt', 'r')
    random1 = save.read()
    save.close()
    product_data = {
                  'randomStr': str(random1),
                  'signature': get_str_sha1_md5_str(),
                  'timeStamp': timeStamp()}
    product_msg = http_request.http_get(product_url,product_data, product_headers)
    transactionid = product_msg.json()['data'][1]['id']
    print(transactionid)
    return transactionid