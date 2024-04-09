import numpy as np
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import glob

# Enables opening HEIF files in default supported by PIL
register_heif_opener()

input_dir = "input_images"

if __name__ == "__main__":
  """
  Reads all of the images in the `input_images` directory.

  Supports PNG, JPG, and HEIF images.
  """
  for filepath in glob.glob(f"{input_dir}/*"):
    # Ignore the README file in the input directory
    if filepath.endswith("README.md"):
      break
    filename = "".join(filepath[len(input_dir)+1:].split('.')[:-1])
    print("Processing:", filepath)
    try:
      im_frame = Image.open(filepath)
      # JPEGs can have EXIF Orientation Data sometimes
      im_frame = ImageOps.exif_transpose(im_frame)
      # Resize the image
      im_frame = im_frame.resize((400, 300))
      # Converts to 1-bit repr per pixel. Uses Floyd-Steinberg dithering
      im_frame = im_frame.convert("1")
      im_frame.save(f"output_images/{filename}.bmp")
    except Exception as e:
      print("Failed to process:", filepath)
      print(e)
