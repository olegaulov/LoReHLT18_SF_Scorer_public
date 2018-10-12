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

    debug = False

    # argument parser ----------------------------------------------------------
    if not debug:
        parser = argparse.ArgumentParser(description='Convert Mandarin annotation files to mimic IL9 and IL10 format')
        parser.add_argument('-s', '--source', help='Path to the old CMN annotation with "need" and "issue" folders', required=True)
        parser.add_argument('-t', '--target', help='Path to the output directory', required=True)
        parser.add_argument('-e', '--edl-file', help='Path to cmn_new_gold.tab', required=True)

        args = parser.parse_args()

        inpath  = args.source
        outpath = args.target
        edlpath = args.edl_file

    # create output directory
    try:
        if not os.path.exists(outpath): os.makedirs(outpath) 
    except:
        sys.exit('CAN NOT CREATE OUTPUT DIRECTORY: '+ outpath)


    kbids = pd.read_csv(edlpath, engine='python', index_col=None, sep='\t', quoting=csv.QUOTE_NONE, header=None, names = ["reftype", "refmention", "reftext", "refdocid", "kb_id", "reft", "refst", "ones"])

    # get mentions and merge with kbids
    allFiles = glob.glob(inpath + "/mentions/*.tab")
    #print(allFiles)
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df2 = pd.read_csv(file_, engine='python', index_col=None, header=0, sep='\t', quoting=csv.QUOTE_NONE)
        df2["doc_id2"] = df2["doc_id"].map(str) + ":" + df2["start_char"].map(str) + "-" + df2["end_char"].map(str)
        list_.append(df2)
    if len(list_) == 0:
        sys.exit('ERROR: failed to find "mentions" reference files.\nMake sure the -t argument '\
            'path points to a directory containing "/mentions/", "/needs/", and "/issues/" subdirectories.\n')

    mentions = pd.concat(list_)
    #merged = pd.merge(mentions, kbids, how='left', left_on=['doc_id2','mention_id'], right_on = ['refdocid','refmention'])
    merged = pd.merge(mentions, kbids, how='left', left_on=['doc_id2'], right_on = ['refdocid'])
    merged = merged.drop(merged.columns[[8,9,10,11,12,14,15,16]], axis=1) 



    # Do Needs
    allFiles = glob.glob(inpath + "/needs/" + "*.tab")
    list_ = []
    try:
        if not os.path.exists(outpath + "/needs/"): os.makedirs(outpath + "/needs/") 
    except:
        sys.exit('CAN NOT CREATE OUTPUT DIRECTORY: '+ outpath + "/needs/")
    if len(allFiles) ==0:
        print('WARNING: No "needs" annotation files found.')
    for file_ in allFiles:
        sf = pd.read_csv(file_, engine='python', index_col=None, header=0, sep='\t', quoting=csv.QUOTE_NONE)
        d = {True: 4, False: 1}
        sf['scope'] = sf['urgency_status'].map(d)
        sf['severity'] = sf['urgency_status'].map(d)
        #sf['scope'] = np.random.choice([1,2,3,4], sf.shape[0])
        #sf['severity'] = np.random.choice([1,2,3,4], sf.shape[0])
        sf = sf[['user_id','doc_id','frame_id','frame_type','need_type','place_id','proxy_status','need_status','scope','severity','resolution_status','reported_by','resolved_by','description']]
        sfout = pd.merge(sf, merged, how='left', left_on=['doc_id','place_id'], right_on = ['doc_id','entity_id']).reset_index(drop=True)
        sfout = sfout.drop(sfout.columns[[14,15,16,17,18,19,20]], axis=1) 
        sfout.to_csv(path_or_buf = outpath + "/needs/" + os.path.basename(file_), sep='\t', index=False, mode='w')

    # Do Issues
    try:
        if not os.path.exists(outpath + "/issues/"): os.makedirs(outpath + "/issues/") 
    except:
        sys.exit('CAN NOT CREATE OUTPUT DIRECTORY: '+ outpath + "/issues/")
    allFiles = glob.glob(inpath + "/issues/" + "*.tab")
    list_ = []
    if len(allFiles) ==0:
        print('WARNING: No "issues" annotation files found.')
    for file_ in allFiles:
        sf = pd.read_csv(file_, engine='python', index_col=None, header=0, sep='\t', quoting=csv.QUOTE_NONE)
        sf['scope'] = np.random.choice([1,2,3,4], sf.shape[0])
        sf['severity'] = np.random.choice([1,2,3,4], sf.shape[0])
        sf = sf[['user_id','doc_id','frame_id','frame_type','issue_type','place_id','proxy_status','issue_status','scope','severity','description']]
        sfout = pd.merge(sf, merged, how='left', left_on=['doc_id','place_id'], right_on = ['doc_id','entity_id'])
        sfout = sfout.drop(sfout.columns[[11, 12,13,14,15,16,17]], axis=1)
        sfout.to_csv(path_or_buf = outpath + "/issues/" + os.path.basename(file_), sep='\t', index=False, mode='w')
    print("Success!\n")


