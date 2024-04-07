
#define ENABLE_GxEPD2_GFX 0
#define ESP32 true

#include <GxEPD2_BW.h>
#include <Fonts/FreeMonoBold9pt7b.h>

// select the display constructor line in one of the following files (old style):
#include "GxEPD2_display_selection.h"

// or select the display class and display driver class in the following file (new style):
#include "GxEPD2_display_selection_new_style.h"

#if !defined(__AVR) && !defined(STM32F1xx)
#include "custom_bitmap.h"
#endif

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
  delay(1000);
  drawBitmaps();
  display.powerOff();
  Serial.println("setup done");
  display.end();
}

void loop()
{
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

void drawBitmaps()
{
  display.setRotation(0);
  display.setFullWindow();
  drawBitmaps400x300();
}

void drawBitmaps400x300()
{
  display.firstPage();
  do
  {
    display.fillScreen(GxEPD_WHITE);
    display.drawInvertedBitmap(0, 0, Bitmap400x300_1, 400, 300, GxEPD_BLACK);
  } while (display.nextPage());
  delay(2000);
}
