from PIL import Image
import numpy as np
from pillow_heif import register_heif_opener
import glob

# Enables opening HEIF files in default supported by PIL
register_heif_opener()

input_dir = "output_images"

def generate_bitmap_h (input_dir='output_images', output_file='custom_bitmaps.h') -> None:
  """Converts `.bmp` images in the `input_dir` to group of uint_8 arrays in a header file with the name `output_file`

  Args:
      input_dir (str, optional): The directory containing the `.bmp` files. Defaults to 'output_images'.
      output_file (str, optional): The name of the file to place the generated C code. Defaults to 'custom_bitmaps.h'.
  """
  bitmaps = []
  for filepath in glob.glob(f"{input_dir}/*"):
    # Ignore the README file in the input directory
    if filepath.endswith("README.md"):
      break
    try:
      print(f"Processing: {filepath}")
      # Read the image, giving a single bit to each pixel
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
  generated_bitmaps = ", ".join(f"bitmap_{i}" for i in range(len(bitmaps)))
  file_imports = "#define _GxBitmaps400x300_H_\n\n#include <pgmspace.h>\n\n"
  bitmaps_list = "const unsigned char *bitmaps[] = {" + generated_bitmaps + "};"
  file_contents = file_imports + "\n".join(bitmaps) + "\n" + bitmaps_list

  # write to file
  with open(output_file, "w") as file:
    file.write(file_contents)

if __name__ == "__main__": 
  generate_bitmap_h()