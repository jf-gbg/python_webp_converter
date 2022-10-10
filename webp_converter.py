import os
import pathlib
import subprocess

def main():
    directory = os.getcwd()
    print("working in", directory)

    desired_quality = get_desired_quality()
    convert_files_to_webp(directory, desired_quality)

    print("Done")


def get_desired_quality():
    desired_quality = input("What should the resulting image quality be?" 
                                "(100 = same quality, 1 = lowest quality, " 
                                "80 and above is advised) ")
    return desired_quality  


def convert_files_to_webp(directory, desired_quality):
        for file in os.listdir(directory):
            file_name = file.split(".")[0]
            webp_convert_command = "cwebp -q " + desired_quality + " " + file + " -o " + file_name + ".webp"
            os.system(webp_convert_command)

main()