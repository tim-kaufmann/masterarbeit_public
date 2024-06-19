import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of images in the input folder
    image_files = sorted(os.listdir(input_folder))
    
    output_str = "Modified images resolutions:\n"
    image_number = 1
    
    for file in image_files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, file)
            img = Image.open(img_path)
            img = img.convert('RGB')
            img = img.resize(resolution)
            
            new_file_name = f"{image_number:03}.jpg"
            new_img_path = os.path.join(output_folder, new_file_name)
            img.save(new_img_path)
            
            output_str += f"{new_file_name}: {resolution[0]} x {resolution[1]}\n"
            image_number += 1
    
    print(output_str)
