# coding: utf-8

"""
A program to capture images

Copyright (C) 2016 NASEBANAL - All Rights Reserved
"""

__author__ = "Shunjiro Yatsuzuka"
__copyright__ = "Copyright (c) 2016 NASEBANAL"
__date__ = "Feb.3, 2016"
__version__ = "1.0"


#======= Import Modules =======

#----- General -----

import os
#import os.path
#import sys
#import time
#import math

#----- Open CV -----

import cv2
import numpy as np

#----- Pi Camera -----

import picamera
from picamera import PiCamera
import picamera.array
from picamera.array import PiRGBArray

#----- NASEBANAL -----

from common import Log


#======= Global Variable =======

log = Log(os.environ.has_key('NB_LOG_LEVEL'))


#======= GetImage Class =======

class GetImage():

    """
    Class to get static images
    """

    #======= Get Image =======

    def get_image(self):

        pass


    #======= Initialization =======

    def __init__(self):

        """
        Constructor
        """

        #======= Start Message =======

        log.output_msg(1, 1, "GetImage.__init__() started")


        #======= Setup Resolution =======

        if os.environ.has_key('NB_RESOLUTION'):
            self.resolution = int(os.environ['NB_RESOLUTION'])
        else:
            self.resolution = 1

        log.output_msg(1, 1, "self.resolution = {0}".format(self.resolution))


        #======= End Message =======

        log.output_msg(1, 1, "GetImage.__init__() ended")


#======= Main Function =======

if __name__ == '__main__':

    #======= Start Message =======

    log.output_msg(1, 1, "get_image.main() started")


    #======= Start Process =======

    app = GetImage()
    app.get_image()

    #======= End Message =======

    log.output_msg(1, 1, "get_image.main() ended")
