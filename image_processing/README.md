# Image Processing Scripts

This folder will have a number of Python Scripts 

## Setup the Virtual Environment

Before using the Python Scripts, install the dependencies in `requirements.txt`. I would recommend creating a virtual envornment either manually or using `conda`.

> I developed this on Windows 11 and made the virtual environment manually in Powershell. If you want to do the same, I wouldn't recommend it. Use `conda` or other tool. That said, to create the virtual environment:
> ```
> python -m venv env
> ```
> Then, look up the specific command to run depending on the terminal you are using [here](https://docs.python.org/3/library/venv.html#how-venvs-work). For Powershell users, you may need to set the ExecutionPolicy to unrestricted. 
> ```
> Set-ExecutionPolicy Unrestricted -Force
> ```
> Once you have activated the virtual env, you can install the requirements with `pip`
> ```bash
> pip install -r requirements.txt
> ```

## The Script

The main utility in this script is to process any images in the `/input_images` directory place the resulting binary images (`.bmp` files) in the `/output_images` directory. 

Place horizontal images in the `/input_images` directory before running the script. It should support most image formats, including PNG, JPG, and HEIF files.

```bash
python generate_bmp_files.py
```

The color images are converted to binary images (each pixel is either pure black or white) using the Floyd-Steinberg dithering algorithm.