from unittest import TestCase
import sys
import os

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
sys.path.append(lib_path)

from lib.lorehlt18helper import *

class TestBadGetsubmission(TestCase):
    def setUp(self):
        # Create a temporary directory
        self.base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tests")
        self.testfile = os.path.join(self.base_dir, "1_bad_docid.json")

    def test_1_bad_submission(self):
        with self.assertRaises(SystemExit) as cm:
            self.submission = getsubmission(self.testfile, gravity, filelist = "")
        self.assertNotEqual(cm.exception.code, 0)


class TestGoodSubmission(TestCase):
    def setUp(self):
        # Create a temporary directory
        self.base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tests")
        self.testfile = os.path.join(self.base_dir, "1_good.json")

    def test_2_good_submission(self):
        with self.assertRaises(SystemExit) as cm:
            self.submission = getsubmission(self.testfile, gravity, filelist = "")
        self.assertNotEqual(cm.exception.code, 1)
