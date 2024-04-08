# Image Processing Scripts

This folder will have a number of Python Scripts 

## Setup the Virtual Environment

Before you can use the Python Scripts, you need to create a Python virtual environment. You may choose to do so either using conda or using Python directly. 

### Method 1 - Manually Creating a Virtual Environment

I developed this on my Windows device and opted to create a the virtual environment manually. If you use Powershell, I would recommend setting up the virtual environment using conda or a similar virtual environment tool.

To begin with, make sure you have an installation of Python on your device. Next, navigate to this directory and create the virtual environment. 
  
```
# Create the Python Environment
python -m venv venv
```

Next, you must activate the virtual environment. You know that you have successfully done so if your terminal now has a `(venv)` prefix. Look up the specific command to run depending on the terminal you are using. 

> Note for Powershell users: To activate the virtual envornment, you may need to set the ExecutionPolicy to unrestricted. 
> ```
> Set-ExecutionPolicy Unrestricted -Force
> ```

### Installing the Requirements

```bash
pip install -r requirements.txt
```

## The Scripts

In this section, I document the scripts that I made for creating bitmaps to load onto my device. 

An important note, the display I purchased is Black and White only and 400 px x 300 px. These values currently are hard coded. If you want to use these scripts for a display of a different screen size, you will need to modify the scripts for your purposes. I don't plan to support dithering in other color values for now.  

### Creating a Bitmap Header File

Once you've got a bitmap saved as `"image.png"`, you can run the `image_to_bitmap_h.py` script to generate a new `bitmap.h` file.

```bash
python image_to_bitmap_h.py
```

For simplicity and maintainability, I will also include these scripts into the SD Card.

