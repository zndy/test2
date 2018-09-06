import os
import unittest


class FileExistTest(unittest.TestCase):

    def test_shouldFindFilesWithSameFolder(self):
        self.assertTrue(os.path.exists("./BeanFactoryTest.py"))

    def test_otherFolder(self):
        self.assertTrue(os.path.exists("../logging.yaml"))

    def test_other(self):
        self.assertTrue(os.path.exists("/mycode/logging.yaml"))
