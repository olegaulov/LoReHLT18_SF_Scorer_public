from unittest import TestCase
import numpy.testing as npt
import sys
import os

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
sys.path.append(lib_path)

from lib.lorehlt18helper import *

class TestPrecisionN(TestCase):
    def setUp(self):
        myrefstr = '''{ "kb_id": {
                "0": "1",
                "3": "5",
                "1": "2",
                "4": "9",
                "2": "4"
              },
              "type": {
                "0": "food",
                "3": "water",
                "1": "evac",
                "4": "water",
                "2": "shelter"
              },
              "urgent": {
                "0": 3.0,
                "3": 3.0,
                "1": 2.0,
                "4": 2.0,
                "2": 1.0
              },
              "unresolved": {
                "0": 3.0,
                "3": 3.0,
                "1": 2.0,
                "4": 2.0,
                "2": 1.0
              },
              "current": {
                "0": 3.0,
                "3": 3.0,
                "1": 2.0,
                "4": 2.0,
                "2": 1.0
              },
              "gravity": {
                "0": 3.0,
                "3": 3.0,
                "1": 2.0,
                "4": 2.0,
                "2": 1.0
              },
              "frame_count": {
                "0": 3,
                "3": 3,
                "1": 2,
                "4": 2,
                "2": 1
              },
              "gain": {
                "0": 10,
                "3": 10,
                "1": 5,
                "4": 5,
                "2": 1
              }
            }'''
        mysysstr1 = '''{
                  "Confidence": {
                    "0": 1,
                    "1": 1,
                    "2": 1,
                    "3": 1,
                    "4": 1,
                    "5": 1,
                    "6": 1,
                    "7": 1,
                    "8": 1,
                    "9": 1
                  },
                  "DocumentID": {
                    "0": "File_3",
                    "1": "File_4",
                    "2": "File_5",
                    "3": "BadFile_1",
                    "4": "BadFile_2",
                    "5": "File_6",
                    "6": "File_7",
                    "7": "File_1",
                    "8": "File_2",
                    "9": "File_8"
                  },
                  "Justification_ID": {
                    "0": "mislabeled food@1 for evac@2",
                    "1": "Segment-0",
                    "2": "Segment-0",
                    "3": "nonexistant1",
                    "4": "nonexistant2",
                    "5": "Segment-0",
                    "6": "Segment-0",
                    "7": "Segment-0",
                    "8": "Segment-0",
                    "9": "Segment-0"
                  },
                  "Place_KB_ID": {
                    "0": "2",
                    "1": "2",
                    "2": "2",
                    "3": "3",
                    "4": "3",
                    "5": "9",
                    "6": "9",
                    "7": "1",
                    "8": "1",
                    "9": "4"
                  },
                  "Resolution": {
                    "0": "insufficient",
                    "1": "insufficient",
                    "2": "insufficient",
                    "3": "insufficient",
                    "4": "insufficient",
                    "5": "insufficient",
                    "6": "insufficient",
                    "7": "insufficient",
                    "8": "insufficient",
                    "9": "insufficient"
                  },
                  "Status": {
                    "0": "current",
                    "1": "current",
                    "2": "current",
                    "3": "current",
                    "4": "current",
                    "5": "current",
                    "6": "current",
                    "7": "current",
                    "8": "current",
                    "9": "current"
                  },
                  "Type": {
                    "0": "evac",
                    "1": "evac",
                    "2": "evac",
                    "3": "shelter",
                    "4": "shelter",
                    "5": "water",
                    "6": "water",
                    "7": "food",
                    "8": "food",
                    "9": "shelter"
                  },
                  "urgent": {
                    "0": true,
                    "1": true,
                    "2": true,
                    "3": true,
                    "4": true,
                    "5": true,
                    "6": true,
                    "7": true,
                    "8": true,
                    "9": true
                  },
                  "unresolved": {
                    "0": true,
                    "1": true,
                    "2": true,
                    "3": true,
                    "4": true,
                    "5": true,
                    "6": true,
                    "7": true,
                    "8": true,
                    "9": true
                  },
                  "current": {
                    "0": true,
                    "1": true,
                    "2": true,
                    "3": true,
                    "4": true,
                    "5": true,
                    "6": true,
                    "7": true,
                    "8": true,
                    "9": true
                  },
                  "gravity": {
                    "0": true,
                    "1": true,
                    "2": true,
                    "3": true,
                    "4": true,
                    "5": true,
                    "6": true,
                    "7": true,
                    "8": true,
                    "9": true
                  },
                  "frame_count": {
                    "0": 1,
                    "1": 1,
                    "2": 1,
                    "3": 1,
                    "4": 1,
                    "5": 1,
                    "6": 1,
                    "7": 1,
                    "8": 1,
                    "9": 1
                  }
                }'''
        self.myref = pd.DataFrame.from_dict(json.loads(myrefstr))
        self.mysys1 = pd.DataFrame.from_dict(json.loads(mysysstr1))

    def test_precisionN(self):
        myprecisionN = precisionN(self.myref, self.mysys1)
        correctPrecisionN = [(1, 1.0), (2, 0.5)]
        TestCase.assertListEqual(self, myprecisionN, correctPrecisionN)
