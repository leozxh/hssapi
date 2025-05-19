#该接口未进行加密处理，请求头无需传加密参数
from common.httprequest import http_request
from common.myunit import StartEnd
from config.config import DOMAINS, ENV, DATA_PATH
from common.common_utils import CommonUtils


class TestGetAccountInfo(StartEnd):
    def test_001_get_account_info(self):
        self._testMethodDoc = '获取当前账号信息'
        base_url = DOMAINS[ENV]  # 获取当前环境域名
        file_path = DATA_PATH['test_cases']  # 获取测试用例路径
        test_cases = CommonUtils.read_test_data(file_path)

        # 假设这个接口是第3条测试用例（索引为2）
        account_case = test_cases[2]
        account_path = account_case['Path']
        account_url = f"{base_url}{account_path}"

        # 从配置中读取 access_token 和 aesKey 用于构造请求头
        access_token = CommonUtils.read_env_config("accesstoken", "login")

        response=None

        try:
            headers = http_request.build_auth_headers(
                access_token=access_token
            )
            response = http_request.http_get(account_url, headers=headers)
            self.assertEqual(200, response.status_code)
            print("响应内容:", response.text)

        except Exception as e:
            print("获取账户信息失败")
            print("响应状态码:", response.status_code)
            print("响应内容:", response.text)
            raise e
