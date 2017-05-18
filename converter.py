import os
from PIL import Image

files_count = 0

for file in os.listdir():
    if file.endswith('.webp'):
        image = Image.open(file).convert("P")
        image.save(file + ".png", "PNG")
        files_count += 1

print(str(files_count) + " files converted")
