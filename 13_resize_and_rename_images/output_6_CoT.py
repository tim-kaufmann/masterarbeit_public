import os
from PIL import Image

def resize_and_rename_images(input_folder: str, output_folder: str, resolution: tuple):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of image files and sort them
    image_files = sorted([f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))])
    
    modified_images = []
    
    for i, filename in enumerate(image_files, start=1):
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Convert image to RGB
            img = img.convert('RGB')
            
            # Resize image
            img = img.resize(resolution)
            
            # Save the image with a new name
            new_filename = f"{i:03}.jpg"
            img.save(os.path.join(output_folder, new_filename))
            
            # Append resolution information for output
            modified_images.append(f"{new_filename}: {resolution[0]} x {resolution[1]}")
    
    # Output the resolutions of all modified images
    print("Modified images resolutions:")
    for info in modified_images:
        print(info)
