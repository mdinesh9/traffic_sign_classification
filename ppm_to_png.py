import glob
import os

import cv2
from PIL import Image

INPUT_DIR = "Images"
OUTPUT_DIR = os.path.join(INPUT_DIR, "pngs")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def convert():
    input_dirpath = os.path.join(INPUT_DIR, "*.ppm")
    ppm_files = glob.glob(input_dirpath)

    for f in ppm_files:
        img = Image.open(f)
        img.thumbnail((32, 32), Image.ANTIALIAS)

        out_path = f.split("/")[-1].replace(".ppm","")
        img.save(os.path.join(OUTPUT_DIR, out_path + ".png"))

    OUTPUT_DIR
    


if __name__ == "__main__":
    convert()