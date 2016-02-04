# coding: utf-8

"""
A program for common function

Copyright (C) 2016 NASEBANAL - All Rights Reserved
"""

__author__ = "Shunjiro Yatsuzuka"
__copyright__ = "Copyright (c) 2016 NASEBANAL"
__date__ = "Feb.3, 2016"
__version__ = "1.0"


#======= Import Modules =======

import sys
import datetime


#======= Log Class =======

class Log():

    """
    Class to get static images
    """

    #======= Message Function =======

    def output_msg(self, type, log_level, msg):

        """
        Function to output message

        type
            1: INFO
            2: WARN
            3: ERROR
        """

        #======= Set Message =======

        if type == 0:
            pass
        elif type == 1:
            msg_type = "INFO"
        elif type == 2:
            msg_type = "WARN"
        elif type_type == 3:
            msg_type = "ERROR"

        curr_time = datetime.datetime.now()
        msg_line = "{0:%Y-%m-%d %H:%M:%S} {1}:\t{2}".format(curr_time, msg_type, msg)


        #======= Output Message =======

        if self.log_level >= log_level:

            if type == 0:
                print (msg_line)
            else:
                print >> sys.stderr, msg_line


    #======= Initialization =======

    def __init__(self, log_level):

        """
        Constructor of Log class
        """

        #======= Set Variable =======

        if log_level:
            self.log_level = int(log_level)
        else:
            self.log_level = 10


        #======= End Message =======

        self.output_msg(1, 1, "Log.log_level = {0}".format(self.log_level))
