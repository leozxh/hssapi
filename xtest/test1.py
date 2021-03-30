'''
拼接规则：
三个字段先拼接
进行sha1加密
转换成string类型
md5加密
转换成string类型
转换成大写
'''
from common.gettime import timeStamp
from encryption.encryption_signature import get_str_sha1_md5_str

"""
    使用sha1、md5加密算法，返回str加密后的字符串
"""

# #获取当前时间转换为字符串
# times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
# timeStamp1 = int(time.mktime(timeArray))
# #timeStamp1 = 1616997017
# #获取随机数
# randomStr = randomno.randint(0, 100000000)
# #randomStr = 57654790
# #内部定义的参数
# secret = "uN3lu01bFtumul8W"
# res = str(timeStamp1)+str(randomStr)+secret
# print(res)
# sha = hashlib.sha1(res.encode('utf-8'))
# encrypts =str(sha.hexdigest())
# print(encrypts)
# hash_md5 = hashlib.md5(encrypts.encode('utf-8'))
# encrypts1 =str(hash_md5.hexdigest())
# print(encrypts1)
# signature =encrypts1.upper()
# print(signature)

# auth_token ="s8mLTZGhIPF7P9Jwpy"
# passwd = "zxh123456"
# str1 = auth_token + passwd
# hash_md5 = hashlib.md5(str1.encode('utf-8'))
# encrypts2 = str(hash_md5.hexdigest())
#password =
# password = get_str_password_md5()
# print(password)
time1 = timeStamp()
signature = get_str_sha1_md5_str()
no1 = open('../data/test.txt', 'r').read()
print(time1)
print(no1)
print(signature)


