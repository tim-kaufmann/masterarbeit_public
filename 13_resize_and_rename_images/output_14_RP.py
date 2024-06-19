import os
from PIL import Image

def resize_and_rename_images(input_folder: str, output_folder: str, resolution: tuple):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of images in the input folder
    image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))])

    # Process and rename images
    modified_images = []
    for idx, image_file in enumerate(image_files, start=1):
        # Open image
        img = Image.open(os.path.join(input_folder, image_file)).convert('RGB')
        # Resize image
        img_resized = img.resize(resolution)
        # Create new filename with zero-padded index
        new_filename = f'{idx:03}.jpg'
        new_filepath = os.path.join(output_folder, new_filename)
        # Save resized image
        img_resized.save(new_filepath)
        # Store information about modified image
        modified_images.append((new_filename, resolution))

    # Output the resolution of all modified images
    print("Modified images resolutions:")
    for filename, res in modified_images:
        print(f"{filename}: {res[0]} x {res[1]}")
