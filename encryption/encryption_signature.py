'''
拼接规则：
三个字段先拼接
进行sha1加密
转换成string类型
md5加密
转换成string类型
转换成大写
'''
import hashlib
import time
from datetime import datetime


def get_str_sha1_md5_str():
    #获取当前时间转换为字符串
    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
    timeStamp1 = int(time.mktime(timeArray))
    #获取随机数
    save = open('C:/Users/2021/PycharmProjects/api_test/data/test.txt', 'r')
    randomStr = save.read()
    save.close()
    #内部定义的参数
    secret = "uN3lu01bFtumul8W"
    res = str(timeStamp1) + str(randomStr) + secret
    sha = hashlib.sha1(res.encode('utf-8'))
    encrypts = str(sha.hexdigest())
    hash_md5 = hashlib.md5(encrypts.encode('utf-8'))
    encrypts1 = str(hash_md5.hexdigest())
    signature = encrypts1.upper()
    return signature



