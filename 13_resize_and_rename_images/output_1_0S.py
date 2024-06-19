import os
from PIL import Image

def resize_and_rename_images(input_folder: str, output_folder: str, resolution: tuple):
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of image files and sort them
    image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))])

    resolutions = []

    for i, filename in enumerate(image_files, start=1):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Convert to RGB
            img = img.convert('RGB')
            # Resize image
            img = img.resize(resolution)
            # Save image with new name
            new_filename = f"{i:03}.jpg"
            img.save(os.path.join(output_folder, new_filename))
            # Store resolution for output
            resolutions.append(f"{new_filename}: {resolution[0]} x {resolution[1]}")

    # Print resolutions of modified images
    print("Modified images resolutions:")
    for res in resolutions:
        print(res)
