import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = [f for f in os.listdir(input_folder) if f.endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff'))]
    images.sort()
    
    for index, image_name in enumerate(images):
        img = Image.open(os.path.join(input_folder, image_name))
        img = img.convert("RGB")
        img = img.resize(resolution, Image.ANTIALIAS)
        
        new_name = f"{index + 1:03}.jpg"
        img.save(os.path.join(output_folder, new_name), "JPEG")

    print("Modified images resolutions:")
    for index in range(len(images)):
        new_name = f"{index + 1:03}.jpg"
        print(f"{new_name}: {resolution[0]} x {resolution[1]}")
