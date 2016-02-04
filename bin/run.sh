#!/bin/bash

#========================================================================
# FILE NAME:    run.sh
# FUNCTION:     Call program
# VERSION:      1.0
# AUTHOR:       S.Yatsuzuka
# 
# Copyright (C) 2016 NASEBANAL
#========================================================================


#======= Check Arguments =======

if [ $# -ne 1 -a $# -ne 2 ]; then

    echo
    echo "Usage: $0 <Parameter File> [Output File]"
    echo
        exit 1
fi


#======= Get Arguments =======

PARAM_FILE=$1
echo "PARAM_FILE    = ${PARAM_FILE}"

if [ $# = 2 ]; then

    OUTPUT_FILE=$2
    echo "OUTPUT_FILE   = ${OUTPUT_FILE}"
fi


#======= Check NB Home =======

if [ ${#NB_HOME} = 0 ]; then

    echo
    echo "ERROR: NB_HOME isn't set as environment variable"
    echo
    exit 1
fi


#======= Check OpenCV Home =======

if [ ${#OPENCV_HOME} = 0 ]; then

    echo
    echo "ERROR: OPENCV_HOME isn't set as environment variable"
echo
exit 1

fi

#======= Get Parameter =======

source ${PARAM_FILE}
echo "CMD   = ${NB_CMD}"

#======= Call Program =======

if [ $# = 1 ]; then

    ${NB_CMD}

elif [ $# = 2 ]; then

    ${NB_CMD} > ${OUTPUT_FILE}
fi

