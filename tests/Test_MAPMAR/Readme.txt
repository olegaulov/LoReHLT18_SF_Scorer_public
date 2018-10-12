Test 1:
same situation listed twice make sure the scorer only keeps one with higher confidence
contains one frame for situation not in reference, should be ignired.

Type+Place:
avgprecision:  1.0
recall: 1.0

Type+Place+Status:
avgprecision:  1.0
recall: 1.0

Type+Place+Status+Urgency:
avgprecision:  1.0
recall: 1.0

Type+Place+Status+Resolution:
avgprecision:  1.0
recall: 1.0

Type+Place+Status+Urgency+Resolution:
avgprecision:  1.0
recall: 1.0


Test 2:
wrong status 2nd frame, wrong urgency 1st frame
File 1 - additional wrong frame

Type+Place:
avgprecision:  1
recall: 1

Type+Place+Status:
avgprecision:  2/3
recall: 1/2

Type+Place+Status+Urgency:
avgprecision:  1/3
recall: 1/3


Type+Place+Status+Resolution:
avgprecision:  2/3
recall: 1/2

Type+Place+Status+Urgency+Resolution:
avgprecision:  1/3
recall: 1/3


Test 3:
2nd frame wrong resolution, 1st frame wrong urgency
File 1 - additional wrong frame

Type+Place:
avgprecision:  1.0
recall: 1.0

Type+Place+Status:
avgprecision:  1.0
recall: 1.0

Type+Place+Status+Urgency:
avgprecision:  0.78
recall: 0.83

Type+Place+Status+Resolution:
avgprecision:  0.67
recall: 0.5

Type+Place+Status+Urgency+Resolution:
avgprecision:  0.33
recall: 0.33


