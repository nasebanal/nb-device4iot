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

if [ $# -gt 1 ]; then

    echo
    echo "Usage: $0 [Output File]"
    echo
        exit 1
fi


#======= Get Arguments =======

if [ $# = 1 ]; then

    OUTPUT_FILE=$1
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

source ${NB_HOME}/param/get_image.param
echo "CMD   = ${NB_CMD}"


#======= Get Work Orders =======


#======= Call Program =======

while [ 1 ]
do

    DATE=`date +%Y%m%d%H%M%S`
    IMAGE_FILE=img_${DATE}.jpg
    echo "IMAGE_FILE    = ${IMAGE_FILE}"

    if [ $# = 0 ]; then

        ${NB_CMD}

    elif [ $# = 1 ]; then

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

    sleep ${NB_WAITING_TIME}

done
