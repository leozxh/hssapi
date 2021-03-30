'''
生成随机数存到本地
'''
import random


def random1():
    randomStr = random.randint(0, 100000000)
    with open("C:/Users/2021/PycharmProjects/api_test/data/test.txt", "wt") as out_file:
        out_file.write(str(randomStr))
    # open('../data/test.txt', 'w').write(str(randomStr))
    # open('../data/test.txt', 'w').close()
    return randomStr
