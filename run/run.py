#生成测试报告
from unittestreport import TestRunner
import unittest
import logging
import os
import json
from testcases import hsslogin,smart_business_order,get_account

logger = logging.getLogger(__name__)


def load_email_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, '..', 'data', 'email_config.json')

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        logger.error("Configuration file 'email_config.json' not found.")
        return None
    except json.JSONDecodeError:
        logger.error("Failed to parse 'email_config.json'.")
        return None
def setup_test_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(hsslogin.TestLogin))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(smart_business_order.TestSmartBusinessOrder))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(get_account.TestGetAccountInfo))
    return suite


def create_test_runner(suite):
    return TestRunner(suite,
                      tester='zxh',
                      title="许愿狐接口测试报告",
                      report_dir=r'..\reports',
                      desc="包含登录和智能商单等操作",
                      templates=1)


def run_tests(runner):
    logger.info("开始测试...")
    runner.run()


def send_test_email(runner, email_config):
    if email_config:
        runner.send_email(
            host=email_config["host"],
            port=email_config["port"],
            user=email_config["user"],
            password=email_config["password"],
            to_addrs=email_config["to_addrs"]
        )
    else:
        logger.error("Failed to load email configuration.")


def test_report():
    suite = setup_test_suite()
    runner = create_test_runner(suite)
    run_tests(runner)
    email_config = load_email_config()
    send_test_email(runner, email_config)


if __name__ == '__main__':
    test_report()