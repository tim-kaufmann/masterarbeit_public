import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = [img for img in os.listdir(input_folder) if img.lower().endswith(('png', 'jpg', 'jpeg'))]
    images.sort()

    modified_images_info = "Modified images resolutions:\n"
    for i, img_name in enumerate(images):
        img_path = os.path.join(input_folder, img_name)
        img = Image.open(img_path).convert('RGB')
        img = img.resize(resolution)

        new_img_name = f"{i+1:03}.jpg"
        new_img_path = os.path.join(output_folder, new_img_name)
        img.save(new_img_path)

        modified_images_info += f"{new_img_name}: {resolution[0]} x {resolution[1]}\n"

    print(modified_images_info)
