# ImagiForge

ImagiForge is an all-in-one image editing tool written in Python. It provides various operations to modify images, such as changing the aspect ratio, brightness, and contrast. The tool uses the Python Imaging Library (PIL) to perform image manipulation.

## Features

* Change aspect ratio: Resize the image by specifying a new width and height.
* Change brightness: Adjust the brightness of the image by providing a value between -1.0 and 1.0.
* Change contrast: Modify the contrast of the image by specifying a value between 0.0 and 2.0.
* Crop image: Select a rectangular region of interest within the image.
* Rotate image: Rotate the image by a specified angle in degrees.

## Usage

1. Install the required dependencies:
   ```shell
   pip install pillow

2. Run the script
   ```shell
   python imagiforge.py

3. Enter the path of the image file when prompted.

4. Choose the desired operation from the available options by entering the corresponding number.

5. Provide additional details if necessary (e.g., new aspect ratio, brightness value, etc.).

6. Enter the output filename prefix.

7. The modified image will be saved in the same directory with the provided prefix and operation number appended to the filename.
