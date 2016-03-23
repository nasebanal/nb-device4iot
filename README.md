# NASEBANAL Device for IoT

This is an open source project for the IoT software.
Images captured by PiCamera is transfered to Cloud Server and they are displayed from NASEBANAL Platform for IoT.
You can see the demo from https://www.youtube.com/watch?v=p_HXt_Oj4GI


[Prerequisite]

* Setup Raspberry Pi and PiCamera
* Setup NASEBANAL Platform for IoT
* Setup the connection between Raspberry Pi and Cloud Server.


[How To Use]

Step.1) Get source code.

 $ git clone https://github.com/nasebanal/nb-platform4iot.git

Step.2) Setup necessary environment variable in .bashrc.

Step.3) Execute the command to get images and transfer them to cloud server.

 $ cd nb-platform4iot/bin/
 $ get_image.py

Then you can captured images from NASEBANAL Platform for IoT web site.
