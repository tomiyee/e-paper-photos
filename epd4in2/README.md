# Description

This directory is an Arduino project built from the Waveshare provided [code for ESP32](https://github.com/waveshareteam/e-Paper/tree/master/Arduino/epd4in2_V2).

## SD Helpers

Assumes that `.bin` files are uploaded into the `/bitmaps` directory of the SD card.

By default, I've defined the SPI pins for the SD card reader to be: 

|SD Reader | ESP32 GPIO Pin|
|----------|---------------|
| CLOCK    | 33            | 
| MISO     | 32            |
| MOSI     | 25            |
| CS       | 26            |

If you want to change the ESP32 pins, change the lines in `sd_helpers.h`.

## E-Paper Display

by default, I've defined the following pins for the Wavesgare E-Paper Module:

| E-Paper Module | ESP32 GPIO Pin |
|----------------|----------------|
| BUSY           | 4              |
| RST            | 16             |
| DC             | 17             |
| CS             | 5              |
| CLOCK          | 18             |
| DIN            | 23             |
