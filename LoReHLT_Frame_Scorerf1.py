#!/usr/bin/env python3

__author__ = "Oleg Aulov (oleg.aulov@nist.gov)"
__version__ = "Development: 1.0.4"
__date__ = "07/09/2018"

################################################################################
# MAIN
################################################################################


import argparse
from lib.lorehlt18helper import *

if __name__ == "__main__":

    debug = False

    # argument parser ----------------------------------------------------------
    parser = argparse.ArgumentParser(description='Generates PR curves for the LORELEI speech evaluation')
    parser.add_argument('-s', '--system-output', help='Path to the system output', required=True)
    parser.add_argument('-g', '--ground-truth', help='Path to the ground truth directory', required=True)
    parser.add_argument('-l', '--filelist', help='Path to the ground truth directory', required=False)
    parser.add_argument('-o', '--output-directory', help='Path to save the evaluation output', required=True)
    parser.add_argument('-m', '--system-name', help='Name of the SF system', required=True)
    parser.add_argument('-p', '--filename-prefix', help='prefix for output files', required=False, default="")
    parser.add_argument('-t', '--system-threshold', help='Threshold', required=False, default=0, type=float)

    args = parser.parse_args()
    # print (args)

    referencePath = args.ground_truth
    referenceFilelist = args.filelist
    systemPath = args.system_output
    outputDir = args.output_directory
    systemName = args.system_name
    threshold = args.system_threshold
    fnprefix = args.filename_prefix
    # create output directory
    try:
        if not os.path.exists(outputDir): os.makedirs(outputDir)
    except:
        sys.exit('CAN NOT CREATE OUTPUT DIRECTORY: ' + outputDir)

    # basic error checks -------------------------------------------------------
    if not os.path.exists(referencePath):
        sys.exit('PATH NOT FOUND: ' + referencePath)

    if not os.path.exists(systemPath):
        sys.exit('PATH NOT FOUND: ' + systemPath)


    referenceTable = getReference(path=referencePath, gravity=gravity, filelist = referenceFilelist)
    systemTable = getsubmission(filename=systemPath, gravity=gravity, filelist = referenceFilelist)
    systemTable = correctkbids(systemTable, referenceTable)

    systemTable = systemTable[["DocumentID","Type", "Place_KB_ID"]]
    referenceTable= referenceTable[["doc_id", "type", "kb_id"]]

    merged = pd.merge(systemTable, referenceTable, left_on=['DocumentID', "Type"], right_on=['doc_id', 'type'], how='inner')
    
    try:
        myprecision = merged.shape[0] / systemTable.shape[0]
    except ZeroDivisionError:
        myprecision = 0
    try:
        myrecall = merged.shape[0] / referenceTable.shape[0]
    except ZeroDivisionError:
        myrecall = 0
    try:
        myf1 = 2 * ((myprecision * myrecall) / (myprecision + myrecall))
    except ZeroDivisionError:
        myf1 = 0

    filename = os.path.join(outputDir,fnprefix + '_F1_type.txt')

    with open(filename, 'w') as F_results_file:
        F_results_file.write("F1_Type:\t"  + str(myf1) + "\n")
        F_results_file.write("Precision_Type:\t"  + str(myprecision) + "\n")
        F_results_file.write("Recall_Type:\t"  + str(myrecall) + "\n")


    merged = pd.merge(systemTable, referenceTable, left_on=['DocumentID', "Type", "Place_KB_ID"], right_on=['doc_id', 'type', 'kb_id'], how='inner')
    
    try:
        myprecision = merged.shape[0] / systemTable.shape[0]
    except ZeroDivisionError:
        myprecision = 0
    try:
        myrecall = merged.shape[0] / referenceTable.shape[0]
    except ZeroDivisionError:
        myrecall = 0
    try:
        myf1 = 2 * ((myprecision * myrecall) / (myprecision + myrecall))
    except ZeroDivisionError:
        myf1 = 0

    filename = os.path.join(outputDir,fnprefix + '_F1_type_place.txt')

    with open(filename, 'w') as F_results_file:
        F_results_file.write("F1_TypePlace:\t"  + str(myf1) + "\n")
        F_results_file.write("Precision_TypePlace:\t"  + str(myprecision) + "\n")
        F_results_file.write("Recall_TypePlace:\t"  + str(myrecall) + "\n")
    print("Success!")
