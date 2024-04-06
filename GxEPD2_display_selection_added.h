// Display Library example for SPI e-paper panels from Dalian Good Display and boards from Waveshare.
// Requires HW SPI and Adafruit_GFX. Caution: the e-paper panels require 3.3V supply AND data lines!
//
// Display Library based on Demo Example from Good Display: https://www.good-display.com/companyfile/32/
//
// Author: Jean-Marc Zingg
//
// Version: see library.properties
//
// Library: https://github.com/ZinggJM/GxEPD2

#ifndef _GxEPD2_boards_added_H_
#define _GxEPD2_boards_added_H_

// Arduino DUE

// mapping suggestion for Arduino DUE, note: pin 77 is on board pin 10, SS is 10
// BUSY -> 7, RST -> 9, DC -> 8, CS-> 10, CLK -> 76, DIN -> 75
// SPI pins are on 6 pin 2x3 SPI header, no SS on SPI header!

#if defined(ARDUINO_ARCH_SAM)
#define MAX_DISPLAY_BUFFER_SIZE 32768ul // e.g., up to 96k
#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8) ? EPD::HEIGHT : MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8))
// select one and adapt to your mapping
#define MAX_HEIGHT_3C(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8))
#define MAX_HEIGHT_7C(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2)) // 2 pixel per byte
#undef MAX_DISPLAY_BUFFER_SIZE
#undef MAX_HEIGHT
#undef MAX_HEIGHT_3C
#undef MAX_HEIGHT_7C
#endif

#if defined(ARDUINO_ARCH_SAMD)
#define MAX_DISPLAY_BUFFER_SIZE 15000ul // ~15k is a good compromise
#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8) ? EPD::HEIGHT : MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8))

#define MAX_HEIGHT_3C(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8))

#define MAX_HEIGHT_7C(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2)) // 2 pixel per byte

#undef MAX_DISPLAY_BUFFER_SIZE
#undef MAX_HEIGHT
#undef MAX_HEIGHT_3C
#undef MAX_HEIGHT_7C
#endif

// mapping suggestion for ESP32, e.g. LOLIN32 D32 PRO
// BUSY -> 15, RST -> 2, DC -> 0, CS -> 5, CLK -> SCK(18), DIN -> MOSI(23), GND -> GND, 3.3V -> 3.3V
// note: use explicit value for CS, as SS is re-defined to TF_CS(4) in pins_arduino.h for Board: "LOLIN D32 PRO"

#if defined(ESP32) && defined(ARDUINO_LOLIN_D32_PRO)
#endif

// mapping suggestion for ESP32, e.g. TTGO T8 ESP32-WROVER
// BUSY -> 4, RST -> 0, DC -> 2, CS -> SS(5), CLK -> SCK(18), DIN -> MOSI(23), GND -> GND, 3.3V -> 3.3V
// for use with Board: "ESP32 Dev Module":

#if defined(ESP32) && defined(ARDUINO_ESP32_DEV)
#endif

// mapping of Waveshare e-Paper ESP8266 Driver Board, old version
// BUSY -> GPIO16, RST -> GPIO5, DC -> GPIO4, CS -> GPIO15, CLK -> GPIO14, DIN -> GPIO13, GND -> GND, 3.3V -> 3.3V
// NOTE for ESP8266: using SS (GPIO15) for CS may cause boot mode problems, add a 3.3k pull-down in case
//      the e-Paper ESP8266 Driver Board should have no boot mode issue, as it doesn't use level converters

#if defined(ESP8266)
#endif

#if defined(ARDUINO_ARCH_RP2040)
#define MAX_DISPLAY_BUFFER_SIZE 131072ul // e.g. half of available ram
#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8) ? EPD::HEIGHT : MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8))
#define MAX_HEIGHT_3C(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8))
#define MAX_HEIGHT_7C(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2)) // 2 pixel per byte
#undef MAX_DISPLAY_BUFFER_SIZE
#undef MAX_HEIGHT
#undef MAX_HEIGHT_3C
#undef MAX_HEIGHT_7C
#endif

#endif
