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
import sys
import time
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

COLOR = {}
COLOR[0] = (255, 255, 255)
COLOR[1] = (255, 0, 0)
COLOR[2] = (0, 255, 0)
COLOR[3] = (0, 0, 255)
COLOR[4] = (100, 100, 100)


#======= ProcImage Class =======

class ProcImage():

    """
    Class to process images
    """


    #======= Process Image =======

    def proc_image(self):

        """
        Function to process image
        """

        #----- No Processing -----

        if self.procmode == 0:

            self.img_output = self.img_input


        #----- Flip Flop -----

        elif self.procmode == 1:

            self.img_output = cv2.flip(self.img_input, flipCode = 0)


        #----- Canny -----

        elif self.procmode == 2:

            self.img_output = cv2.Canny(self.img_input, 50, 150)


        #----- Face Recognition -----

        elif self.procmode == 3:


            #----- Copy Mat -----

            self.img_output = self.img_input.copy()


            #----- Get Face Object -----

            faces = self.cascade_face.detectMultiScale(
                self.img_output,
                scaleFactor=1.1,
                minNeighbors=3,
                flags=cv2.CASCADE_SCALE_IMAGE,
                minSize=(0,0)
            )

        #----- Depict Face region -----

        for x, y, w, h in faces:

            #----- Depict rectangle for each face -----

            cv2.rectangle(
                self.img_output,
                (x-self.face_margin_x, y-self.face_margin_y),
                (x+w+self.face_margin_x, y+h+self.face_margin_y),
                COLOR[2],
                self.rect_width
            )


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


            #----- Read HAAR files -----

            if self.procmode == 3:

                self.cascade_face = cv2.CascadeClassifier(self.cascade_face)

                if self.cascade_face.empty():
                    self.log.output_msg(1, 1, "Couldn\'t read HAAR file for face recognition")
                    sys.exit()


            #----- Test Image -----

            '''
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


                #======= Image Processing =======

                self.proc_image()


                #======= Display Image =======

                cv2.imwrite(self.output_img, self.img_output)

                cv2.imshow('input', self.img_input)
                cv2.imshow('output', self.img_output)

                cv2.waitKey(1000)

            cv2.destroyAllWindows()


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


        #======= Setup ProcMode =======

        if os.environ.has_key('NB_PROCMODE'):
            self.procmode = int(os.environ['NB_PROCMODE'])
        else:
            self.procmode = 32

        self.log.output_msg(1, 1, "self.procmode = {0}".format(self.procmode))



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


        #======= Setup Cascade File (Face) =======

        if os.environ.has_key('NB_CASCADE_FACE'):
            self.cascade_face = os.environ['NB_CASCADE_FACE']
        else:
            self.cascade_face = os.environ['OPENCV_HOME'] + "/data/haarcascades/haarcascade_frontalface_default.xml"

        self.log.output_msg(1, 1, "self.cascade_face = {0}".format(self.cascade_face))


        #======= Setup Face Margin X =======

        if os.environ.has_key('NB_FACE_MARGIN_X'):
            self.face_margin_x = int(os.environ['NB_FACE_MARGIN_X'])
        else:
            self.face_margin_x = 15

        self.log.output_msg(1, 1, "self.face_margin_x = {0}".format(self.face_margin_x))


        #======= Setup Face Margin Y =======

        if os.environ.has_key('NB_FACE_MARGIN_Y'):
            self.face_margin_y = int(os.environ['NB_FACE_MARGIN_Y'])
        else:
            self.face_margin_y = 30

        self.log.output_msg(1, 1, "self.face_margin_y = {0}".format(self.face_margin_y))


        #======= Setup Rectangle Width =======

        if os.environ.has_key('NB_RECT_WIDTH'):
            self.rect_width = int(os.environ['NB_RECT_WIDTH'])
        else:
            self.rect_width = 4

        self.log.output_msg(1, 1, "self.rect_width = {0}".format(self.rect_width))


        #======= End Message =======

        self.log.output_msg(1, 1, "ProcImage.__init__() ended")

