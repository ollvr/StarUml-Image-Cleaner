## Introduction

This Python program effectively cleans and simplifies SVG files exported from StarUML, removing unnecessary background elements that hinder readability. It leverages the cairosvg library for SVG rendering and xml.etree.ElementTree for parsing, generating both a cleaned SVG and a high-quality image.

## Benefits:

Enhanced Readability: Eliminate distracting backgrounds for clear diagram comprehension.
Format Flexibility: Choose between cleaned SVG or image format depending on your needs.
 
## Requirements:

Python 3.x (download from https://www.python.org/downloads/)
cairosvg library:
Run pip install cairosvg to install it.

## Installation:

Clone Repository: Use git clone https://github.com/ollvr/StarUml-Image-Cleaner.git to clone this repository.
Install Dependency: Run pip install cairosvg to install the required library.
Usage:

Update File Path:
Open clean_staruml_svg.py in a text editor.
Locate the variable file_path and replace "Your SVG file path" with the actual path to your StarUML-exported SVG file.
Run the Script: Execute python clean_staruml_svg.py in your terminal/command prompt.

## Disclaimer:

The cleaning process might require adjustments for highly customized StarUML diagrams. Please report any issues or suggest enhancements on GitHub.


If you find this program useful, please show your appreciation by giving it a star on GitHub! Your support motivates further development and helps others enjoy cleaner StarUML exports.