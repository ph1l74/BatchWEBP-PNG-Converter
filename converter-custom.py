import os

from PIL import Image

path_src = input("Input the path to directory with *.webp files: ")
path_dst = input("Input the path to directory with *.png files. (If you want to place files in the same directory just "
                 "press 'Enter'): ")
if not path_dst:
    path_dst = path_src

files_count = 0

print("Processing...")
for file in os.listdir(path_src):
    if file.endswith('.webp'):
        image = Image.open(path_src + file).convert("P")
        image.save(path_dst + file + ".png", "PNG")
        files_count += 1

print("{} files converted from {} to {}" .format(str(files_count), path_src, path_dst))
