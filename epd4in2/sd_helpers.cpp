
#include <SPI.h>
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "sd_helpers.h"

// Not using HSPI bc for some reason it kept boot cycling.
SPIClass sdSpi;

void initSD () {
  Serial.println("Intializing micro-SD module");
  // Initialize SPI for the SD card with custom pins
  sdSpi.begin(SD_SPI_SCK, SD_SPI_MISO, SD_SPI_MOSI, SD_SPI_CS);
  if(!SD.begin(SD_SPI_CS, sdSpi)){
    Serial.println("Card Mount Failed");
    return;
  }
  Serial.println("Successfully initialized micro-SD module");
}

int countFilesInDir(const char* dirPath) {
    File root = SD.open(dirPath);
    if (!root || !root.isDirectory()) {
        return 0;
    }
    int fileCount = 0;
    while (true) {
        File entry = root.openNextFile();
        // No more files
        if (!entry) {
            break;
        }
        if (!entry.isDirectory()) {
            fileCount++;
        }
        entry.close();
    }
    root.close();
    return fileCount;
}


ImageBuffer loadImage(const char* dirPath, const int imageIndex) {
  ImageBuffer buffer;
  buffer.size = 0;

  File root = SD.open(dirPath);
  if(!root){
    Serial.println("Failed to open directory");
    return buffer;
  }
  if(!root.isDirectory()){
    Serial.println("Path is not a directory");
    return buffer;
  }
  int skippedFiles = 0;
  File file = root.openNextFile();
  while(file){
    // Skip files within the directory
    if (file.isDirectory()) {
      file = root.openNextFile();
      continue;
    }
    Serial.print("  FILE: ");
    Serial.println(file.name());
    if (skippedFiles < imageIndex) {
      skippedFiles += 1;
      file = root.openNextFile();
      continue;
    }

    size_t fileSize = file.size();

    // Allocate onto the heap
    buffer.data = (char *)malloc(fileSize);
    buffer.size = fileSize;
    if (buffer.data == nullptr) {
      Serial.println("Failed to allocate memory!");
      file.close();
      return buffer;
    }

    // Read the file into the buffer
    size_t bytesRead = file.readBytes(buffer.data, buffer.size);
    Serial.println("File contents read successfully!");

    // Close the file
    file.close();

    return buffer;
  }
}
