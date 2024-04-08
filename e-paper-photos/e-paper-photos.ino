
#include <HardwareSerial.h>
#define ENABLE_GxEPD2_GFX 0
#define ESP32 true

#include <GxEPD2_BW.h>

// select the display constructor line in one of the following files (old style):
#include "GxEPD2_display_selection.h"

// or select the display class and display driver class in the following file (new style):
// #include "GxEPD2_display_selection_new_style.h"

#if !defined(__AVR) && !defined(STM32F1xx)
#include "custom_bitmaps.h"
#endif

const unsigned photo_change_delay = 30 * 1000;

void setup()
{
  Serial.begin(115200);
  Serial.println();
  Serial.println("setup");
  delay(100);
  // USE THIS for Waveshare boards with "clever" reset circuit, 2ms reset pulse
  display.init(115200, true, 2, false);
  // first update should be full refresh
  clearScreen();
  display.setRotation(0);
  display.setFullWindow();
}

void loop()
{
  drawBitmaps400x300();
}

/**
 * Sets the display to full white to clear the screen
 * in preparation for a new screen to be drawn.
 */
void clearScreen()
{
  display.setFullWindow();
  display.firstPage();
  do
  {
    display.fillScreen(GxEPD_WHITE);
  } while (display.nextPage());
}

void drawBitmaps400x300()
{
  for (int i = 0; i < sizeof(bitmaps); i++)
  {
    display.firstPage();
    do
    {
      display.fillScreen(GxEPD_WHITE);
      display.drawInvertedBitmap(0, 0, bitmaps[i], 400, 300, GxEPD_BLACK);
    } while (display.nextPage());
    display.powerOff();
    delay(photo_change_delay);
  }
}
