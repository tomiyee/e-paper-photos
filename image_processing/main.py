import inquirer

from generate_bitmap_h import generate_bitmap_h
from generate_bmp_files import generate_bmp_files

HEADER_OPTION = "A Header File (no SD card)"
BMP_DIR_OPTION = "BMP Files (for SD Card)"

def positive_integer(answers, text: str):
  """Validates that the string is a positive integer"""
  try:
    if int(text) <= 0 or int(text) != float(text):
      raise inquirer.errors.ValidationError("", reason="Please enter a positive integer.")
  except Exception as e:
    raise inquirer.errors.ValidationError("", reason="Please enter a number")
  return True


def perform_script() -> None:
  answers = inquirer.prompt([
    inquirer.List(
      "output", 
      message='Save images as:', 
      choices=[BMP_DIR_OPTION, HEADER_OPTION], 
      default=HEADER_OPTION
    ),
    inquirer.Path(
      "input_dir", 
      message="Directory with images?", 
      default="input_images"
    ),
    inquirer.Path(
      "output_dir", 
      message="Directory to put BMP files?", 
      default="output_images"
    ),
    inquirer.Text(
      "width", 
      message="Width of the display", 
      default="400", 
      validate=positive_integer
    ),
    inquirer.Text(
      "height", 
      message="Height of the display", 
      default="300", 
      validate=positive_integer
    ),
  ])
  # Keyboard interrupt
  if answers is None:
     return
  output_dir = answers['output_dir']
  generate_bmp_files(
    input_dir=answers['input_dir'], 
    output_dir=output_dir, 
    dimentions=[
      int(answers['width']), 
      int(answers['height'])
    ]
  )

  if answers["output"] == HEADER_OPTION:
    answers = inquirer.prompt([
      inquirer.Text(
        "header_file_name",
        message="Name for the Header File",
        default="custom_bitmaps.h"
      )
    ])
    if answers is not None:
      generate_bitmap_h(
        input_dir=output_dir,
        output_file=answers["header_file_name"]
      )

if __name__ == "__main__":
   perform_script()