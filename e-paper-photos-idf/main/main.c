#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"

void app_main(void)
{
  printf("Hello, world!\n");
  // Initialize the GPIO Pin as a Pull-Down Resister
  configure_buttons();

  while (1)
  {
    // Read the value of GPIO 5
    int button = gpio_get_level(GPIO_NUM_5);
    printf("Button value: %d\n", button);
    vTaskDelay(200 / portTICK_PERIOD_MS);
  }
}

/**
 * Configures the GPIO 5 as an input pin with a pull-down resistor.
 */
void configure_buttons()
{
  // Creates a GPIO config struct
  gpio_config_t io_conf;
  io_conf.intr_type = GPIO_INTR_DISABLE;
  io_conf.mode = GPIO_MODE_INPUT;
  // 1ULL is a 64 unsigned long long with the first bit set to 1
  io_conf.pin_bit_mask = 1ULL << GPIO_NUM_5;
  io_conf.pull_down_en = 1;
  io_conf.pull_up_en = 0;
  // Passes the GPIO config struct to configure the mode
  gpio_config(&io_conf);
}