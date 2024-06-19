import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    images.sort()
    
    modified_images_info = "Modified images resolutions:\n"
    
    for i, image_name in enumerate(images):
        with Image.open(os.path.join(input_folder, image_name)) as img:
            rgb_img = img.convert('RGB')
            resized_img = rgb_img.resize(resolution)
            new_image_name = f"{i+1:03}.jpg"
            resized_img.save(os.path.join(output_folder, new_image_name))
            modified_images_info += f"{new_image_name}: {resolution[0]} x {resolution[1]}\n"
    
    print(modified_images_info)
