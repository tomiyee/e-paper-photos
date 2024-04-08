from PIL import Image
import numpy as np

def load_png_image(filename: str) -> np.ndarray:
  im_frame = Image.open(filename)
  np_frame = np.array(im_frame.getdata())
  return np_frame

def image_to_bitmap(image: np.ndarray) -> np.ndarray:
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

def bitmap_to_c_array(bitmap: np.ndarray) -> str:
  # separate the bitmap into columns of 10 and join as a grid
  bitmap = bitmap.reshape(-1, 20)
  # convert each row to a string
  bitmap = np.array([','.join(row) for row in bitmap.astype(str)])
  return "#define _GxBitmaps400x300_H_\n\n#include <pgmspace.h>\n\nconst unsigned char bitmap[] PROGMEM = {\n" +  ",\n".join(bitmap) + "};"

from pillow_heif import register_heif_opener
import glob

# Enables opening HEIF files in default supported by PIL
register_heif_opener()

input_dir = "output_images"

if __name__ == "__main__":
  bitmaps = []
  for filepath in glob.glob(f"{input_dir}/*"):
    # Ignore the README file in the input directory
    if filepath.endswith("README.md"):
      break
    try:
      print(f"Processing: {filepath}")
      bitmap_image = Image.open(filepath).convert('1')
      # group the bitmap every eight bits
      image_data = np.array(bitmap_image.getdata()).reshape(-1, 8) // 255
      # convert each row to a string of eight 0s and 1s
      image = np.array([''.join(row) for row in image_data.astype(str)])
      # read each binary string as a binary number (0 to 15)
      image = np.array([int(row, 2) for row in image])
      # convert the binary number into a hex number
      image = np.array([hex(row) for row in image])
      # For formatting, each row of the image is 30 bytes
      image = image.reshape(-1, 50)
      # convert each row to a string
      bitmap_arr_rows_str = np.array([','.join(row) for row in image.astype(str)])
      # concatenate the rows
      bitmap_arr_str = ",\n".join(bitmap_arr_rows_str)

      bitmap_var = "const unsigned char bitmap_" + str(len(bitmaps)) + "[] PROGMEM = {\n" + bitmap_arr_str + "};\n"
      bitmaps.append(bitmap_var)
    except Exception as e:
      print("Failed to process:", filepath)
      print(e)
      
  
  bitmaps_list = "const uint8 bitmaps[] = {" + ", ".join(f"bitmap_{i}" for i in range(len(bitmaps))) + "};"

  file_contents = "#define _GxBitmaps400x300_H_\n\n#include <pgmspace.h>\n\n" + "\n".join(bitmaps) + "\n" + bitmaps_list

  # # write to file
  with open("custom_bitmaps.h", "w") as file:
    file.write(file_contents)
    