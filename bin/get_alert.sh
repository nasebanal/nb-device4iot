#!/bin/bash

#========================================================================
# FILE NAME:    get_alert.sh
# FUNCTION:     Get alert flag from remote server
# VERSION:      1.0
# AUTHOR:       S.Yatsuzuka
# 
# Copyright (C) 2016 NASEBANAL
#========================================================================


#======= Check Arguments =======

if [ $# -gt 1 ]; then

    echo
    echo "Usage: $0"
    echo
    echo "  [Output File]"
    echo "      log file name (optional)"
    echo
        exit 1
fi


#======= Get Arguments =======

if [ $# -eq 1 ]; then

    export OUTPUT_FILE=$1
    echo "OUTPUT_FILE   = ${OUTPUT_FILE}"

fi


#======= Check NB Home =======

if [ ${#NB_HOME} = 0 ]; then

    echo
    echo "ERROR: NB_HOME isn't set as environment variable"
    echo
    exit 1
fi


#=======

if [ ${#NB_DEBUG} = 1 ]; then

    export NB_ENDPOINT="http://${NB_REMOTE_HOST}:3000/alert/index.json"

else

    export NB_ENDPOINT="http://${NB_DEBUG_HOST}:3000/alert/index.json"
fi


#======= Get Parameter =======

source ${NB_HOME}/param/get_alert.param
echo "CMD   = ${NB_CMD}"


#======= Call Program =======

if [ $# -eq 0 ]; then

    ${NB_CMD}

elif [ $# -eq 1 ]; then

    ${NB_CMD} > ${OUTPUT_FILE}

fi
