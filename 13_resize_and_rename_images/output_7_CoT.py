import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    image_files.sort()

    for idx, image_file in enumerate(image_files):
        with Image.open(os.path.join(input_folder, image_file)) as img:
            rgb_img = img.convert('RGB')
            resized_img = rgb_img.resize(resolution)
            new_filename = f"{idx+1:03}.jpg"
            resized_img.save(os.path.join(output_folder, new_filename))
    
    print("Modified images resolutions:")
    for idx, image_file in enumerate(image_files):
        new_filename = f"{idx+1:03}.jpg"
        with Image.open(os.path.join(output_folder, new_filename)) as img:
            width, height = img.size
            print(f"{new_filename}: {width} x {height}")