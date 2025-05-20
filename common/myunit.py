import unittest
import logging
import time
from config.config import DOMAINS, ENV, DATA_PATH
from common.common_utils import CommonUtils


class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """类级别初始化：整个测试类执行一次"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        cls.logger = logging.getLogger(__name__)
        cls.logger.info("===== 测试类开始执行 =====")

        # 加载基础配置
        cls.base_url = DOMAINS[ENV]
        cls.file_path = DATA_PATH['test_cases']
        cls.test_cases = CommonUtils.read_test_data(cls.file_path)

        cls.logger.info("已加载测试数据，路径：%s", cls.file_path)

    def setUp(self):
        """每个测试方法执行前运行"""
        self.logger.info("Start testing: %s" % self._testMethodName)
        self.startTime = time.time()

    def tearDown(self):
        """每个测试方法执行后运行"""
        self.logger.info("End testing: %s, 耗时 %.3f 秒", self._testMethodName, time.time() - self.startTime)

    @classmethod
    def tearDownClass(cls):
        """类级别清理：整个测试类结束后运行"""
        cls.logger.info("===== 测试类执行完成 =====")
