from typing import List, Tuple
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import glob
from tqdm import tqdm

# Enables opening HEIF files in default supported by PIL
register_heif_opener()


def load_images(
    input_directory: str, dimensions: Tuple[int, int] = (400, 300)
) -> List[Tuple[str, Image.Image]]:
    """
    Loads all of the images in the input directory and returns them as a list
    of PIL Image objects.

    If an image fails to load, it is printed to the console and omitted from
    the returned list
    """
    images = []
    input_dir_len = len(input_directory) + 1
    for filepath in tqdm(glob.glob(f"{input_directory}/*"), desc="Reading Images"):
        filename = "".join(filepath[input_dir_len:].split(".")[:-1])
        # Ignore the README file in the input directory
        if filepath.endswith("README.md"):
            continue
        try:
            im_frame = Image.open(filepath)
            # JPEGs can have EXIF Orientation Data sometimes
            ImageOps.exif_transpose(im_frame, in_place=True)
            im_frame = im_frame.resize(dimensions)
            images.append((filename, im_frame))
        except Exception as e:
            print("Failed to process:", filepath)
            print(e)
    return images


def convert_to_bmp(source_image: Image.Image, colors: int = 2) -> Image.Image:
    """
    Converts the source image to a BMP image with the specified number of
    colors. The default is 2 colors.
    """
    im_frame = source_image.copy()
    # Converts to 1-bit per pixel. Uses Floyd-Steinberg dithering
    if colors == 2:
        im_frame = im_frame.convert("1")
    # Converts to multiple bits per pixel. Uses Floyd-Steinberg dithering
    else:
        im_frame = im_frame.quantize(
            colors,
            palette=im_frame.convert("L").quantize(colors),
            dither=Image.Dither.FLOYDSTEINBERG,
        )
    return im_frame


if __name__ == "__main__":
    input_dir = "input_images"
    output_dir = "output_images"

    images = load_images(input_dir, dimensions=(400, 300))

    for filename, image_data in images:
        bmp_image = convert_to_bmp(image_data)
        bmp_image.save(f"{output_dir}/{filename}.bmp")
