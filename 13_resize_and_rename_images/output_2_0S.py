import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = [f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    images.sort()
    
    for i, image_name in enumerate(images):
        image_path = os.path.join(input_folder, image_name)
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            img = img.resize(resolution)
            new_image_name = f"{i+1:03d}.jpg"
            img.save(os.path.join(output_folder, new_image_name))
    
    print("Modified images resolutions:")
    for i in range(1, len(images) + 1):
        print(f"{i:03d}.jpg: {resolution[0]} x {resolution[1]}")
