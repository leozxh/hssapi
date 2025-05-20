# run/runner.py

import unittest
from unittestreport import TestRunner
from testcases import hsslogin, smart_business_order, get_account
from config.config import REPORT_CONFIG, EMAIL_CONFIG_PATH
import json
import logging
import os

logger = logging.getLogger(__name__)

def load_email_config():
    try:
        with open(EMAIL_CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error("加载 email_config.json 失败: %s", e)
        return None


def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(hsslogin.TestLogin))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(smart_business_order.TestSmartBusinessOrder))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(get_account.TestGetAccountInfo))
    return suite


def create_runner(suite):
    return TestRunner(
        suite,
        tester=REPORT_CONFIG["tester"],
        title=REPORT_CONFIG["title"],
        report_dir=REPORT_CONFIG["report_dir"],
        desc=REPORT_CONFIG["desc"],
        templates=REPORT_CONFIG["template"]
    )


def run_tests(runner):
    logger.info("开始执行测试...")
    runner.run()


def send_report_email(runner, email_config=None):
    if not email_config:
        logger.warning("未提供邮箱配置，跳过发送邮件")
        return

    runner.send_email(
        host=email_config["host"],
        port=email_config["port"],
        user=email_config["user"],
        password=email_config["password"],
        to_addrs=email_config["to_addrs"]
    )
    logger.info("测试报告已发送")


def run_all():
    suite = create_test_suite()
    runner = create_runner(suite)
    run_tests(runner)
    email_config = load_email_config()
    send_report_email(runner, email_config)
