import unittest


class MyTestRunner:

    def __init__(self):
        self.suite = unittest.TestSuite()  # 创建测试套件
        all_cases = unittest.defaultTestLoader.discover('.', 'test_*.py')
        # 找到某个目录下所有的以test开头的Python文件里面的测试用例
        for case in all_cases:
            self.suite.addTests(case)  # 把所有的测试用例添加进来

    def run(self):
        unittest.TextTestRunner(verbosity=2).run(self.suite)


if __name__ == "__main__":
    MyTestRunner().run()
