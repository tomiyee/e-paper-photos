import numpy as np
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import glob

# Enables opening HEIF files in default supported by PIL
register_heif_opener()

def generate_bmp_files(input_dir="input_images", output_dir="output_images", dimentions: tuple[int, int]=(400,300)) -> None:
  """
  Reads all of the images in the `input_images` directory, resizes them, dithers, and saves the BMP files
  to the `output_dir. Supports most image types, including PNG, JPG, and HEIF images.

  Args:
      input_dir (str, optional): The folder to read image files. Defaults to "input_images".
      output_dir (str, optional): The folder to place `.bmp` files. Defaults to "output_images".
      dimentions (tuple[int, int], optional): The target (width, height) of the image. Defaults to (400,300).
  """
  for filepath in glob.glob(f"{input_dir}/*"):
    # Ignore the README file in the input directory
    if filepath.endswith("README.md"):
      break
    filename = "".join(filepath[len(input_dir)+1:].split('.')[:-1])
    print(f"Processing: {filepath}")
    try:
      im_frame = Image.open(filepath)
      # JPEGs can have EXIF Orientation Data sometimes
      im_frame = ImageOps.exif_transpose(im_frame)
      # Resize the image
      im_frame = im_frame.resize(dimentions)
      # Converts to 1-bit repr per pixel. Uses Floyd-Steinberg dithering
      im_frame = im_frame.convert("1")
      im_frame.save(f"{output_dir}/{filename}.bmp")
    except Exception as e:
      print("Failed to process:", filepath)
      print(e)

if __name__ == "__main__":
  generate_bmp_files()
