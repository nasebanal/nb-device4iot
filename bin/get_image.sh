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
    if [ $# = 0 ]; then

        ${NB_CMD}

    elif [ $# = 1 ]; then

        ${NB_CMD} > ${OUTPUT_FILE}
    fi

    #======= Transfer image files =======

    scp -i ${NB_KEY_FILE} ${NB_OUTPUT_IMG} ${NB_REMOTE_USER}@${NB_REMOTE_HOST}:${NB_REMOTE_IMAGE_PATH}

done
