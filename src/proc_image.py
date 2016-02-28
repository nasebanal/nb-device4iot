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
import time
#import math

#----- Open CV -----

#import cv2
#import numpy as np

#----- Pi Camera -----

import picamera
#from picamera import PiCamera
#import picamera.array
#from picamera.array import PiRGBArray

#----- NASEBANAL -----

from common import Log


#======= ProcImage Class =======

class ProcImage():

    """
    Class to process images
    """

    #======= Get Movies =======

    def get_movie(self):

        """
        Function to get video
        """

        #======= Start Message =======

        self.log.output_msg(1, 1, "ProcImage.get_movie() started")


        #======= Open Camera =======

        with picamera.PiCamera() as camera:


            #======= Open Window =======

            cv2.namedWindow('input')
            cv2.namedWindow('output')


            #======= Prepare Video Recorder =======

            video = cv2.VideoWriter(
                self.output_video,
                cv2.VideoWriter_fourcc('H','2','6','4'),
                30,
                camera.resolution,
                self.isColor
            )


            #======= Capture Movie =======

            with picamera.array.PiRGBArray(camera) as stream:

                #======= Prepare Stream =======

                time.sleep(0.1)

                #======= Get Frame Info =======

                camera.capture(stream, format='bgr')
                self.img_input = stream.array
                
                self.input_height, self.input_width, self.input_channels = self.img_input.shape

                #======= Read Stream =======

                for frame in camera.capture_continuous(
                    stream,
                    format='bgr',
                    use_video_port=True
                ):

                    #======= Read Image =======

                    self.img_input = frame.array


                    #======= Write File =======

                    video.write(self.img_input)


    #======= Get Image =======

    def get_image(self):

        """
        Function to capture image
        """

        #======= Start Message =======
        self.log.output_msg(1, 1, "ProcImage.get_image() started")


        #======= Open Camera =======

        with picamera.PiCamera() as camera:


            #======= Setup Camera Configuration =======

            #----- Setup Resolution -----

            if self.resolution == 3:
                camera.resolution = (1024, 768)

            elif self.resolution == 2:
                camera.resolution = (640, 480)

            else:
                camera.resolution = (320, 240)

            #----- Setup Framerate -----

            camera.framerate = self.framerate


            camera.start_preview()
            time.sleep(self.standby_time)
            camera.stop_preview()

            camera.capture(self.output_img)


            '''
            #======= Open WIndow =======

            cv2.namedWindow('input')
            cv2.namedWindow('output')

            #======= Capture Image =======

            with picamera.array.PiRGBArray(camera) as stream:

                #======= Read Stream =======

                camera.capture(stream, format='bgr')
                self.img_input = stream.array

                #======= Display Image =======

                cv2.imshow('input', self.img_input)

                cv2.waitKey(1000)

            cv2.destroyAllWindows()
            '''


        #======= End Message =======

        self.log.output_msg(1, 1, "ProcImage.get_image() ended")


    #======= Initialization =======

    def __init__(self):

        """
        Constructor
        """

        #======= Setup Log =======

        self.log = Log(os.environ.has_key('NB_LOG_LEVEL'))


        #======= Start Message =======

        self.log.output_msg(1, 1, "ProcImage.__init__() started")

        #======= Setup Resolution =======

        if os.environ.has_key('NB_RESOLUTION'):
            self.resolution = int(os.environ['NB_RESOLUTION'])
        else:
            self.resolution = 1

        self.log.output_msg(1, 1, "self.resolution = {0}".format(self.resolution))


        #======= Setup Framerate =======

        if os.environ.has_key('NB_FRAMERATE'):
            self.framerate = int(os.environ['NB_FRAMERATE'])
        else:
            self.framerate = 32

        self.log.output_msg(1, 1, "self.framerate = {0}".format(self.framerate))


        #======= Setup Output Image =======

        if os.environ.has_key('NB_OUTPUT_IMG'):
            self.output_img = os.environ['NB_OUTPUT_IMG']
        else:
            self.output_img = 'output'

        self.log.output_msg(1, 1, "self.output_img = {0}".format(self.output_img))

        #======= Setup Standby Time =======

        if os.environ.has_key('NB_STANDBY_TIME'):
            self.standby_time = int(os.environ['NB_STANDBY_TIME'])
        else:
            self.standby_time = 1

        self.log.output_msg(1, 1, "self.standby_time = {0}".format(self.standby_time))


        #======= End Message =======

        self.log.output_msg(1, 1, "ProcImage.__init__() ended")

