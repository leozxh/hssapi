from common.httprequest import http_request  # 导入 http_request 模块，用于发送 HTTP 请求
from common.myunit import StartEnd  # 导入 StartEnd 类，作为测试基类
from config.config import DOMAINS, ENV,DATA_PATH  # 导入配置模块，包含环境变量和路径
from common.common_utils import CommonUtils

class TestGetAESKey(StartEnd):  # 定义测试类，继承自 StartEnd
    def test_get_aes_key(self):  # 定义测试方法，用于获取 AES 密钥
        base_url = DOMAINS[ENV]  # 根据当前环境获取域名
        file_path = DATA_PATH['test_cases']  # 定义获取 AES 密钥的接口路径
        test_cases = CommonUtils.read_test_data(file_path)
        aes_case = test_cases[1]
        aeskey_path = aes_case['Path']
        aes_key_url = f"{base_url}{aeskey_path}"

        try:
            response = http_request.http_get(aes_key_url)  # 发送 GET 请求获取 AES 密钥
            print("====== AES Key 接口响应 ======")  # 添加打印标识
            print("响应状态码:", response.status_code)
            print("响应内容:", response.text)  # 打印原始响应内容
            print("==============================")
            self.assertEqual(200, response.status_code)  # 断言响应状态码为 200
            # 获取响应中的 data 数据
            response_data = response.json().get('data', {})
            # 将 data 写入配置文件，section 设置为 'aes'
            CommonUtils.write_env_config(response_data, section='aes', filename="data/env.ini")
        except Exception as e:  # 捕获异常
            print("获取 AES 密钥失败")  # 打印失败信息
            print("响应状态码:", response.status_code)  # 打印响应状态码
            print("响应内容:", response.text)  # 打印响应内容
            raise e  # 抛出异常