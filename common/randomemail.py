
'''
生成随机邮箱
'''

import random
import string

def eamil():

    a = random.randint(0, 999)
    b = random.choice(string.ascii_letters)
    randomemail = str(a)+str(b)+"zxh@Test.cn"
    print("随机生成的邮箱号为:",randomemail)
    with open("C:/Users/2021/PycharmProjects/api_test/data/email.txt", "wt") as out_file:
        out_file.write(randomemail)
    # open('C:/Users/2021/PycharmProjects/api_test/data/email.txt', 'w').write(str(randomemail))
    # open('C:/Users/2021/PycharmProjects/api_test/data/email.txt', 'w').close()
    return randomemail