import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        # print('setUp: before every test\n')
        pass

    def tearDown(self):
        # print('tearDown: after every test\n')
        pass

    @classmethod
    def setUpClass(self):
        # print('setUpClass: before all test\n')
        pass

    @classmethod
    def tearDownClass(self):
        # print('tearDownClass: after all test\n')
        pass

    def test_c_run(self):
        self.assertEqual(1, 1)

    def test_d_run(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # test_suite.addTest(MyTest('test_a_run'))
    test_suite.addTest(unittest.makeSuite(MyTest))  # all test
    unittest.TextTestRunner(verbosity=2).run(test_suite)
