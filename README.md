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

PARAMETER|DESCRIPTION|EXAMPLE
---------|-----------|-------
NB_HOME|Root directory of nb-device4iot|${HOME}/nb-device4iot
OPENCV_HOME|Root directory for OpenCV|${HOME}/vendor/opencv
NB_KEY_FILE|public key file for AWS|${HOME}/.ssh/xxx.pem
NB_REMOTE_USER|user id for AWS|ec2-user
NB_REMOTE_HOST|IP Address for AWS|xxx.xxx.xxx.xxx
NB_REMOTE_IMAGE_PATH|Directory path for image storage|/home/ec2-user/nb-platform4iot/app/assets/images/
NB_DEBUG_USER|user id for development environment|syatsuzuka
NB_DEBUG_HOST|IP Address for development environment|192.168.1.1
NB_DEBUG_IMAGE_PATH|Directory path for image storage|/home/syatsuzuka/nb-platform4iot/app/assets/images/
NB_DEBUG|Debug flag|1

Step.3) Execute the command to get images and transfer them to cloud server.

 $ cd nb-platform4iot/bin/
 $ get_image.py

Then you can captured images from NASEBANAL Platform for IoT web site.
