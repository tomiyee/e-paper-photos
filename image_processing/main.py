from typing import Literal
import inquirer
from tqdm import tqdm
from generate_bin_files import convert_to_bin, save_to_binary_file
from generate_bitmap_h import generate_bitmap_h
from generate_bmp_files import convert_to_bmp, load_images


HEADER_OPTION = "A Header File (no SD card)"
BMP_DIR_OPTION = "BMP Files (for SD Card)"
BIN_DIR_OPTION = "BIN Files (for SD Card)"


def positive_integer(_: dict[str, str], text: str) -> Literal[True]:
    """Validates that the string is a positive integer"""
    try:
        if int(text) <= 0 or int(text) != float(text):
            raise inquirer.errors.ValidationError(
                "", reason="Please enter a positive integer."
            )
    except Exception:
        raise inquirer.errors.ValidationError("", reason="Please enter a number")
    return True


# An enum for each of the inquirer fields
class Field:
    WIDTH = "width"
    HEIGHT = "height"
    COLORS = "colors"
    INPUT_DIR = "input_dir"
    OUTPUT = "output"
    OUTPUT_DIR = "output_dir"
    SHOULD_GENERATE_PREVIEW = "should_gen_preview"
    PREVIEW_DIR = "preview_dir"
    HEADER_FILE_NAME = "header_file_name"


def perform_script() -> None:
    answers = inquirer.prompt(
        [
            inquirer.Text(
                Field.WIDTH,
                message="Width of the display",
                default="400",
                validate=positive_integer,
            ),
            inquirer.Text(
                Field.HEIGHT,
                message="Height of the display",
                default="300",
                validate=positive_integer,
            ),
            inquirer.Text(
                Field.COLORS,
                message="Number of colors (binary is 2)",
                default="4",
                validate=positive_integer,
            ),
            inquirer.Path(
                Field.INPUT_DIR,
                message="Directory with images?",
                default="input_images",
            ),
            inquirer.List(
                Field.OUTPUT,
                message="Save images as:",
                choices=[BIN_DIR_OPTION, BMP_DIR_OPTION, HEADER_OPTION],
                default=BIN_DIR_OPTION,
            ),
        ]
    )
    if answers is None:
        return

    # Save the images as a directory of BMP Images
    if answers[Field.OUTPUT] is BMP_DIR_OPTION:
        followup_answers = inquirer.prompt(
            [
                inquirer.Path(
                    Field.OUTPUT_DIR,
                    message="Directory to put BMP files?",
                    default="output_images",
                ),
            ]
        )
        if followup_answers is None:
            return
        # load the images from the directory
        raw_image_data = load_images(
            input_directory=answers[Field.INPUT_DIR],
            dimensions=(int(answers[Field.WIDTH]), int(answers[Field.HEIGHT])),
        )

        output_dir = followup_answers[Field.OUTPUT_DIR]
        for filename, image in tqdm(raw_image_data, desc="Convert to BMP Files"):
            # convert the images into the BMP format
            bmp_data = convert_to_bmp(image, colors=int(answers[Field.COLORS]))
            # save the BMP formatted images into the directory
            bmp_data.save(f"{output_dir}/{filename}.bmp")

    # Save the images as a directory of BMP Images
    if answers[Field.OUTPUT] is BIN_DIR_OPTION:
        followup_answers = inquirer.prompt(
            [
                inquirer.Path(
                    Field.OUTPUT_DIR,
                    message="Directory to put BIN files?",
                    default="output_images",
                ),
                inquirer.Confirm(
                    Field.SHOULD_GENERATE_PREVIEW,
                    message="Generate BMP for previewing?",
                    default=True,
                ),
                inquirer.Path(
                    Field.PREVIEW_DIR,
                    message="Directory to put BMP files?",
                    default="preview_images",
                    ignore=lambda answers: not answers[Field.SHOULD_GENERATE_PREVIEW],
                ),
            ]
        )
        if followup_answers is None:
            return
        # load the images from the directory
        raw_image_data = load_images(
            input_directory=answers[Field.INPUT_DIR],
            dimensions=(int(answers[Field.WIDTH]), int(answers[Field.HEIGHT])),
        )

        output_dir = followup_answers[Field.OUTPUT_DIR]
        preview_dir = followup_answers[Field.PREVIEW_DIR]
        for filename, image in tqdm(raw_image_data, desc="Convert to BMP Files"):
            # convert the images into the BMP format
            bin_data = convert_to_bin(image, colors=int(answers[Field.COLORS]))
            # save the BMP formatted images into the directory
            save_to_binary_file(bin_data, f"{output_dir}/{filename}.bin")

            # generate bin
            if followup_answers[Field.SHOULD_GENERATE_PREVIEW]:
                bmp_data = convert_to_bmp(image, colors=int(answers[Field.COLORS]))
                # save the BMP formatted images into the directory
                bmp_data.save(f"{preview_dir}/{filename}.bmp")

    # Save the images as a single header file of bitmap arrays
    elif answers[Field.OUTPUT] is HEADER_OPTION:
        followup_answers = inquirer.prompt(
            [
                inquirer.Text(
                    Field.HEADER_FILE_NAME,
                    message="Name for the Header File",
                    default="custom_bitmaps.h",
                )
            ]
        )
        if followup_answers is None:
            return
        # load the images from the directory
        raw_image_data = load_images(
            input_directory=answers[Field.INPUT_DIR],
            dimensions=(int(answers[Field.WIDTH]), int(answers[Field.HEIGHT])),
        )
        bmp_images = [
            convert_to_bmp(image, colors=int(answers[Field.COLORS]))
            for _, image in tqdm(raw_image_data, desc="Convert to BMP Files")
        ]

        output_file = followup_answers[Field.HEADER_FILE_NAME]
        file_contents = generate_bitmap_h(bmp_images)
        with open(output_file, "w") as file:
            file.write(file_contents)


if __name__ == "__main__":
    perform_script()
