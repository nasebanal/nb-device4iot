#!/bin/bash

#========================================================================
# FILE NAME:    get_image.sh
# FUNCTION:     Get image and transfer it to AWS
# VERSION:      1.0
# AUTHOR:       S.Yatsuzuka
# 
# Copyright (C) 2016 NASEBANAL
#========================================================================


#======= Check Arguments =======

if [ $# -eq 0 -o $# -gt 2 ]; then

    echo
    echo "Usage: $0 <Mode> [Output File]"
    echo
    echo "  <Mode>"
    echo "      0: loop"
    echo "      other: one time"
    echo
    echo "  [Output File]"
    echo "      log file name (optional)"
    echo
        exit 1
fi


#======= Get Arguments =======

MODE=$1

if [ $# -eq 2 ]; then

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


#======= Check PID file =======

PIDFILE=${NB_HOME}/temp/pid.txt

if [ -e ${PIDFILE} ]; then

    echo "INFO: pidfile exists"
    exit 0
fi

echo $$ > ${PIDFILE}


#======= Get Parameter =======

source ${NB_HOME}/param/get_image.param
echo "CMD   = ${NB_CMD}"


#======= Get Work Orders =======


#======= Call Program =======

while [ 1 ]
do

    DATE=`date +%Y%m%d%H%M%S`
    IMAGE_FILE=img_${DATE}.jpg
    echo "IMAGE_FILE    = ${IMAGE_FILE}"

    if [ $# = 1 ]; then

        ${NB_CMD}

    elif [ $# = 2 ]; then

        ${NB_CMD} > ${OUTPUT_FILE}
    fi

    #======= Transfer image files =======

    if [ ${#NB_DEBUG} = 0 ]; then
        scp -i ${NB_KEY_FILE} ${NB_OUTPUT_IMG} ${NB_REMOTE_USER}@${NB_REMOTE_HOST}:${NB_REMOTE_IMAGE_PATH}/waiting/${IMAGE_FILE}
        scp -i ${NB_KEY_FILE} ${NB_OUTPUT_IMG} ${NB_REMOTE_USER}@${NB_REMOTE_HOST}:${NB_REMOTE_IMAGE_PATH}/
    else
        scp ${NB_OUTPUT_IMG} ${NB_DEBUG_USER}@${NB_DEBUG_HOST}:${NB_DEBUG_IMAGE_PATH}/waiting/${IMAGE_FILE}
        scp ${NB_OUTPUT_IMG} ${NB_DEBUG_USER}@${NB_DEBUG_HOST}:${NB_DEBUG_IMAGE_PATH}/
    fi

    if [ ${MODE} -ne "0" ]; then
        echo
        break
    fi

    sleep ${NB_WAITING_TIME}

done


#======= Remove pid file =======

rm ${PIDFILE}
