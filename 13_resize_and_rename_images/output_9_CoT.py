import os
from PIL import Image

def resize_and_rename_images(input_folder, output_folder, resolution):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    
    # Sort files by name
    files.sort()
    
    # Initialize a list to store the resolutions of the modified images
    resolutions = []

    # Process each file
    for i, file in enumerate(files):
        with Image.open(os.path.join(input_folder, file)) as img:
            # Convert the image to RGB format
            img = img.convert("RGB")
            # Resize the image
            img = img.resize(resolution)
            # Generate new filename with leading zeros
            new_filename = f"{i+1:03}.jpg"
            # Save the modified image to the output folder
            img.save(os.path.join(output_folder, new_filename))
            # Append the resolution information to the list
            resolutions.append(f"{new_filename}: {resolution[0]} x {resolution[1]}")

    # Print out the resolutions
    print("Modified images resolutions:")
    for res in resolutions:
        print(res)
