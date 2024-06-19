import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of image files in the input folder and sort them
    image_files = sorted(os.listdir(input_folder))
    
    modified_images_resolutions = "Modified images resolutions:\n"
    
    for idx, image_file in enumerate(image_files):
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, f"{idx + 1:03d}.jpg")
        
        with Image.open(input_path) as img:
            # Convert image to RGB
            img = img.convert("RGB")
            # Resize image
            img = img.resize(resolution)
            # Save image to the output folder
            img.save(output_path)
            # Add resolution info to the output string
            modified_images_resolutions += f"{idx + 1:03d}.jpg: {resolution[0]} x {resolution[1]}\n"
    
    # Output the resolutions of the modified images
    print(modified_images_resolutions)

