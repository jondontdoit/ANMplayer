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

### rPi_MediaPlayers
* While I was at it, I made a couple Python scripts to directly render image and video files to play on a NeoPixel grid
* These scripts don't use ANM files or make use of Processing

#### Neo Movie Player
* Took a few iterations but the final process is to run "sudo python3 neomovie.py"
    * Use -r and specify a filename to render a movie file and start playing it
    * Use -p and specify a folder name in the renders folder to play that movie
    * Use neither r or p to play random files
  
#### Neo Image Player
* Took a few iterations but the final process is to run "sudo python3 neoimage.py"
    * Use -p and specify a file name to display
    * Use no p argument to play images randomly in the images folder
