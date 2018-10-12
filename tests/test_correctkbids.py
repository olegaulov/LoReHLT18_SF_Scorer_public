from unittest import TestCase
from pandas.util.testing import assert_frame_equal
import sys
import os

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
sys.path.append(lib_path)

from lib.lorehlt18helper import *


class TestCorrectkbids(TestCase):
    def setUp(self):
        # Create a temporary directory
        self.base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tests")
        self.testfile = os.path.join(self.base_dir, "1_bad_docid.json")
        refstr = """{
          "doc_id":{
            "3":"DOC1",
            "4":"DOC2"
          },
          "frame_id":{
            "3":"Frame1",
            "4":"Frame2"
          },
          "kb_id":{
            "3":"7690208",
            "4":"11186696|384272"
          },
          "user_id":{
            "3":53100,
            "4":53133
          },
          "type":{
            "3":"food",
            "4":"water"
          },
          "urgent":{
            "3":true,
            "4":true
          },
          "unresolved":{
            "3":true,
            "4":true
          },
          "current":{
            "3":true,
            "4":true
          },
          "gravity":{
            "3":true,
            "4":true
          },
          "frame_count":{
            "3":1,
            "4":1
          }
        }"""

        sysstr = """{
          "Confidence":{
            "2040":1.0,
            "513707":1.0,
            "513715":1.0
          },
          "DocumentID":{
            "2040":"DOC1",
            "513707":"DOC2",
            "513715":"DOC2"
          },
          "Justification_ID":{
            "2040":"Segment-13",
            "513707":"Segment-0",
            "513715":"Segment-0"
          },
          "Place_KB_ID":{
            "2040":"7690208",
            "513707":"11399531",
            "513715":"11186696"
          },
          "Resolution":{
            "2040":"insufficient",
            "513707":"insufficient",
            "513715":"insufficient"
          },
          "Status":{
            "2040":"current",
            "513707":"current",
            "513715":"current"
          },
          "Type":{
            "2040":"food",
            "513707":"water",
            "513715":"water"
          },
          "urgent":{
            "2040":true,
            "513707":true,
            "513715":true
          },
          "unresolved":{
            "2040":true,
            "513707":true,
            "513715":true
          },
          "current":{
            "2040":true,
            "513707":true,
            "513715":true
          },
          "gravity":{
            "2040":true,
            "513707":true,
            "513715":true
          },
          "frame_count":{
            "2040":1,
            "513707":1,
            "513715":1
          }
        }"""


        correctsysstr = """{
          "Confidence": {
            "2040": 1.0,
            "513707": 1.0,
            "513715": 1.0
          },
          "DocumentID": {
            "2040": "DOC1",
            "513707": "DOC2",
            "513715": "DOC2"
          },
          "Justification_ID": {
            "2040": "Segment-13",
            "513707": "Segment-0",
            "513715": "Segment-0"
          },
          "Place_KB_ID": {
            "2040": "7690208",
            "513707": "11399531",
            "513715": "11186696|384272"
          },
          "Resolution": {
            "2040": "insufficient",
            "513707": "insufficient",
            "513715": "insufficient"
          },
          "Status": {
            "2040": "current",
            "513707": "current",
            "513715": "current"
          },
          "Type": {
            "2040": "food",
            "513707": "water",
            "513715": "water"
          },
          "current": {
            "2040": true,
            "513707": true,
            "513715": true
          },
          "frame_count": {
            "2040": 1,
            "513707": 1,
            "513715": 1
          },
          "gravity": {
            "2040": true,
            "513707": true,
            "513715": true
          },
          "unresolved": {
            "2040": true,
            "513707": true,
            "513715": true
          },
          "urgent": {
            "2040": true,
            "513707": true,
            "513715": true
          }
        }"""

        self.systemTable = pd.DataFrame.from_dict(json.loads(sysstr))
        self.reference = pd.DataFrame.from_dict(json.loads(refstr))
        self.correctsystemTable = pd.DataFrame.from_dict(json.loads(correctsysstr))


    def test_correctkbids(self):
        assert_frame_equal(correctkbids(self.systemTable, self.reference),self.correctsystemTable)
