# python_webp_converter
Simple python 3 program that converts pictures in the current directory to webp.
Depends on Googles libwebp library: https://developers.google.com/speed/webp/docs/precompiled


Usage:
In terminal navigate to the folder images are contained in.
Run wep_converter.py - It can be placed and run from any directory and uses the current working directory as the folder it will work in.
An error will be given by the webp library if an attempt is made to convert a file that is not supported, the program will continue running and 
converting the other files in the directory.
