#!/usr/bin/env bash

# ------------------------------------------------------------------------------
# NER LOREHLT - Scoring step
# Author: lukas.diduch@nist.gov
#   0.3  2016-06-01, upadtes for dryrun
# ------------------------------------------------------------------------------

echo "- ${0}"
# Get env from job-config
#source $1


function check_error() {
    EXIT_STAT=$1
    if [ $EXIT_STAT -ne 0 ]; then
        echo "(${0}) exit stat: $EXIT_STAT"
        exit $EXIT_STAT
    fi
}

set -x
pwd

python --version

OURFILE=$1
SYSNAME=$2
SCORE_DIR=$3

# Pick up any first .tab file and designate it as the file to score.


#OURFILE=$(ls $UNCOMPRESS_DIR/*.json | head -n 1)

#cd /data/LOREHLT-SF/SF-Scorer 
#$MODDIR/2016ner_bin/score_submission.sh \
./LoReHLT_Frame_Scorer.py \
    -g ./datasets/IL10/situation_frame/ \
    -s $OURFILE \
    -o $SCORE_DIR \
    -m $SYSNAME \
    -l ./datasets/IL10/IL10_all_filelist.txt \
    -p IL10_CP2_all_ 

check_error $?

./LoReHLT_Frame_Scorer.py \
    -g ./datasets/IL10/situation_frame/ \
    -s $OURFILE \
    -o $SCORE_DIR \
    -m $SYSNAME \
    -l ./datasets/IL10/IL10_filelist.txt \
    -p IL10_CP2_IL_text_

check_error $?

./LoReHLT_Frame_Scorer.py \
    -g ./datasets/IL10/situation_frame/ \
    -s $OURFILE \
    -o $SCORE_DIR \
    -m $SYSNAME \
    -l ./datasets/IL10/ENG_IL10_filelist.txt \
    -p IL10_CP2_ENG_text_ 

check_error $?

./LoReHLT_Frame_Scorer.py \
    -g ./datasets/IL10/situation_frame/ \
    -s $OURFILE \
    -o $SCORE_DIR \
    -m $SYSNAME \
    -l ./datasets/IL10/IL10+ENG_filelist.txt \
    -p IL10_CP2_IL+ENG_text_ 

check_error $?

./LoReHLT_Frame_Scorer.py \
    -g ./datasets/IL10/situation_frame/ \
    -s $OURFILE \
    -o $SCORE_DIR \
    -m $SYSNAME \
    -l ./datasets/IL10/IL10_speech_filelist.txt \
    -p IL10_CP2_speech_ 

check_error $?


#cd -

#EXIT_STAT=$?
#if [ "$EXIT_STAT" -eq "0" ]; then 
#  echo "(${0}) checking logfile for anormalities.."
#  EXIT_STAT=$(grep -ic error $EVALDIR/3-score.log)
#fi

echo "(${0}) exit stat: $EXIT_STAT"
exit $EXIT_STAT
