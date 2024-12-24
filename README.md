# E-Paper Photo Frame

This repository contains a record of my project building a digital photo frame using a Waveshare E-Paper display and ESP32.

## Software Development

This project was developed on a Windows machine with the Arduino IDE.

### References

The `/e-paper-photos/references` directory contains relevent documentation that I referenced during this project. The README contained within gives a description of each document, and a link to different resources and blogs I referenced.

The Waveshare-provided [documentation](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_Manual#ESP32.2F8266)

### Image Processing

The image processing is done using Python.
1. Navigate to `/e-paper-photos/image_processing`.
2. Create a virtual environment.
3. Install the requirements: `pip install -r requirements`
4. Run `python ./style.py` to automatically apply styles.
5. Read the `README.md` for instructions on where to place images
6. Run `python ./main.py` and follow the instructions for your device. 

### The Arduino Project Files

The code was written to be compatible with the Arduino IDE (not ESP-IDF). 
1. Download the Arduino IDE
2. Open the directory. 
3. Install the ESP32 development libraries.
4. Build and upload the Arduino project to the ESP32.

### The 3D Model Files

I'm very new to 3D modeling, so forgive my bad CAD. The files will be very specific to the particular E-paper display. 

## Hardware Development

Below is a list of the harware involved in creating this project. 

### Electronic Components
- Waveshare 4.2 inch 4-Gray E-Paper Display. [Available here](https://www.waveshare.com/product/displays/e-paper/epaper-2/4.2inch-e-paper-module.htm). 
- ESP-32 Devkit C
- Micro SD Card module
- Micro SD Card
- (Untested) Battery power, either:
  - 18650 Battery and Battery Shield modules, or
  - Thin LiPo battery and a TP...(?) for chargieg it

### Assembly Components
- 3D-Printer and Filanments to build the photo frame
  - Recommend brown/wood-like and a white filament
- Soldering iron and solder, depending on how permanent you want the connections
- A variety of M3 screws



ESP32 and E-Paper Photo Frame

## Project Goal

I wanted to make a gift for my parents and thought that a photo frame that can cycle between many photos would make a great fit.

My background is almost entirely in web-design with only the vaguest experience in ESP32 develoopment, electrical engineering, or 3D modeling and manufacturing practices, so there were a lot of unknowns going into this project. 

### Requirements

Before gettings started, I set some requirements for the project at varying priorities. 

**1. [MVP] It should display the photo when powered off**
- I don't expect my parents to do a good job keeping the device plugged in and wanted to give them the flexibility to use it like a traditional photo frame.
- This led me to using a E-Paper display. They consume very little power and the display can persist effectively indefinitely.

**2. [MVP] It should be easy to load new photos**
- In my limited experience with Arduino IDE and ESP32, I knew that the microcontroller typically has very limited on-board memory.
- I also wanted it to be very easy to revisit after not thinking about this project, since I typically only visit home every 6 months.
- This led me to choose to read images from the SD Card. 

**3. [Not MVP] It should be battery powered**
- Not only did I want my parents to be able to use this device like a traditional photo frame, I also wanted it to still cycle through photos while not being tethered to an outlet. 
- After some research, I settled on one of two combinations:
  - An 18650 rechargable battery and an accompanying battery shield.
  - A thin rectangular LiPo and a module for charging it.
- However, I couldn't get the batteries to cooperate, so I decided to drop this requirement. 
