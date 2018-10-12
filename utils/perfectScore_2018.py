#!/usr/bin/env python3

__author__ = "Oleg Aulov (oleg.aulov@nist.gov)"
__version__ = "Development: 0.8"
__date__ = "05/14/2018"

import argparse
import glob
import numpy as np
import pandas as pd
import csv
import os
import sys

if __name__ == "__main__":

    from sys import path
    from os.path import dirname
    path.append(dirname(path[0]))

    #import lib.lorehlt18helper
    from lib.lorehlt18helper import *

    debug = False

    # argument parser ----------------------------------------------------------
    if not debug:
        parser = argparse.ArgumentParser(description='Generate a perfect score json submission file from the Mandarin annotation files')
        parser.add_argument('-s', '--source', help='Path to the CMN annotation with "need" and "issue" folders', required=True)
        parser.add_argument('-t', '--target', help='Path to the output json file', required=True)

        args = parser.parse_args()

        inpath  = args.source
        outpath = args.target

    reference = getreference(inpath, gravity = gravity)
    reference.kb_id = reference.kb_id.replace(pd.np.nan, '', regex=True)

    #Perfect Submission from reference
    list_ = []
    for index, row in reference.iterrows():
        if row["type"] == "crimeviolence" or row["type"] == "regimechange" or row["type"] == "terrorism":
            dicframe = {'DocumentID':row["doc_id"],
                 'Type':row["type"],
                 'Justification_ID':"Segment-0",
                 'Place_KB_ID':row["kb_id"],
                 'Confidence':1,
                 'Status':row["status"],
                 'Urgent':row["urgent"]}
        else:
            dicframe = {'DocumentID':row["doc_id"],
                 'Type':row["type"],
                 'Justification_ID':"Segment-0",
                 'Place_KB_ID':row["kb_id"],
                 'Confidence':1,
                 'Status':row["status"],
                 'Resolution':row["resolution_status"],
                 'Urgent':row["urgent"]}
        list_.append(dicframe)


    try:
        if not os.path.exists(dirname(outpath)): os.makedirs(dirname(outpath)) 
    except:
        sys.exit('CAN NOT CREATE OUTPUT DIRECTORY: '+ dirname(outpath))
    try:
        with open(outpath, 'w') as fp:
            json.dump(list_, fp, indent=4)
    except:
        sys.exit('CAN NOT CREATE OUTPUT FILE: '+ outpath)
    print("Success!\n")
    
