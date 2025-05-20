import os
from common.common_utils import CommonUtils

ENV = 'test'  # 可选: test, pre, prod

# 加载 DOMAIN 配置
domain_config = CommonUtils.read_env_config(section='domain')
if domain_config:
    DOMAINS = {
        'test': domain_config.get('test', ''),
        'pre': domain_config.get('pre', ''),
        'prod': domain_config.get('prod', '')
    }
else:
    DOMAINS = {}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录

DATA_PATH = {
    'test_cases': os.path.join(BASE_DIR, 'data', 'testcases.xlsx')
}