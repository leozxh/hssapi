import json
from common.httprequest import http_request
from common.myunit import StartEnd
from common.common_utils import CommonUtils
from common.encryption_utils import EncryptionUtils


class TestSmartBusinessOrder(StartEnd):
    def test_001_get_dialog_history(self):
        self._testMethodDoc = '智能商单-获取历史商单'
        # base_url = DOMAINS[ENV]  # 获取当前环境域名
        # file_path = DATA_PATH['test_cases']  # 获取测试用例路径
        # test_cases = CommonUtils.read_test_data(file_path)

        # 假设这个接口是第4条测试用例（索引为3）
        dialog_case = self.test_cases[3]
        dialog_path = dialog_case['Path']
        dialog_url = f"{self.base_url}{dialog_path}"

        # 从配置中读取 access_token
        access_token = CommonUtils.read_env_config("accesstoken", section="login")
        x_encrypt_key = EncryptionUtils.get_x_encrypt_key(dialog_path)

        try:
            version = "1.5.4"
            # 构造请求头：该接口使用 x-encrypt-key
            headers = http_request.build_auth_headers(
                access_token=access_token,
                x_encrypt_key=x_encrypt_key,  # ✅ 使用 x_encrypt_key 参数
                version = version
            )

            #打印请求信息
            print("====== 请求信息 ======")
            print(f"请求 URL: {dialog_url}")
            print(f"请求方法: GET")
            print(f"请求头 Headers: {headers}")
            print("======================")

            # 发送 GET 请求
            response = http_request.http_get(dialog_url, headers=headers)
            self.assertEqual(200, response.status_code)

            # 打印响应内容
            print("响应内容:", response.text)

        except Exception as e:
            print("获取对话历史失败")
            print("响应状态码:", response.status_code)
            print("响应内容:", response.text)
            raise e

    def test_002_custom_dialog_task(self):
        self._testMethodDoc = '智能商单-生成对话'
        # 假设该接口是第5条测试用例（索引为4）
        task_case = self.test_cases[4]
        task_path = task_case['Path']
        task_url = f"{self.base_url}{task_path}"

        # 从配置中读取 access_token
        access_token = CommonUtils.read_env_config("accesstoken", section="login")
        x_encrypt_key = EncryptionUtils.get_x_encrypt_key(task_path)

        response = None  # 提前声明并初始化为 None

        try:
            version = "1.5.4"
            # 构造请求头：该接口使用 x-encrypt-key
            headers = http_request.build_auth_headers(
                access_token=access_token,
                x_encrypt_key=x_encrypt_key,
                version=version
            )

            # 添加 message 参数
            params = {
                'message': CommonUtils.generate_realistic_industry_requirement()
            }

            # 打印请求信息（可选）
            print("====== 请求信息 ======")
            print(f"请求 URL: {task_url}")
            print(f"请求方法: GET")
            print(f"请求头 Headers: {headers}")
            print("======================")

            # 发送 GET 请求
            response = http_request.http_get(task_url, headers=headers,params=params)
            self.assertEqual(200, response.status_code)
            try:
                decoded_text = response.content.decode('utf-8')
            except UnicodeDecodeError:
                decoded_text = response.text  # 自动解码失败时回退
            #print("响应内容:", decoded_text)

            # ========== 新增：解析第一行有效的 data: JSON 并写入 env.ini ==========
            dialog_record_id = None
            dialog_id = None

            for line in response.text.strip().split('\n'):
                if line.startswith('data:'):
                    json_str = line[len('data:'):].strip()
                    try:
                        data = json.loads(json_str)
                        dialog_record_id = data.get('dialogRecordId')
                        dialog_id = data.get('dialogId')

                        if dialog_record_id and dialog_id:
                            break  # 提取成功，退出循环
                    except json.JSONDecodeError:
                        continue  # 跳过无法解析的行

            # 写入配置文件
            if dialog_record_id and dialog_id:
                CommonUtils.write_env_config({
                    'dialogRecordId': dialog_record_id,
                    'dialogId': dialog_id
                }, section='dialog', filename="data/env.ini")
            else:
                print("未找到有效的 dialogRecordId 或 dialogId")

        except Exception as e:
            print("获取自定义对话任务失败")
            print("响应状态码:", response.status_code)
            print("响应内容:", response.text)
            raise e

    def test_003_get_analysis_result(self):
        self._testMethodDoc = '智能商单-点击下一步'
        # 假设该接口是第6条测试用例（索引为5）
        analysis_case = self.test_cases[5]
        analysis_path = analysis_case['Path']
        analysis_url = f"{self.base_url}{analysis_path}"

        # 从 env.ini 中读取 dialogRecordId（由 test_002_custom_dialog_task 写入）
        dialog_record_id = CommonUtils.read_env_config("dialogRecordId", section="dialog")
        if not dialog_record_id:
            raise ValueError("缺少必要的 dialogRecordId，请先运行 test_002_custom_dialog_task")

        # 构造请求路径
        analysis_url_with_id = f"{analysis_url}/{dialog_record_id}"

        # 从配置中读取 access_token
        access_token = CommonUtils.read_env_config("accesstoken", section="login")
        x_encrypt_key = EncryptionUtils.get_x_encrypt_key(analysis_path)

        response = None
        try:
            version = "1.5.4"
            # 构造请求头：该接口使用 x-encrypt-key
            headers = http_request.build_auth_headers(
                access_token=access_token,
                x_encrypt_key=x_encrypt_key,
                version=version
            )

            print("====== 请求信息 ======")
            print(f"请求 URL: {analysis_url_with_id}")
            print(f"请求方法: GET")
            print(f"请求头 Headers: {headers}")
            print("======================")

            # 发送 GET 请求（无 params，直接发送）
            response = http_request.http_get(analysis_url_with_id, headers=headers)

            self.assertEqual(200, response.status_code)

            # 打印响应内容并处理乱码问题
            try:
                decoded_text = response.content.decode('utf-8')
            except UnicodeDecodeError:
                decoded_text = response.text

            print("响应内容:", decoded_text)

            # ========== 新增：解析响应内容并写入 env.ini ==========
            try:
                response_json = response.json()
                data = response_json.get('data', {}).get('busyTaskVo', {})

                # 提取字段
                industry_type = data.get('industryType')
                industry_name = data.get('industryName')
                title = data.get('title')
                potential_demand = data.get('potentialDemand', [])
                content = data.get('content')

                # 处理 content 字段：转义换行和双引号
                escaped_content = content.replace('\n', '\\n').replace('"', '\\"') if content else ""

                # 转义潜在需求中的 % 防止 configparser 报错
                escaped_potential_demand = [item.replace("%", "%%") for item in potential_demand]

                # 写入 env.ini
                CommonUtils.write_env_config({
                    'industryType': str(industry_type),
                    'industryName': industry_name,
                    'title': title,
                    'potentialDemand': json.dumps(escaped_potential_demand, ensure_ascii=False),
                    'content': escaped_content
                }, section='analysis', filename="data/env.ini")

                print("已成功写入 env.ini")
                print('生成的商单标题为：'+ title)

            except Exception as parse_error:
                print("解析响应内容失败:", str(parse_error))

        except Exception as e:
            print("获取对话分析失败")
            print("响应状态码:", response.status_code if response else "未知")
            print("响应内容:", response.text if response else "无响应数据")
            raise e

    def test_004_submit_task(self):
        self._testMethodDoc = '智能商单-生成商单'
        # 假设这是第7条测试用例（索引为6）
        submit_case = self.test_cases[6]
        submit_path = submit_case['Path']
        submit_url = f"{self.base_url}{submit_path}"

        # 从 env.ini 中读取 dialogId
        dialog_id = CommonUtils.read_env_config("dialogId", section="dialog")
        if not dialog_id:
            raise ValueError("缺少必要的 dialogId，请先运行 test_002_custom_dialog_task")

        # 从 env.ini 中读取之前保存的 analysis 数据
        industry_type = CommonUtils.read_env_config("industryType", section="analysis")
        industry_name = CommonUtils.read_env_config("industryName", section="analysis")
        title = CommonUtils.read_env_config("title", section="analysis")
        potential_demand_str = CommonUtils.read_env_config("potentialDemand", section="analysis")
        content = CommonUtils.read_env_config("content", section="analysis")

        try:
            # 解析 potentialDemand 字符串为列表
            potential_demand = json.loads(potential_demand_str)
        except json.JSONDecodeError:
            raise ValueError("potentialDemand 数据格式错误，无法解析为 JSON 数组")

        # 构造请求 body（Payload）
        payload = {
            "imageUrl": "",
            "siteVoNames": [],
            "labelList": [],
            "deliveryDay":CommonUtils.generate_random_delivery_day(),
            "location": "",
            "fullAmount": CommonUtils.generate_random_number(),
            "type": 1294,
            "potentialDemand": potential_demand,
            "addSiteIds": [],
            "ios_identifier": "9F494372-1A76-4712-BB9B-703501126066",
            "receiveLimit": False,
            "address": "",
            "deliveryList": [],
            "isSaveDraft": False,
            "typeName": "通用",
            "deliveryStep": False,
            "isApproveReceive": False,
            "industryType": industry_type,
            "kickbackValue": "",
            "totalPrice": CommonUtils.generate_random_number(),
            "fullCurrency": 0,
            "sys_model": "iPhone",
            "industryName": industry_name,
            "isReceiveDeposit": False,
            "kickbackType": "none",
            "dialogId": int(dialog_id),
            "videoUrl": "",
            "needSplit": False,
            "isDraft": False,
            "settleType": -1,
            "ios_version": "1.5.4",
            "sys_name": "iOS",
            "name": "",
            "content": content.replace("\\n", "\n"),  # 还原换行符
            "sys_version": "18.0.1",
            "deliveryMsg": "",
            "title":title+'zxh'
        }

        # 从当前接口路径生成 x_encrypt_key
        access_token = CommonUtils.read_env_config("accesstoken", section="login")
        x_encrypt_key = EncryptionUtils.get_x_encrypt_key(submit_path)

        version = "1.5.4"
        # 构造请求头：该接口使用 x-encrypt-key
        headers = http_request.build_auth_headers(
            access_token=access_token,
            x_encrypt_key=x_encrypt_key,
            version=version
        )

        print("====== 请求信息 ======")
        print(f"请求 URL: {submit_url}")
        print(f"请求方法: POST")
        print(f"请求头 Headers: {headers}")
        print("======================")

        # 发送 POST 请求
        response = http_request.http_post(submit_url, headers=headers, json=payload)

        self.assertEqual(200, response.status_code)

        try:
            decoded_text = response.content.decode('utf-8')
        except UnicodeDecodeError:
            decoded_text = response.text

        print("响应内容:", decoded_text)

        # ========== 新增：提取并写入 busyTaskId 到 env.ini ==========
        try:
            response_json = response.json()
            raw_data = response_json.get('data')

            if isinstance(raw_data, int):
                busy_task_id = raw_data
            elif isinstance(raw_data, dict):
                busy_task_id = raw_data.get('busyTaskId')
            else:
                busy_task_id = None

            if busy_task_id:
                CommonUtils.write_env_config({
                    'busyTaskId': str(busy_task_id)
                }, section='task', filename="data/env.ini")
                #print(f"已将 busyTaskId 写入配置文件: {busy_task_id}")
            else:
                print("未找到有效的 busyTaskId")

        except json.JSONDecodeError:
            print("响应内容无法解析为 JSON:", response.text)
        except Exception as parse_error:
            print("解析响应失败或无 busyTaskId:", str(parse_error))

