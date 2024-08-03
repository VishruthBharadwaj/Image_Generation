

# Random Shape Generator

This Python script generates images with basic shapes such as circles, squares, and triangles, either in 2D or 3D. The process begins with an AI model randomly selecting the shapes and colors to be used. Multiple colors can be applied to the image.

## Features

- Randomly selects between 2D and 3D shapes
- Randomly selects shapes (circle, square, triangle for 2D; cube, pyramid, sphere for 3D)
- Randomly selects colors for each shape
- Generates and saves images with the selected shapes and colors

## Dependencies

- `matplotlib`: For drawing and visualizing shapes
- `numpy`: For numerical operations and creating vertices for 3D shapes

## Installation

To install the necessary dependencies, run:

```sh
pip install matplotlib numpy


**
## Usage**
To generate an image with random shapes and colors, simply run the script:

python random_shape_generator.py


The script will generate either 2d_shapes.png or 3d_shapes.png based on the randomly selected shape type and save it in the current directory.


