#ifndef SD_HELPERS_H
#define SD_HELPERS_H

// SD Card
#define SD_SPI_SCK  33   // SD SPI Clock
#define SD_SPI_MISO 32   // SD SPI MISO
#define SD_SPI_MOSI 25   // SD SPI MOSI
#define SD_SPI_CS   26   // SD SPI Chip Select

extern SPIClass sdSpi; // Create an SPI instance for SD SPI

struct ImageBuffer {
    char* data;      // Pointer to the allocated memory
    size_t size;     // Size of the allocated memory
};

/** Initializes the SD card interface */
void initSD ();

/** Counts the number of files in the given directory */
int countFilesInDir(const char* dirPath);

/** Loads the image with the given 0-index value */
ImageBuffer loadImage(const char* dirPath, const int imageIndex);

#endif // SD_HELPERS_H