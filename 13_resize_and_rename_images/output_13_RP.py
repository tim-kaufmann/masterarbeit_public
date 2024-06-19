import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = sorted(os.listdir(input_folder))
    resized_images_info = "Modified images resolutions:\n"

    for index, image_name in enumerate(images):
        image_path = os.path.join(input_folder, image_name)
        with Image.open(image_path) as img:
            rgb_img = img.convert('RGB')
            resized_img = rgb_img.resize(resolution)
            new_image_name = f"{index+1:03}.jpg"
            resized_img.save(os.path.join(output_folder, new_image_name))
            resized_images_info += f"{new_image_name}: {resolution[0]} x {resolution[1]}\n"
    
    print(resized_images_info)
