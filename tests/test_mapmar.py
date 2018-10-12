from unittest import TestCase
import numpy.testing as npt
import sys
import os

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
sys.path.append(lib_path)

from lib.lorehlt18helper import *

class TestMapmar(TestCase):
    def setUp(self):
        self.referenceTableStr = '''{
                                  "doc_id": {
                                    "0": "File_1",
                                    "1": "File_1",
                                    "2": "File_1",
                                    "3": "File_2",
                                    "4": "File_2",
                                    "5": "File_3"
                                  },
                                  "frame_id": {
                                    "0": "Frame-1",
                                    "1": "Frame-1",
                                    "2": "Frame-1",
                                    "3": "Frame-1",
                                    "4": "Frame-1",
                                    "5": "Frame-1"
                                  },
                                  "kb_id": {
                                    "0": "1",
                                    "1": "1",
                                    "2": "1",
                                    "3": "1",
                                    "4": "1",
                                    "5": "1"
                                  },
                                  "user_id": {
                                    "0": 1,
                                    "1": 2,
                                    "2": 3,
                                    "3": 1,
                                    "4": 2,
                                    "5": 1
                                  },
                                  "type": {
                                    "0": "food",
                                    "1": "food",
                                    "2": "food",
                                    "3": "food",
                                    "4": "food",
                                    "5": "food"
                                  },
                                  "urgent": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true,
                                    "4": true,
                                    "5": false
                                  },
                                  "unresolved": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true,
                                    "4": true,
                                    "5": true
                                  },
                                  "current": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true,
                                    "4": true,
                                    "5": true
                                  },
                                  "gravity": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true,
                                    "4": true,
                                    "5": false
                                  },
                                  "frame_count": {
                                    "0": 1,
                                    "1": 1,
                                    "2": 1,
                                    "3": 1,
                                    "4": 1,
                                    "5": 1
                                  }
                                }'''

        self.systemTableStr1 = '''{
                              "Confidence": {
                                "0": 0.8,
                                "1": 0.79,
                                "2": 0.7,
                                "3": 0.9,
                                "4": 0.85
                              },
                              "DocumentID": {
                                "0": "File_1",
                                "1": "File_1",
                                "2": "File_2",
                                "3": "File_3",
                                "4": "File_1"
                              },
                              "Justification_ID": {
                                "0": "segment-0",
                                "1": "cheatersDuplicate",
                                "2": "segment-0",
                                "3": "segment-0",
                                "4": "wrongframe"
                              },
                              "Place_KB_ID": {
                                "0": "1",
                                "1": "1",
                                "2": "1",
                                "3": "1",
                                "4": "1"
                              },
                              "Resolution": {
                                "0": "insufficient",
                                "1": "insufficient",
                                "2": "insufficient",
                                "3": "insufficient",
                                "4": "insufficient"
                              },
                              "Status": {
                                "0": "current",
                                "1": "future",
                                "2": "current",
                                "3": "current",
                                "4": "current"
                              },
                              "Type": {
                                "0": "food",
                                "1": "food",
                                "2": "food",
                                "3": "food",
                                "4": "shelter"
                              },
                              "urgent": {
                                "0": true,
                                "1": false,
                                "2": true,
                                "3": false,
                                "4": true
                              },
                              "unresolved": {
                                "0": true,
                                "1": true,
                                "2": true,
                                "3": true,
                                "4": true
                              },
                              "current": {
                                "0": true,
                                "1": false,
                                "2": true,
                                "3": true,
                                "4": true
                              },
                              "gravity": {
                                "0": true,
                                "1": false,
                                "2": true,
                                "3": false,
                                "4": true
                              },
                              "frame_count": {
                                "0": 1,
                                "1": 1,
                                "2": 1,
                                "3": 1,
                                "4": 1
                              }
                            }'''

        self.systemTableStr2 = '''{
                                  "Confidence": {
                                    "0": 0.8,
                                    "1": 0.7,
                                    "2": 0.9,
                                    "3": 0.85
                                  },
                                  "DocumentID": {
                                    "0": "File_1",
                                    "1": "File_2",
                                    "2": "File_3",
                                    "3": "File_1"
                                  },
                                  "Justification_ID": {
                                    "0": "missStatus",
                                    "1": "segment-0",
                                    "2": "segment-0",
                                    "3": "wrongframe"
                                  },
                                  "Place_KB_ID": {
                                    "0": "1",
                                    "1": "1",
                                    "2": "1",
                                    "3": "1"
                                  },
                                  "Resolution": {
                                    "0": "insufficient",
                                    "1": "insufficient",
                                    "2": "insufficient",
                                    "3": "insufficient"
                                  },
                                  "Status": {
                                    "0": "past",
                                    "1": "current",
                                    "2": "current",
                                    "3": "current"
                                  },
                                  "Type": {
                                    "0": "food",
                                    "1": "food",
                                    "2": "food",
                                    "3": "shelter"
                                  },
                                  "urgent": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "unresolved": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "current": {
                                    "0": false,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "gravity": {
                                    "0": false,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "frame_count": {
                                    "0": 1,
                                    "1": 1,
                                    "2": 1,
                                    "3": 1
                                  }
                                }'''

        self.systemTableStr3 = '''{
                                  "Confidence": {
                                    "0": 0.8,
                                    "1": 0.7,
                                    "2": 0.9,
                                    "3": 0.85
                                  },
                                  "DocumentID": {
                                    "0": "File_1",
                                    "1": "File_2",
                                    "2": "File_3",
                                    "3": "File_1"
                                  },
                                  "Justification_ID": {
                                    "0": "missResolution",
                                    "1": "segment-0",
                                    "2": "segment-0",
                                    "3": "wrongframe"
                                  },
                                  "Place_KB_ID": {
                                    "0": "1",
                                    "1": "1",
                                    "2": "1",
                                    "3": "1"
                                  },
                                  "Resolution": {
                                    "0": "sufficient",
                                    "1": "insufficient",
                                    "2": "insufficient",
                                    "3": "insufficient"
                                  },
                                  "Status": {
                                    "0": "current",
                                    "1": "current",
                                    "2": "current",
                                    "3": "current"
                                  },
                                  "Type": {
                                    "0": "food",
                                    "1": "food",
                                    "2": "food",
                                    "3": "shelter"
                                  },
                                  "urgent": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "unresolved": {
                                    "0": false,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "current": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "gravity": {
                                    "0": false,
                                    "1": true,
                                    "2": true,
                                    "3": true
                                  },
                                  "frame_count": {
                                    "0": 1,
                                    "1": 1,
                                    "2": 1,
                                    "3": 1
                                  }
                                }'''

        self.systemTableStr4 = '''{
                                  "Confidence": {
                                    "0": 0.8,
                                    "1": 0.79,
                                    "2": 0.7,
                                    "3": 0.9,
                                    "4": 0.85
                                  },
                                  "DocumentID": {
                                    "0": "File_1",
                                    "1": "File_1",
                                    "2": "File_2",
                                    "3": "File_3",
                                    "4": "File_1"
                                  },
                                  "Justification_ID": {
                                    "0": "segment-0",
                                    "1": "cheatersDuplicate",
                                    "2": "segment-0",
                                    "3": "segment-0",
                                    "4": "wrongframe"
                                  },
                                  "Place_KB_ID": {
                                    "0": "1",
                                    "1": "1",
                                    "2": "1",
                                    "3": "1",
                                    "4": "1"
                                  },
                                  "Resolution": {
                                    "0": "insufficient",
                                    "1": "insufficient",
                                    "2": "insufficient",
                                    "3": "insufficient",
                                    "4": "insufficient"
                                  },
                                  "Status": {
                                    "0": "current",
                                    "1": "future",
                                    "2": "current",
                                    "3": "past",
                                    "4": "current"
                                  },
                                  "Type": {
                                    "0": "food",
                                    "1": "food",
                                    "2": "food",
                                    "3": "food",
                                    "4": "shelter"
                                  },
                                  "urgent": {
                                    "0": true,
                                    "1": false,
                                    "2": true,
                                    "3": false,
                                    "4": true
                                  },
                                  "unresolved": {
                                    "0": true,
                                    "1": true,
                                    "2": true,
                                    "3": true,
                                    "4": true
                                  },
                                  "current": {
                                    "0": true,
                                    "1": false,
                                    "2": true,
                                    "3": false,
                                    "4": true
                                  },
                                  "gravity": {
                                    "0": true,
                                    "1": false,
                                    "2": true,
                                    "3": false,
                                    "4": true
                                  },
                                  "frame_count": {
                                    "0": 1,
                                    "1": 1,
                                    "2": 1,
                                    "3": 1,
                                    "4": 1
                                  }
                                }'''

        self.referenceTable = pd.DataFrame.from_dict(json.loads(self.referenceTableStr))
        self.systemTable1 = pd.DataFrame.from_dict(json.loads(self.systemTableStr1))
        self.systemTable2 = pd.DataFrame.from_dict(json.loads(self.systemTableStr2))
        self.systemTable3 = pd.DataFrame.from_dict(json.loads(self.systemTableStr3))
        self.systemTable4 = pd.DataFrame.from_dict(json.loads(self.systemTableStr4))

    def test_mapmar_type_place_1(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable1, genTrue_TypePlace)
        npt.assert_almost_equal(mymap,1.0, decimal = 9)
        npt.assert_almost_equal(mymar,1.0, decimal = 9)

    def test_mapmar_type_place_2(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable2, genTrue_TypePlace)
        npt.assert_almost_equal(mymap,1.0, decimal = 9)
        npt.assert_almost_equal(mymar,1.0, decimal = 9)

    def test_mapmar_type_place_3(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable3, genTrue_TypePlace)
        npt.assert_almost_equal(mymap, 1.0, decimal=9)
        npt.assert_almost_equal(mymar, 1.0, decimal=9)

    def test_mapmar_type_place_status_1(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable1, genTrue_TypePlaceStatus)
        npt.assert_almost_equal(mymap,1.0, decimal = 9)
        npt.assert_almost_equal(mymar,1.0, decimal = 9)

    def test_mapmar_type_place_status_2(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable2, genTrue_TypePlaceStatus)
        npt.assert_almost_equal(mymap,0.66666666666666674, decimal = 9)
        npt.assert_almost_equal(mymar,0.5, decimal = 9)

    def test_mapmar_type_place_status_3(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable3, genTrue_TypePlaceStatus)
        npt.assert_almost_equal(mymap, 1.0, decimal=9)
        npt.assert_almost_equal(mymar, 1.0, decimal=9)

    def test_mapmar_type_place_status_urgency_1(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable1, genTrue_TypePlaceStatusUrgency)
        npt.assert_almost_equal(mymap,1.0, decimal = 9)
        npt.assert_almost_equal(mymar,1.0, decimal = 9)

    def test_mapmar_type_place_status_urgency_2(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable2, genTrue_TypePlaceStatusUrgency)
        npt.assert_almost_equal(mymap,0.33333333333333331, decimal = 9)
        npt.assert_almost_equal(mymar,0.33333333333333331, decimal = 9)

    def test_mapmar_type_place_status_urgency_3(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable3, genTrue_TypePlaceStatusUrgency)
        npt.assert_almost_equal(mymap, 0.78333333333333333, decimal=9)
        npt.assert_almost_equal(mymar, 0.83333333333333337, decimal=9)

    def test_mapmar_type_place_status_resolution_1(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable1, genTrue_TypePlaceStatusResolution)
        npt.assert_almost_equal(mymap,1.0, decimal = 9)
        npt.assert_almost_equal(mymar,1.0, decimal = 9)

    def test_mapmar_type_place_status_resolution_2(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable2, genTrue_TypePlaceStatusResolution)
        npt.assert_almost_equal(mymap,0.66666666666666674, decimal = 9)
        npt.assert_almost_equal(mymar,0.5, decimal = 9)

    def test_mapmar_type_place_status_resolution_3(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable3, genTrue_TypePlaceStatusResolution)
        npt.assert_almost_equal(mymap, 0.66666666666666674, decimal=9)
        npt.assert_almost_equal(mymar, 0.5, decimal=9)

    def test_mapmar_type_place_status_urgency_resolution_1(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable1, genTrue_TypePlaceStatusUrgencyResolution)
        npt.assert_almost_equal(mymap,1.0, decimal = 9)
        npt.assert_almost_equal(mymar,1.0, decimal = 9)

    def test_mapmar_type_place_status_urgency_resolution_2(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable2, genTrue_TypePlaceStatusUrgencyResolution)
        npt.assert_almost_equal(mymap,0.33333333333333331, decimal = 9)
        npt.assert_almost_equal(mymar,0.33333333333333331, decimal = 9)

    def test_mapmar_type_place_status_urgency_resolution_3(self):
        mymap, mymar = mapmar(self.referenceTable, self.systemTable3, genTrue_TypePlaceStatusUrgencyResolution)
        npt.assert_almost_equal(mymap, 0.33333333333333331, decimal=9)
        npt.assert_almost_equal(mymar, 0.33333333333333331, decimal=9)

    def test_mapmar_type_place_status_urgency_resolution_Urgent_Unresolved_1(self):
        referenceGraveTable = self.referenceTable[(self.referenceTable.urgent == True) & (self.referenceTable.unresolved == True)]
        systemGraveTable = self.systemTable4[(self.systemTable4.urgent == True) & (self.systemTable4.unresolved == True)]
        mymap1, mymar1 = mapmar(referenceGraveTable, systemGraveTable, genTrue_TypePlaceStatusUrgencyResolution)
        mymap2, mymar2 = mapmar(self.referenceTable, self.systemTable4, genTrue_TypePlaceStatusUrgencyResolution)

        npt.assert_almost_equal(mymap1, 1.0, decimal=9)
        npt.assert_almost_equal(mymar1, 1.0, decimal=9)
        npt.assert_almost_equal(mymap2, 0.78333333333333333, decimal=9)
        npt.assert_almost_equal(mymar2, 0.83333333333333337, decimal=9)
