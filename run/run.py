#生成测试报告
import time
import HTMLTestRunner
import  unittest
from testcases.register import Testregister
from testcases.login import TestLogin
from testcases.getmyproduct import GetMyproduct




def  test_report():
    suite= unittest.TestSuite()
    test1=unittest.TestLoader().loadTestsFromTestCase(Testregister)
    suite.addTests(test1)
    test2 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTests(test2)
    test3 = unittest.TestLoader().loadTestsFromTestCase(GetMyproduct)
    suite.addTests(test3)


    now=time.strftime('%Y-%m-%d %H_%M_%S') #获取当前时间
    filename='..//report1/'+now+'._report.html'
    fp=open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner\
        (stream=fp, title='接口测试报告', description='测试用例执行情况')
    runner.run(suite)

if __name__ == '__main__':
     test_report()
