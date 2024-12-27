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

Place horizontal images in the `/input_images` directory before running the script. It should support most image formats, including PNG, JPG, and HEIF files.

```bash
python main.py
```

The color images are converted to grayscale images using the Floyd-Steinberg dithering algorithm. If you want to load the BMP files from an SD card, you are done. Otherwise, the scsript will generate a header file with the bitmaps loaded as a list of char arrays.