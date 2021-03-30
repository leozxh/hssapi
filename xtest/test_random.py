
import random

# randomStr1 = random.randint(0, 100000000)
# open('../data/test.txt', 'w').write(str(randomStr1))
# randomStr = open('../data/test.txt', 'r').read()
# print(randomStr)

a = random.randint(0, 999)
randomemail = str(a)+"zxh@Test.cn"
print("随机生成的邮箱号为:",randomemail)
open('C:/Users/2021/PycharmProjects/api_test/data/email.txt', 'w').write(str(randomemail))

