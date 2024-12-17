/**
 *  @filename   :   epd4in2-demo.ino
 *  @brief      :   4.2inch e-paper display demo
 *  @author     :   Yehui from Waveshare
 *
 *  Copyright (C) Waveshare     August 4 2017
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documnetation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to  whom the Software is
 * furished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include <EEPROM.h>
#include <SPI.h>
#include "epd4in2.h"
#include "sd_helpers.h"

#define COLORED 0
#define UNCOLORED 1
// The address in Flash Memory storing the progress through the list
#define IMAGE_INDEX_ADDRESS 0
// define the number of bytes (max 512) you want to access
#define EEPROM_SIZE 1

#define uS_TO_S_FACTOR 1000000 /* Conversion factor for micro seconds to seconds */
#define TIME_TO_SLEEP 15     /* Time ESP32 will go to sleep (in seconds) */

Epd epd;

void setup()
{
  Serial.begin(115200);
  initSD();

  
  // Schedules a time to automatically wake up from deep sleep
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);

  // // Turn off the Red LED. Turns on the Blue LED to indicate it is awake and working
  gpio_set_direction(GPIO_NUM_2, GPIO_MODE_OUTPUT);
  gpio_set_level(GPIO_NUM_2, 1);
  gpio_set_level(GPIO_NUM_13, 0);

  // Initialize the E Paper Display
  epd.Init_4Gray();
  epd.ClearFrame();

  // Incrememnt Index by one, looping back around if necessary
  const int numImages = countFilesInDir("/bitmaps");
  EEPROM.begin(EEPROM_SIZE);
  const int i = (EEPROM.read(IMAGE_INDEX_ADDRESS) + 1) % numImages;
  EEPROM.write(IMAGE_INDEX_ADDRESS, i);
  EEPROM.commit();

  const ImageBuffer imageBuffer = loadImage("/bitmaps", i);
  
  // Show the image of the appropriate index
  epd.Set_4GrayDisplay((const unsigned char *)imageBuffer.data, 0, 0, 400, 300);
  gpio_set_level(GPIO_NUM_2, 0);

  // Sleep. When it wakes, it will re-run setup
  esp_deep_sleep_start();
}

void loop() {
  for (int i = 0; i < sizeof(bitmaps); i++)
  {
    epd.Set_4GrayDisplay(bitmaps[i], 0, 0,  400,300);
    delay(30000);
  }
}

