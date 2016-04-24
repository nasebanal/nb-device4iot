# coding: utf-8

"""
A program to get alert information

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

#----- NASEBANAL -----

from common import Log
from proc_alert import ProcAlert


#======= Global Variable =======

log = Log(os.environ.has_key('NB_LOG_LEVEL'))


#======= Main Function =======

if __name__ == '__main__':


    #======= Start Message =======

    log.output_msg(1, 1, "main() started")
    log.output_msg(1, 1, "log.log_level = {0}".format(log.log_level))


    #======= Start Process =======

    app = ProcAlert()

    while 1:
        app.get_alert()
        app.alert_led()

        time.sleep(5)


    #======= End Message =======

    log.output_msg(1, 1, "main() ended")

