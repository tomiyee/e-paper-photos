#ifndef SD_HELPERS_H
#define SD_HELPERS_H

// SD Card SPI pins
#define SD_SPI_SCK  33
#define SD_SPI_MISO 32
#define SD_SPI_MOSI 25
#define SD_SPI_CS   26

extern SPIClass sdSpi; // Create an SPI instance for SD SPI

struct ImageBuffer {
    char* data;      // Pointer to the allocated memory
    size_t size;     // Size of the allocated memory
};

/** Initializes the SD card interface */
void initSD ();

/** Counts the number of files in the given directory */
int countFilesInDir(const char* dirPath);

/** 
 * Loads the image with the given 0-index value.
 *
 * @note If the image failed to load (such aas failing to find 
 * the directory or if there are fewer images in the dir 
 * than the given index), an ImageBuffer with size = 0 
 * will be returned. 
 */
ImageBuffer loadImage(const char* dirPath, const int imageIndex);

#endif