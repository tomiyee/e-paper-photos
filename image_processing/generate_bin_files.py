import math
from PIL import Image, ImageOps
from typing import List, Tuple
from tqdm import tqdm
import glob


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


def convert_to_bin(source_image: Image.Image, colors: int = 4) -> bytes:
    # Invert the image
    inverted_image = ImageOps.invert(source_image).quantize(
        4,
        palette=ImageOps.invert(source_image).convert("L").quantize(4),
        dither=Image.Dither.FLOYDSTEINBERG,
    )

    image_bytes = inverted_image.tobytes()
    bpp = math.ceil(math.log2(colors))

    result = bytearray()
    buffer = 0
    buffer_length = 0

    for byte in image_bytes:
        # Keep only the last bpp bits
        last_bits = byte & 2**bpp - 1
        # Add the n bits to the buffer
        buffer = (buffer << bpp) | last_bits
        buffer_length += bpp
        # If the buffer has a full byte, add it to the result
        if buffer_length >= 8:
            result.append((buffer >> (buffer_length - 8)) & 0xFF)
            buffer_length -= 8

    # If there are remaining bits in the buffer, append them as a final byte
    if buffer_length > 0:
        result.append((buffer << (8 - buffer_length)) & 0xFF)

    return bytes(result)


def save_to_binary_file(byte_string: bytes, filename: str) -> None:
    try:
        with open(filename, "wb") as binary_file:
            binary_file.write(byte_string)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


if __name__ == "__main__":
    images = load_images("input_images", (400, 300))
    test_image = images[0][1]

    im_bytes = convert_to_bin(test_image, colors=4)

    result = bytearray()
    bytes_per_shade = int(100 * 300 / 4)

    for i in range(bytes_per_shade):
        result.append(0b00000000)
    for i in range(bytes_per_shade):
        result.append(0b01010101)
    for i in range(bytes_per_shade):
        result.append(0b10101010)
    for i in range(bytes_per_shade):
        result.append(0b11111111)

    save_to_binary_file(result, "./test2.bin")
