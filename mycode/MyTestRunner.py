import unittest


class MyTestRunner:

    def __init__(self):
        self.suite = unittest.TestSuite()
        all_cases = unittest.defaultTestLoader.discover('.', 'test_*.py')
        for case in all_cases:
            self.suite.addTests(case)

    def run(self):
        unittest.TextTestRunner(verbosity=2).run(self.suite)


if __name__ == "__main__":
    MyTestRunner().run()
