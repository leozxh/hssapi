import json
from common.httprequest import http_request
from common.myunit import StartEnd
from common.common_utils import CommonUtils
from common.encryption_utils import EncryptionUtils


class TestPersonalSettled(StartEnd):
    def test_001_personal_settle(self):
        """
        商家个人入驻接口测试
        """
        settled_case = self.test_cases[7]
        settled_path = settled_case['Path']
        settled_url = f"{self.base_url}{settled_path}"

        # 从 env.ini 中读取 access_token
        access_token = CommonUtils.read_env_config("accesstoken", section="login")

        # 根据版本号决定是否使用 x_encrypt_key
        version = "1.5.2"  # 当前版本低于 1.5.4，不添加 x_encrypt_key
        x_encrypt_key = EncryptionUtils.get_x_encrypt_key(settled_path)

        # 构造请求头
        headers = http_request.build_auth_headers(
            access_token=access_token,
            x_encrypt_key=x_encrypt_key,  # 版本 < 1.5.4 时不传
            version=version
        )

        # 构造请求体 payload
        payload = {
            "accountInfo": {
                "accountType": "personal",
                "merchantName": "麻光秀",
                "legalName": "麻光秀",
                "identityType": 1,
                "identityNo": "520103195506214022",
                "identityValidityType": 1,
                "identityBeginDate": "20060821",
                "identityEndDate": "",
                "contactPhone": "15207142998",
                "certPhotoFront": "http://111.175.90.254:9000/sohuglobal/2025/05/13/cbc298a942a640928ee9bdfcfca13811_800x800.jpg",
                "certPhotoBack": "http://111.175.90.254:9000/sohuglobal/2025/05/13/8c133a0c0d8f4533a0e7f6b9adb2201c_800x800.jpg"
            },
            "brandInfos": [],
            "categoryInfos": [
                {
                    "cateId": 423,
                    "icon": "http://111.175.90.254:9000/sohuglobal/2025/05/12/3d29a3fbd7a4496daa9a1d3b275b1f3d_400x250.png",
                    "parentId": 419,
                    "qualificationInfos": [
                        {
                            "proveUrl": "http://111.175.90.254:9000/sohuglobal/2025/05/13/1a3958bba0b6405c8aaf8c69cfa7fa35_0x0.jpg",
                            "qualificateId": 6,
                            "qualificateName": "123"
                        },
                        {
                            "proveUrl": "http://111.175.90.254:9000/sohuglobal/2025/05/13/84b76ea8c9b64117b6361a3f7e8e886b_0x0.jpg",
                            "qualificateId": 7,
                            "qualificateName": "321"
                        },
                        {
                            "proveUrl": "http://111.175.90.254:9000/sohuglobal/2025/05/13/afbe4924def24ea48d49baccedd7b987_0x0.jpg",
                            "qualificateId": 8,
                            "qualificateName": "123"
                        },
                        {
                            "proveUrl": "http://111.175.90.254:9000/sohuglobal/2025/05/13/b5d63c36cd894511898dff38e46a1556_0x0.jpg",
                            "qualificateId": 4,
                            "qualificateName": "zlf测试类目资质"
                        }
                    ]
                }
            ],
            "id": None,
            "merchantType": "personal",
            "name": "测试入驻"
        }

        print("====== 请求信息 ======")
        print(f"请求 URL: {settled_url}")
        print(f"请求方法: POST")
        print(f"请求头 Headers: {headers}")
        print("======================")

        # 发送 POST 请求
        response = http_request.http_post(settled_url, headers=headers, json=payload)

        self.assertEqual(200, response.status_code)

        try:
            decoded_text = response.content.decode('utf-8')
        except UnicodeDecodeError:
            decoded_text = response.text

        print("响应内容:", decoded_text)

        # ========== 可选：提取并写入 merchantId 到 env.ini ==========
        # try:
        #     response_json = response.json()
        #     merchant_id = response_json.get('data', {}).get('merchantId')
        #
        #     if merchant_id:
        #         CommonUtils.write_env_config({
        #             'merchantId': str(merchant_id)
        #         }, section='merchant', filename="data/env.ini")
        #         print(f"已将 merchantId 写入配置文件: {merchant_id}")
        #     else:
        #         print("未找到有效的 merchantId")

        # except json.JSONDecodeError:
        #     print("响应内容无法解析为 JSON:", response.text)
