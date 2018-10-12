LoReHLT 2018 Situation Frame Scorer

Date 07/09/2018

This package includes the system output scorer for the LoReHLT
Situation Frame (SF) Evalaution task for year 2018.  The release includes
the Python script 'LoReHLT_Frame_Scorer.py', which validates and scores SF
system output files.


Below is an example command that would run the scoring script acainst an
SF system output json file named 2018_CMN_system_output.json. 

LoReHLT_Frame_Scorer.py -s /Data/2018_CMN_system_output.json \
-g /Data/DryRun/CMN -o /Data/Scores/ -m SF_Primary_System

Optionally, -t argument allows to run the scorer only on frames that are equal to or 
above the specified threshold. For example -t 0.3


Ground truth tab delimited files are expected to be in the directory
specified by the -g argument. This directory is expected to contain "needs" 
and issues" subdirectories. The scorer output files are written
to the directory specified by the -o argument. Argument -m specifies the 
SF system name.


Annotation Convertion Script:

The dryrun is conducted on Chineese Mandarin language (CMN), however the
annotation for this language is substantially different from the annotation
that will be provided for IL9 and IL10. In order to better exercise the
scorer, a conversinon script is provided that converts old CMN annotation
to be consistent with the expected format of the new IL9 IL10 annotation.
This script is intended for pipeline exercise only, and does not result in
meaningful annotatinon. Some fields are randomly generated.

./utils/referenceConverter_2018.py \
-s ./datasets/CMN_Reference/setE/data/annotation/situation_frame/  \
-e ./datasets/CMN_EDL/2018_cmn_gold.tab \
-t /New_CMN/


Perfect Score Generation Script:

Additionally, a perfect score generating script is included for testing 
perposes. Such a script can be invoked as follows:

./utils/perfectScore_2018.py -s ~/Desktop/testoutputCMN/ -t ~/Desktop/perfectCMN.json


A collection of unit test cases is under development and will be included
in future releases.


LoReHLT_Frame_Scorer.py when run with the '-h' option, or without
arguments, will show the usage text.

The scoring script performs the following steps ..
  - JSON validation
  - Ingestion of reference files
  - Scoring (note that output files will be overwritten on subsequent
    runs without prompt)
  * Exits with status of 0 if scoring was succesful, and 1 otherwise

Setup:

  The LoReHLT_Frame_Scorer.py is a Python script and requires:
  Python version 3.5.0 or later,
  Numpy version 1.13.3 or later,
  Pandas version 0.22.0 or later,
  Matplotlib 2.1.0 or later,
  Jsonschema 2.6.0 or later

Changelog:

  07/08/2018 (1.0.4)
    - Fixed bug in nDCG that would order situations in the wrong order

  07/08/2018 (1.0.3)

    - Several bug fixes in MAP and MAR calculations that would result in NaN
      if no correct frames were found
    - Added test cases to ./tests/ folder to test the MAP MAR functions 

  06/29/2018 (1.0.2)

    - Bug fix in nDCG score that would ignore undiscovered situations
    - Bug fix in system output processing that would have missing columns
      if very few frames are present, and would cause the scorer to crash

  06/26/2018 (1.0.1)

    - Added option to set up Gain and number of grave frames for each
      gravity group of the nDCG metric

  06/10/2018 (1.0)

    - Fixed several bugs.
    - Added perfect score generator
    - Restructured the project

  05/15/18 (0.8):

    - Initial development release

Authors:

  Oleg Aulov <oleg.aulov@nist.gov>

Copyright:

  Full details can be found at: http://nist.gov/data/license.cfm

  This software was developed at the National Institute of Standards
  and Technology by employees of the Federal Government in the course
  of their official duties.  Pursuant to Title 17 Section 105 of the
  United States Code this software is not subject to copyright
  protection within the United States and is in the public domain.
  NIST assumes no responsibility whatsoever for its use by any party,
  and makes no guarantees, expressed or implied, about its quality,
  reliability, or any other characteristic.

  We would appreciate acknowledgement if the software is used.  This
  software can be redistributed and/or modified freely provided that
  any derivative works bear some notice that they are derived from it,
  and any modified versions bear some notice that they have been
  modified.

  THIS SOFTWARE IS PROVIDED "AS IS."  With regard to this software,
  NIST MAKES NO EXPRESS OR IMPLIED WARRANTY AS TO ANY MATTER
  WHATSOEVER, INCLUDING MERCHANTABILITY, OR FITNESS FOR A PARTICULAR
  PURPOSE.

