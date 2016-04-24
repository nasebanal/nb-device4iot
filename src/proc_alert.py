# coding: utf-8

"""
A program to capture alert information

Copyright (C) 2016 NASEBANAL - All Rights Reserved
"""

__author__ = "Shunjiro Yatsuzuka"
__copyright__ = "Copyright (c) 2016 NASEBANAL"
__date__ = "April.24, 2016"
__version__ = "1.0"


#======= Import Modules =======

#----- General -----

import os
import time
import pprint
import requests


#----- RPIO Library -----

import RPi.GPIO as GPIO


#----- NASEBANAL -----

from common import Log


#======= ProcAlert Class =======

class ProcAlert():

    """
    Class to process alert
    """


    #======= alert_led =======

    def alert_led(self):

        """
        Function to light LED
        """

        #======= Start Message =======

        self.log.output_msg(1, 1, "ProcAlert.alert_led() started")


        #======= Switch LED =======

        if self.alert_flag == 1:

            GPIO.output(self.led_pos, GPIO.HIGH)

        else:
            
            GPIO.output(self.led_pos, GPIO.LOW)


        #======= End Message =======

        self.log.output_msg(1, 1, "ProcAlert.alert_led() ended")


    #======= Get Alert =======

    def get_alert(self):

        """
        Function to capture alert
        """

        #======= Start Message =======

        self.log.output_msg(1, 1, "ProcAlert.get_alert() started")


        #======= Get Alert =======

        response = requests.get( self.endpoint )
        self.alert_flag = response.json()[0]['alert_flag']

        self.log.output_msg(1, 1, "self.alert_flag = {0}".format(self.alert_flag))


        #======= End Message =======

        self.log.output_msg(1, 1, "ProcAlert.get_alert() ended")


    #======= Initialization =======

    def __init__(self):

        """
        Constructor
        """

        #======= Setup Log =======

        self.log = Log(os.environ.has_key('NB_LOG_LEVEL'))


        #======= Start Message =======

        self.log.output_msg(1, 1, "ProcAlert.__init__() started")


        #======= Setup ProcMode =======

        if os.environ.has_key('NB_PROCMODE'):
            self.procmode = int(os.environ['NB_PROCMODE'])
        else:
            self.procmode = 1

        self.log.output_msg(1, 1, "self.procmode = {0}".format(self.procmode))


        #======= Setup Waiting Time =======

        if os.environ.has_key('NB_WAITING_TIME'):
            self.waiting_time = int(os.environ['NB_WAITING_TIME'])
        else:
            self.waiting_time = 1

        self.log.output_msg(1, 1, "self.waiting_time = {0}".format(self.waiting_time))


        #======= Setup LED Position =======

        if os.environ.has_key('NB_LED_POS'):
            self.led_pos = int(os.environ['NB_LED_POS'])
        else:
            self.led_pos = 11

        self.log.output_msg(1, 1, "self.led_pos = {0}".format(self.led_pos))


        #======= Setup GPIO =======

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.led_pos, GPIO.OUT, initial=GPIO.LOW)


        #======= Setup Endpoint =======

        if os.environ.has_key('NB_ENDPOINT'):
            self.endpoint = os.environ['NB_ENDPOINT']
        else:
            self.endpoint = "http://192.168.1.1:3000/alert/index.json"

        self.log.output_msg(1, 1, "self.endpoint = {0}".format(self.endpoint))


        #======= End Message =======

        self.log.output_msg(1, 1, "ProcImage.__init__() ended")

