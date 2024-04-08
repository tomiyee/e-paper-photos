from PIL import Image
import numpy as np

def load_png_image(filename):
  im_frame = Image.open(filename)
  np_frame = np.array(im_frame.getdata())
  return np_frame

def image_to_bitmap(image):
  # group the image into 8 columns of 0s and 1s
  # Any pixel with a value less than 254 is considered 0
  image = image.reshape(-1, 8)//255
  # convert each row to a string of eight 0s and 1s
  image = np.array([''.join(row) for row in image.astype(str)])
  # read each binary string as a binary number (0 to 15)
  image = np.array([int(row, 2) for row in image])
  # convert the binary number into a hex number
  image = np.array([hex(row) for row in image])
  return image

def bitmap_to_c_array(bitmap):
  # separate the bitmap into columns of 10 and join as a grid
  bitmap = bitmap.reshape(-1, 20)
  # convert each row to a string
  bitmap = np.array([','.join(row) for row in bitmap.astype(str)])
  return "#define _GxBitmaps400x300_H_\n\n#include <pgmspace.h>\n\nconst unsigned char bitmap[] PROGMEM = {\n" +  ",\n".join(bitmap) + "};"

if __name__ == "__main__":
  image = load_png_image("image.png")
  bitmap = image_to_bitmap(image)
  file_contents = bitmap_to_c_array(bitmap)
  # write to file
  with open("bitmap.h", "w") as file:
    file.write(file_contents)
    