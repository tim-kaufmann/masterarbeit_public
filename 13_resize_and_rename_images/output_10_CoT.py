import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, new_resolution):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Get list of images sorted by name
    images = sorted(os.listdir(input_folder))
    
    resolutions = []
    
    for idx, image_name in enumerate(images, start=1):
        # Open image
        image_path = os.path.join(input_folder, image_name)
        with Image.open(image_path) as img:
            # Convert to RGB
            rgb_image = img.convert("RGB")
            # Resize image
            resized_image = rgb_image.resize(new_resolution)
            # Create new file name
            new_image_name = f"{idx:03d}.jpg"
            new_image_path = os.path.join(output_folder, new_image_name)
            # Save image
            resized_image.save(new_image_path, "JPEG")
            # Store resolution for output
            resolutions.append((new_image_name, new_resolution))
    
    # Output the resolutions
    print("Modified images resolutions:")
    for image_name, (width, height) in resolutions:
        print(f"{image_name}: {width} x {height}")

