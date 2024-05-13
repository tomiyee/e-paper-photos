from typing import List
from PIL import Image
import inquirer
import numpy as np
from pillow_heif import register_heif_opener
import glob
from tqdm import tqdm

# Enables opening HEIF files in default supported by PIL
register_heif_opener()


def generate_bitmap_h(bmp_imgs: List[Image.Image]) -> str:
    """Converts the list of BMP images to the contents of a bitmap header file

    Args:
        input_dir (str, optional): The directory containing the `.bmp` files.
        Defaults to 'output_images'.
        output_file (str, optional): The name of the generated C code file.
        Defaults to 'custom_bitmaps.h'.
    """
    # A list of strings, each a variable defn for a bitmap in C
    bitmaps: List[str] = []
    for bitmap_image in tqdm(bmp_imgs, desc="Convert to Header File"):
        # Read the image, giving a single bit to each pixel
        bitmap_image = bitmap_image.convert("L")
        palette = sorted(list(set(bitmap_image.getdata())))
        base = int(np.ceil(np.log2(len(palette))))
        palette_binary = [(bin(i)[2:]).rjust(base, "0") for i in range(len(palette))]
        # group the bitmap every eight bits
        image_data = np.array(bitmap_image.getdata()).astype(str)
        # convert
        for b, c in zip(palette_binary, palette):
            image_data[image_data == str(c)] = b
        image_data = np.array(list("".join(image_data.astype(str))))
        image_data = image_data.reshape((-1, 8))
        # convert each row to a string of eight 0s and 1s
        image = np.array(["".join(row) for row in image_data.astype(str)])
        # read each binary string as a binary number (0 to 15)
        image = np.array([int(row, 2) for row in image])
        # convert the binary number into a hex number
        image = np.array([hex(row) for row in image])
        # For formatting, each row of the image is 30 bytes
        image = image.reshape(-1, 50)
        # convert each row to a string
        bitmap_arr_rows_str = np.array([",".join(row) for row in image.astype(str)])
        # concatenate the rows
        bitmap_arr_str = ",\n".join(bitmap_arr_rows_str)
        bitmap_var = (
            "const unsigned char bitmap_"
            + str(len(bitmaps))
            + "[] PROGMEM = {\n"
            + bitmap_arr_str
            + "};\n"
        )
        bitmaps.append(bitmap_var)

    generated_bitmaps = ", ".join(f"bitmap_{i}" for i in range(len(bitmaps)))
    file_imports = "#define _GxBitmaps400x300_H_\n\n#include <pgmspace.h>\n\n"
    bitmaps_list = "const unsigned char *bitmaps[] = {" + generated_bitmaps + "};"
    file_contents = file_imports + "\n".join(bitmaps) + "\n" + bitmaps_list

    return file_contents


if __name__ == "__main__":

    answers = inquirer.prompt(
        [
            inquirer.Path(
                "input_dir",
                message="Folder with .bmp files:",
                exists=True,
                path_type=inquirer.Path.DIRECTORY,
            ),
            inquirer.Text(
                "output_file",
                "custom_bitmaps.h",
                message="Name of file:",
            ),
        ]
    )
    if answers is None:
        exit()
    input_dir = answers["input_dir"].rstrip("/\\")
    output_file: str = answers["output_file"]
    output_file = output_file if output_file.endswith(".h") else output_file + ".h"
    bmp_files = [Image.open(filepath) for filepath in glob.glob(f"{input_dir}/*")]

    images = []
    for filepath in glob.glob(f"{input_dir}/*"):
        # Ignore the README file in the input directory
        if filepath.endswith("README.md"):
            break
        try:
            # Read the image, giving a single bit to each pixel
            bitmap_image = Image.open(filepath)
            images.append(bitmap_image)
        except Exception as e:
            print("Failed to load:", filepath)
            print(e)

    file_contents = generate_bitmap_h(images)
    # write to file
    with open(output_file, "w") as file:
        file.write(file_contents)
