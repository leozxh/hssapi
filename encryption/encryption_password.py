'''
密码加密
'''

import hashlib

def get_str_password_md5():
    auth_token ="s8mLTZGhIPF7P9Jwpy"
    passwd = "zxh123456"
    str1 = auth_token + passwd
    hash_md5 = hashlib.md5(str1.encode('utf-8'))
    encrypts2 = str(hash_md5.hexdigest())
    password = encrypts2
    return password