# TeensyVGA
TeensyVGA is written on top of the [VGA_t4 library by by J-M Harvengt](https://github.com/Jean-MarcHarvengt/VGA_t4 "VGA_t4 library by by J-M Harvengt"). It currently allows the next frame to be cached in the RAM on the Teensy4.0 and also has support for pixel data images. (Included script allows conversion from .jpg/.png to the pixeldata in PROGMEM). Due to needing to store multiple frames there is only 3 bit color.
## Pinout
- Teensy4.0 D2  -> 470OHM -> VGA Pin 2 (GREEN PIN)
- Teensy4.0 D4  -> 470OHM -> VGA Pin 1 (RED PIN)
- Teensy4.0 D10 -> 470OHM -> VGA Pin 10 (BLUE PIN)
- Teensy4.0 D8 -> 82OHM -> VGA Pin 14 (VSYNC)
- Teensy4.0 D15 -> 82OHM -> VGA Pin 13 (HSYNC)

## Instructions
Default the code is set to bitmap mode. The PROGMEM bitmap is loaded into RAM. On request the other PROGMEM bitmap is loaded into RAM. The sample code shows a GIF of Ben Shapiro.
To change the image(s):
- Change image_original.jpg to your desired image
- On windows cd to project directory and py -3 colormap.py
- Copy the contents of the bitmap text file and paste them into desired PROGMEM in the .ino arduino/teensy file