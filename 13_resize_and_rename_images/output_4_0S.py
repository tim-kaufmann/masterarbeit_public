import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    
    # Sort the image files by name
    image_files.sort()

    # Process each image
    for index, filename in enumerate(image_files):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Convert image to RGB
        img = img.convert('RGB')

        # Resize image to the specified resolution
        img = img.resize(resolution, Image.ANTIALIAS)

        # Generate new filename with leading zeros
        new_filename = f"{index+1:03}.jpg"
        new_path = os.path.join(output_folder, new_filename)

        # Save the image to the output folder
        img.save(new_path, 'JPEG')

    # Output the resolution of all images in the modified folder
    print("Modified images resolutions:")
    for index in range(len(image_files)):
        new_filename = f"{index+1:03}.jpg"
        new_path = os.path.join(output_folder, new_filename)
        img = Image.open(new_path)
        print(f"{new_filename}: {img.width} x {img.height}")
