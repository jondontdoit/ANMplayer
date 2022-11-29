
static int xSize = 28;
static int ySize = 28;

static int pixelSize = 10;

static long frameHoldTime = 100;
long frameStartTime = 0;

void setup() {
  size(280, 280);
  background(0);
  stroke(0,0);  
}

void draw() {
  byte f[] = loadBytes("circle.anm");
  int fileLength = f.length;
  println(fileLength);
  int i = 0;
  
  while (i < fileLength) {
    
    if (millis() - frameStartTime > frameHoldTime) {
      
      frameStartTime = millis();
      
      for (int x=0; x<xSize; x++) {
        for (int y=0; y<ySize; y++) {
          
          //print(i);
          //print("/");
          //println(fileLength);
          
          int r = f[i] & 0xff;
          i++; if (i > fileLength) i=0;
          int g = f[i] & 0xff;
          i++; if (i > fileLength) i=0;
          int b = f[i] & 0xff;
          i++; if (i > fileLength) i=0;
          
          //print(r);
          //print("\t");
          //print(g);
          //print("\t");
          //print(b);
          //println();
          
          colorMode(RGB, 255.0);
          color c = color(r,g,b);
        
          fill(c);
          rect(x*pixelSize, y*pixelSize, pixelSize, pixelSize);
          
          //print(red(c));
          //print("\t");
          //print(green(c));
          //print("\t");
          //print(blue(c));
          //println();
        }
      }
    }
  }
}
