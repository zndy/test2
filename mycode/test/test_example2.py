import unittest


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def setUp(self):
        print('setUp: before every test\n')

    def tearDown(self):
        print('tearDown: after every test\n')

    @classmethod
    def setUpClass(self):
        print('setUpClass: before all test\n')

    @classmethod
    def tearDownClass(self):
        print('tearDownClass: after all test\n')

    def test_c_run(self):
        self.assertEqual(1, 1)

    def test_d_run(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # test_suite.addTest(MyTest('test_a_run'))
    test_suite.addTest(unittest.makeSuite(MyTest))  # all test
    unittest.TextTestRunner(verbosity=2).run(test_suite)