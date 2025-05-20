from common.httprequest import http_request  # 导入 http_request 模块，用于发送 HTTP 请求
from common.myunit import StartEnd  # 导入 StartEnd 类，作为测试基类
from config.config import DOMAINS, ENV, DATA_PATH  # 导入配置模块，包含环境变量和路径
from common.common_utils import CommonUtils  # 导入 CommonUtils 类，提供通用工具方法

class TestLogin(StartEnd):
    def test_001_login_newaccount(self):
        self._testMethodDoc = '登录操作'
        base_url = DOMAINS[ENV]
        file_path = DATA_PATH['test_cases']
        test_cases = CommonUtils.read_test_data(file_path)

        # 直接获取第一条用例（索引为 0）
        case = test_cases[0]

        login_path = case['Path']  # 获取登录接口路径
        login_url = f"{base_url}{login_path}"  # 拼接完整的登录 URL

        login_data = {  # 构造登录请求的数据
            'userName': case['userName'],  # 用户名
            'password': case['password'],  # 密码
            'loginType': case['loginType'],  # 登录类型
        }

        login_msg = http_request.http_post(login_url, json=login_data)  # 发送 POST 请求并获取响应

        # 打印请求信息（可选）
        print("====== 请求信息 ======")
        print(f"请求 URL: {login_url}")
        print(f"请求方法: POST")
        print("======================")


        try:
            self.assertEqual(case['ExpectedResult'], login_msg.json()['msg'])  # 断言实际响应与预期结果是否一致
            print(f"{case['CaseID']} 测试通过")  # 如果测试通过，打印成功信息

            response_data = login_msg.json().get('data', {})  # 获取响应中的 data 部分
            filtered_data = {  # 过滤需要的数据
                'userid': response_data.get('userId'),  # 用户 ID
                'accesstoken': response_data.get('accessToken'),  # 访问令牌
                'roles': response_data.get('roles')  # 角色信息
            }
            CommonUtils.write_env_config(filtered_data, filename="data/env.ini")  # 将过滤后的数据写入环境变量文件

        except Exception as e:  # 捕获异常
            print(f"{case['CaseID']} 测试不通过")  # 打印测试失败信息
            print("响应状态码:", login_msg.status_code)  # 打印响应状态码
            print("响应内容:", login_msg.text)  # 打印响应内容
            raise e  # 抛出异常