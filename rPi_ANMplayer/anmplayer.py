from datetime import datetime
import board
import neopixel


##############################################
# This program makes a lot of assumptions 
# about the format of the animation file:
#  - It's a .txt file
#  - Each line (broken by /LF) is a full
#    frame AND lines up with the pixel count
#  - Each byte value is stored directly with
#    no delimeters
##############################################


##############################################
# GLOBAL SETTINGS
##############################################
NEO_NUM_PIXELS =    28*28
NEO_LENGTH =            3    # 3 for RGB (etc.), 4 for RGBW (etc.)
ANIM_FILE = "circle.anm"
ANIM_DELIM_COUNT =      0    # 2 for CR+LF, 1 for CR/LF
maxBrightness =       0.2
frameHoldTime =     20000   # micro seconds 20,000 = 50Hz


##############################################
# INTERNAL VARIABLES AND STRUCTURES
##############################################
pixels = neopixel.NeoPixel(board.D18, NEO_NUM_PIXELS, brightness=maxBrightness, auto_write=False, pixel_order=neopixel.GRB)
colourArray = [0] * NEO_LENGTH


##############################################
# SETUP
##############################################
f = open(ANIM_FILE, "rb")
f.seek(0)

frameStartTime = 0
maxNow = 998369


##############################################
# LOOP
##############################################
while True:
  now = datetime.now().microsecond
  
  if now > maxNow:
    maxNow = now
  
  delta = now - frameStartTime
  if (now < frameStartTime):
    delta = (maxNow-frameStartTime) + now
  
  if delta >= frameHoldTime:
    frameStartTime = now
    #pixels.clear()
    
    for i in range(0, NEO_NUM_PIXELS):
      
      for j in range(0, NEO_LENGTH):
        data = f.read(1)
        if not data:
          f.seek(0)
          data = f.read(1)
          print("RELOAD")
          if not data:
            print("ERROR")
        #print(data)
        colourArray[j] = int.from_bytes(data, byteorder='big')
      
      #print(str(colourArray[0]) + "\t" + str(colourArray[1]) + "\t" + str(colourArray[2]))
      
      if NEO_LENGTH > 3:
        pixels[i] = (colourArray[0], colourArray[1], colourArray[2], colourArray[3])
      else:
        pixels[i] = (colourArray[0], colourArray[1], colourArray[2])
        
    pixels.show()
    
    # Waste the delimeter
    if ANIM_DELIM_COUNT > 0:
      for d in range(0, ANIM_DELIM_COUNT):
        try:
          f.read(1)
        except:
          f.seek(0)

f.close()