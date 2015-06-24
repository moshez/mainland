import unittest
import sys

from mainland import _main as mymain


class TestGetModule(unittest.TestCase):

    def test_regular(self):
        m = mymain.getModule('mainland')
        self.assertIs(m, sys.modules['mainland'])

    def test_bad(self):
        with self.assertRaises(ImportError):
            mymain.getModule('mainlandGOOOP')

    def test_suffix(self):
        m = mymain.getModule('mainla', suffix=['nd'])
        self.assertIs(m, sys.modules['mainland'])


class TestMain(unittest.TestCase):

    def test_nothing(self):
        mymain.main()
