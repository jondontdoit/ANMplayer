# ANMplayer
Custom ANM file support for encoding and playing low-res animations from video files

## How to Use
Admittedly this is a proof of concept and therefore in some shambles. You'll need both the Processing.org software and a Raspberry Pi with CircuitPython installed. 

### Processing_VideoToANM
* First update and run the VideoToANM.pde file, which generates an output.txt file
* Next, update and run anmBuilder.py which converts output.txt to a cleaner .anm file
* Move that .anm file over to the Raspberry Pi

### Processing_ANMplayer
* This Processing script just allows you to check the .anm file plays back as expected

### rPi_ANMplayer
* Follow this guide to get started: https://learn.adafruit.com/neopixels-on-raspberry-pi
* Update and run anmplayer.py
